(function () {
    const revealTargets = document.querySelectorAll(".reveal, .reveal-on-load");

    function showAll() {
        revealTargets.forEach((target) => target.classList.add("is-visible"));
    }

    if (!("IntersectionObserver" in window)) {
        showAll();
    } else {
        const observer = new IntersectionObserver(
            (entries) => {
                entries.forEach((entry) => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add("is-visible");
                        observer.unobserve(entry.target);
                    }
                });
            },
            { threshold: 0.16 }
        );

        revealTargets.forEach((target) => observer.observe(target));
        window.setTimeout(() => {
            document.querySelectorAll(".reveal-on-load").forEach((target) => {
                target.classList.add("is-visible");
            });
        }, 120);
    }

    const tabs = Array.from(document.querySelectorAll(".filter-tab"));
    const cards = Array.from(document.querySelectorAll(".system-card"));
    const search = document.getElementById("system-search");
    const empty = document.getElementById("empty-state");
    let activeFilter = "all";

    function normalize(value) {
        return value.trim().toLowerCase();
    }

    function applyFilters() {
        const query = search ? normalize(search.value) : "";
        let visibleCount = 0;

        cards.forEach((card) => {
            const kindMatches = activeFilter === "all" || card.dataset.kind === activeFilter;
            const searchable = normalize(
                [
                    card.dataset.search || "",
                    card.textContent || ""
                ].join(" ")
            );
            const queryMatches = !query || searchable.includes(query);
            const isVisible = kindMatches && queryMatches;

            card.hidden = !isVisible;
            if (isVisible) {
                visibleCount += 1;
            }
        });

        if (empty) {
            empty.hidden = visibleCount !== 0;
        }
    }

    tabs.forEach((tab) => {
        tab.addEventListener("click", () => {
            activeFilter = tab.dataset.filter || "all";
            tabs.forEach((item) => {
                const isActive = item === tab;
                item.classList.toggle("is-active", isActive);
                item.setAttribute("aria-pressed", String(isActive));
            });
            applyFilters();
        });
    });

    if (search) {
        search.addEventListener("input", applyFilters);
    }

    applyFilters();

    const canvas = document.getElementById("rates-lab-canvas");
    const modeButtons = Array.from(document.querySelectorAll(".lab-mode"));
    const modelReadout = document.getElementById("lab-model");
    const aReadout = document.getElementById("lab-a");
    const sigmaReadout = document.getElementById("lab-sigma");
    let labMode = "rates";
    const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    modeButtons.forEach((button) => {
        button.addEventListener("click", () => {
            labMode = button.dataset.labMode || "rates";
            modeButtons.forEach((item) => {
                const isActive = item === button;
                item.classList.toggle("is-active", isActive);
                item.setAttribute("aria-pressed", String(isActive));
            });
        });
    });

    if (!canvas) {
        return;
    }

    const context = canvas.getContext("2d");
    const pathCount = 34;
    const pointCount = 96;
    let paths = [];
    let animationStart = performance.now();
    let resizeQueued = false;

    function randomNormal() {
        let u = 0;
        let v = 0;
        while (u === 0) u = Math.random();
        while (v === 0) v = Math.random();
        return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v);
    }

    function buildPaths() {
        const meanReversion = 0.1;
        const volatility = 0.0115;
        const dt = 1 / 12;
        paths = [];

        for (let pathIndex = 0; pathIndex < pathCount; pathIndex += 1) {
            let rate = 0.041 + (Math.random() - 0.5) * 0.006;
            const path = [];
            for (let step = 0; step < pointCount; step += 1) {
                const time = step / 12;
                const theta = 0.038 + 0.007 * Math.sin(time * 0.85);
                rate += meanReversion * (theta - rate) * dt + volatility * Math.sqrt(dt) * randomNormal();
                const exposure = Math.max(0, (0.046 - rate) * 1800 + 12 * Math.sin(time * 1.4 + pathIndex));
                const callable = 0.045 + 0.004 * Math.sin(time * 0.72);
                path.push({ rate, exposure, callable });
            }
            paths.push(path);
        }

        if (aReadout) aReadout.textContent = "a 0.10";
        if (sigmaReadout) sigmaReadout.textContent = "sigma 1.15%";
    }

    function resizeCanvas() {
        const rect = canvas.getBoundingClientRect();
        const scale = window.devicePixelRatio || 1;
        const width = Math.max(640, Math.floor(rect.width * scale));
        const height = Math.max(360, Math.floor(rect.height * scale));

        if (canvas.width !== width || canvas.height !== height) {
            canvas.width = width;
            canvas.height = height;
        }
    }

    function xFor(step, width, pad) {
        return pad + (step / (pointCount - 1)) * (width - pad * 2);
    }

    function yForRate(rate, height, pad) {
        const minRate = 0.006;
        const maxRate = 0.071;
        const pct = (rate - minRate) / (maxRate - minRate);
        return height - pad - pct * (height - pad * 2);
    }

    function yForExposure(exposure, height, pad) {
        const pct = Math.min(1, exposure / 72);
        return height - pad - pct * (height - pad * 2);
    }

    function drawGrid(width, height, pad) {
        context.strokeStyle = "rgba(255,253,247,0.08)";
        context.lineWidth = 1;
        for (let i = 0; i < 8; i += 1) {
            const x = pad + (i / 7) * (width - pad * 2);
            context.beginPath();
            context.moveTo(x, pad);
            context.lineTo(x, height - pad);
            context.stroke();
        }
        for (let i = 0; i < 5; i += 1) {
            const y = pad + (i / 4) * (height - pad * 2);
            context.beginPath();
            context.moveTo(pad, y);
            context.lineTo(width - pad, y);
            context.stroke();
        }
    }

    function drawCurve(points, color, width, progress, valueAccessor, yAccessor, dash) {
        const maxStep = Math.max(2, Math.floor((pointCount - 1) * progress));
        context.save();
        context.strokeStyle = color;
        context.lineWidth = width;
        if (dash) {
            context.setLineDash(dash);
        }
        context.beginPath();
        for (let step = 0; step <= maxStep; step += 1) {
            const x = xFor(step, canvas.width, 58);
            const y = yAccessor(valueAccessor(points[step]), canvas.height, 58);
            if (step === 0) {
                context.moveTo(x, y);
            } else {
                context.lineTo(x, y);
            }
        }
        context.stroke();
        context.restore();
    }

    function drawQuantLab(now) {
        if (!paths.length) {
            buildPaths();
        }

        resizeCanvas();
        const width = canvas.width;
        const height = canvas.height;
        const progress = ((now - animationStart) % 9000) / 9000;
        const easedProgress = Math.min(1, progress * 1.16);

        context.clearRect(0, 0, width, height);
        context.fillStyle = "#080806";
        context.fillRect(0, 0, width, height);
        drawGrid(width, height, 58);

        const glow = context.createRadialGradient(width * 0.74, height * 0.2, 10, width * 0.74, height * 0.2, width * 0.75);
        glow.addColorStop(0, "rgba(119,168,87,0.16)");
        glow.addColorStop(1, "rgba(119,168,87,0)");
        context.fillStyle = glow;
        context.fillRect(0, 0, width, height);

        context.fillStyle = "rgba(255,253,247,0.66)";
        context.font = `${Math.max(13, Math.floor(width / 78))}px Menlo, Consolas, monospace`;
        context.fillText(labMode === "xva" ? "positive exposure profile" : "simulated short-rate paths", 58, 34);
        context.fillText("0Y", 58, height - 24);
        context.fillText("8Y", width - 88, height - 24);

        if (modelReadout) {
            modelReadout.textContent = labMode === "callable" ? "HW tree + call boundary" : labMode === "xva" ? "XVA exposure paths" : "Hull-White 1F";
        }

        paths.forEach((path, index) => {
            const opacity = 0.16 + (index % 5) * 0.025;
            if (labMode === "xva") {
                drawCurve(path, `rgba(79,143,155,${opacity + 0.08})`, 1.2, easedProgress, (point) => point.exposure, yForExposure);
            } else {
                drawCurve(path, `rgba(183,211,129,${opacity})`, 1.15, easedProgress, (point) => point.rate, yForRate);
            }
        });

        const mainPath = paths[0];
        if (labMode === "callable") {
            drawCurve(mainPath, "rgba(201,153,53,0.95)", 3, easedProgress, (point) => point.callable, yForRate, [10, 8]);
            context.fillStyle = "rgba(157,30,34,0.18)";
            context.beginPath();
            for (let step = 0; step < pointCount; step += 1) {
                const x = xFor(step, width, 58);
                const y = yForRate(mainPath[step].callable, height, 58);
                if (step === 0) {
                    context.moveTo(x, y);
                } else {
                    context.lineTo(x, y);
                }
            }
            context.lineTo(width - 58, 58);
            context.lineTo(58, 58);
            context.closePath();
            context.fill();
        }

        if (labMode === "xva") {
            context.fillStyle = "rgba(157,30,34,0.2)";
            context.beginPath();
            mainPath.forEach((point, step) => {
                const x = xFor(step, width, 58);
                const y = yForExposure(point.exposure + 18, height, 58);
                if (step === 0) {
                    context.moveTo(x, y);
                } else {
                    context.lineTo(x, y);
                }
            });
            for (let step = pointCount - 1; step >= 0; step -= 1) {
                const x = xFor(step, width, 58);
                const y = yForExposure(Math.max(0, mainPath[step].exposure - 14), height, 58);
                context.lineTo(x, y);
            }
            context.closePath();
            context.fill();
        }

        drawCurve(mainPath, labMode === "xva" ? "rgba(255,253,247,0.92)" : "rgba(255,253,247,0.86)", 2.3, easedProgress, labMode === "xva" ? (point) => point.exposure : (point) => point.rate, labMode === "xva" ? yForExposure : yForRate);

        if (!reduceMotion) {
            requestAnimationFrame(drawQuantLab);
        }
    }

    buildPaths();
    requestAnimationFrame(drawQuantLab);
    window.addEventListener("resize", () => {
        if (!resizeQueued) {
            resizeQueued = true;
            window.requestAnimationFrame(() => {
                resizeQueued = false;
                resizeCanvas();
            });
        }
    });
})();
