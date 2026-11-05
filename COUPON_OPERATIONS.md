# Course coupon operations

The four Udemy courses use the paid code `25OFF_TG_NOV_2026`. Each code is a separate coupon on each course. All four November paid coupons were created and verified enabled on November 5, 2026, at USD 149.99, with unlimited redemptions.

`course-offers.json` records the course IDs, canonical slugs, prices, and actual expiration timestamps. The November paid offers expire on December 6, 2026: IRD at 3:08 p.m. Eastern, MBS/ABS and FRTB at 3:09 p.m., and VaR at 3:10 p.m. These are 31-day offers, independent of calendar month-end.

Existing `FREE_TG_OCT_2026` coupons were preserved and verified enabled. They expire on November 6, 2026, at 12:41–12:43 a.m. Eastern; individual timestamps are recorded as `free_expires_at`. No November FREE coupons were created or advertised. Paid and FREE codes may therefore have different month suffixes. The release report records the Git revisions, production backup, deployment status, and live verification results for this rollover.

From the common website parent folder, validate the source:

```bash
python3 landing_page_tglauner.com/scripts/validate_course_offers.py
node visitor_analytics/tests/test_tracking_consent.js
python3 landing_page_tglauner.com/scripts/test_coupon_rollover.py
python3 landing_page_tglauner.com/scripts/check_production_links.py --report landing_page_tglauner.com/output/production-links.json
```

For the next monthly rollover, first inspect Udemy's existing coupons and allocations for all four course IDs. Reuse an existing matching enabled coupon. Create coupons only when requested, and verify the final code, price, and timezone-aware expiry on each course.

```bash
coupon-rollover OCT_2026 NOV_2026 --paid-prefix 25OFF_TG --preview
coupon-rollover OCT_2026 NOV_2026 --paid-prefix 25OFF_TG
```

The generic helper rolls both paid and FREE suffixes. For a paid-only rollover, apply only paid-code changes and preserve the verified FREE code, its timestamps, helper examples, and historical release notes.

Update the readable month labels, `course-offers.json` expiry values, and each course body's `data-offer-deadline` from the verified Udemy tables. These are intentionally not inferred from the code name. The source validator checks that pages and metadata agree.

The homepage and VaR page belong to the `landing_page_tglauner.com` repository. IRD, MBS/ABS, FRTB, and the shared tracker have separate repositories. Review each repository's diff and preserve unrelated edits. The VS Code status bar shows the active repository; `.vscode/settings.json` at the common parent enables discovery of sibling repositories.

Source edits and Udemy creation do not publish the website. An authorized release commits and pushes each repository, backs up production source outside the web root, and installs the reviewed Git revisions on the existing DigitalOcean droplet. Preserve sibling applications, `.env`, databases, and host-local agent state. Record the deployed commit IDs, backup path, and link-check results in the release report. Roll back the source from that backup and restart the existing visitor collector only when restoring its backend.

The canonical coupon and analytics skills are versioned under `cross_project_tools/skills/`. Their local discovery links are installed with `scripts/install_coupon_skills.sh`; real pre-existing skill directories receive small adapters rather than being replaced. The coupon helper and tests live in this website repository.

Analytics uses the existing shared tracker. These sites require consent before any analytics IDs or events; the cookie manager publishes consent changes, including changes in other tabs. Other applications retain their existing tracker defaults. The local browser check used an isolated collector database and confirmed zero events with Essential Only, followed by correctly attributed page views after enabling analytics.

The original mixed-architecture analytics environment is preserved as `.venv.pre-coupon-release`; the active environment uses `.venv/`. On Macs with universal Python builds, ensure binary wheels match the running process architecture. Run `make test` in the analytics repository before releasing its backend.

Production checks must cover all four public sites, canonical paid and FREE coupon links, preview links, cookie preferences, and the collector health endpoint. Report any browser or external-service validation limitations explicitly. Historical HAR files remain historical evidence.
