# TGIR Site Architecture Template

Use this file as the shared architecture note for TG Investments and Research web properties. The goal is that course pages, app launchers, and infrastructure pages feel like one system while allowing each page to emphasize its own product.

## Required Shell

Every site should use this top-level order:

1. Sticky header with TGIR icon, site name, and four to six anchor links.
2. First-screen hero with a real finance/product image or interactive quantitative scene.
3. Quant signal section when relevant: rates fan, callable boundary, XVA exposure, securitization waterfall, or risk-capital stack.
4. Primary offer or tool section with direct action links.
5. Systems or related destinations directory if the page is part of the broader TGIR network.
6. About/proof section written for serious practitioners.
7. Location/map band using the Manhasset address.
8. Compact legal footer.

## Shared Assets

Each site should keep local public assets under:

```text
assets/
```

At minimum:

```text
assets/favicon.png
assets/hero-bg.jpg
```

Use relative paths like `assets/favicon.png`, not `../assets/favicon.png`, so the site works when opened directly, served from its own folder, or served as a subdirectory.

## Brand Shell

Header requirements:

```html
<header class="site-header" aria-label="Primary">
  <a class="brand-lockup" href="#top" aria-label="TG Investments and Research home">
    <img class="brand-icon" src="assets/favicon.png" alt="" aria-hidden="true">
    <span class="brand-name">TG Investments and Research</span>
  </a>
  <nav class="primary-nav" aria-label="Main navigation">
    <a href="#courses">Courses</a>
    <a href="#systems">Systems</a>
    <a href="#about">About</a>
  </nav>
</header>
```

Avoid generic SaaS gradients and generic AI-looking cards. The TGIR house style is editorial, quantitative, and disciplined: warm paper background, graphite surfaces, deep red action color, muted green quant accent, restrained borders, real finance imagery, and dense but readable information.

## CSS Tokens

Use the same design tokens across pages:

```css
:root {
  --ink: #11100d;
  --ink-soft: #38332c;
  --paper: #f4f1e8;
  --paper-strong: #fffdf7;
  --graphite: #1c1c1a;
  --rail: #d9d1bd;
  --red: #9d1e22;
  --red-dark: #681114;
  --green: #77a857;
  --cyan: #4f8f9b;
  --gold: #c99935;
  --line: rgba(17, 16, 13, 0.16);
  --radius: 6px;
  --max: 1180px;
}
```

Typography:

- Display: `Iowan Old Style`, Georgia, serif.
- UI/body: `Avenir Next`, `Gill Sans`, `Trebuchet MS`, sans-serif.
- Quant/code labels: Menlo, Consolas, Monaco, monospace.
- Do not use viewport-scaled font sizes.
- Do not use negative letter spacing.

## Course Offer Pattern

Each course row should include:

- Course code.
- Direct, specific practitioner copy.
- Three practical bullets.
- Detail-page imagery copied from the live course detail page, not generic parent-page cards.
- Visible `25% OFF` badge when the linked Udemy URL has a coupon code.
- Coupon note using the exact `couponCode` token.
- Primary action: `Enroll on Udemy - 25% OFF` when a coupon is present.
- Secondary action: `Course details`.
- Real course image from `assets/`.

Use direct Udemy course URLs unless there is a current verified coupon code. Coupon URLs should keep the token in the query string, for example:

```text
https://www.udemy.com/course/mastering-interest-rate-derivatives/?couponCode=IRDERIVS25_APR_2026
```

## Quant Animation Pattern

When a site needs a sophisticated motion element, use a real quantitative concept rather than decorative particles.

Preferred patterns:

- Rates site: Hull-White style short-rate path fan, callable boundary, and exposure tail.
- XVA site: expected exposure, positive exposure tail, CVA/FVA/KVA layer stack.
- Securitization site: waterfall cashflow priority and prepayment scenario bands.
- FRTB site: sensitivities, curvature, default risk charge, and capital aggregation blocks.

For the rates animation, the concept should reference a one-factor Hull-White style process:

```text
dr = (theta(t) - a r) dt + sigma dW
```

The animation is a visual teaching signal, not a pricing engine. If mathematical accuracy is needed, route calculations to QuantLib or a backend model and label outputs accordingly.

## Systems Directory Rules

Order related systems like this when used on the parent site:

1. Interest Rate Derivatives
2. MBS and ABS
3. FRTB Fundamentals
4. XVA Essentials
5. QuantLib Tools
6. AI Value Advisor
7. Multi-Model Talkshow
8. Markets Dashboard
9. MCP endpoint

Do not include private/admin-only destinations in public launchers.

## Location Band

Use the map band near the bottom:

```html
<section class="location-section" aria-label="Location map">
  <div class="location-copy">
    <p class="kicker">Manhasset, New York</p>
    <h2>Rooted on the North Shore.</h2>
    <p>TG Investments and Research, LLC. PO Box 802, 155 Stonytown Road, Manhasset, NY 11030.</p>
  </div>
  <div class="map-frame">
    <iframe
      title="TG Investments and Research office location"
      src="https://www.google.com/maps?q=155+Stonytown+Rd,+Manhasset,+NY+11030&t=k&z=16&output=embed"
      loading="lazy"
      referrerpolicy="no-referrer-when-downgrade"
      allowfullscreen>
    </iframe>
  </div>
</section>
```

## Validation

For a static site:

```bash
python3 -m html.parser index.html
node --check app.js
python3 -m http.server 8080
```

Then open `http://localhost:8080/` from the site directory, or serve from the repo root and open the site subdirectory.
