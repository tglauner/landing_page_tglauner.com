# landing_page_tglauner.com

Static landing page for `https://tglauner.com/`.

## Scope

- Main homepage markup: `index.html`
- Main homepage styles: `styles.css`
- Homepage interactions and quantitative canvas: `app.js`
- Static assets: `assets/`

## Current Homepage Structure

- Image-led hero and capital-markets experience summary
- Interactive rates, callable-boundary, and XVA visualization
- Course offers for Interest Rate Derivatives, MBS/ABS, FRTB, and VaR
- XVA Essentials launch section
- Searchable and filterable live systems directory
- Public MCP section
- About, location map, and legal footer

## Verified Live Systems

The homepage `Systems` section is based on a droplet audit performed on April 14, 2026.

- `https://tglauner.com/`
- `https://tglauner.com/mastering_interest_rate_derivatives/`
- `https://tglauner.com/mastering_mbs_and_abs/`
- `https://tglauner.com/frtb_fundamentals/`
- `https://tglauner.com/value_at_risk/`
- `https://course-xva-essentials.tglauner.com/`
- `https://tglauner.com/dashboard/`
- `https://tglauner.com/visitor_log/`
- `https://openclaw.tglauner.com/`
- `https://quant.tglauner.com/`
- `https://tglauner.com/mcp`

Notes:

- The live MCP endpoint is `https://tglauner.com/mcp`.
- `mcp.tglauner.com` did not resolve during the audit.
- QuantLib Tools is live at `https://quant.tglauner.com/`.

## Local Validation

Serve the site locally:

```bash
python3 -m http.server 8000
```

Then open:

```text
http://localhost:8000/
```

## Production Deploy

Push from local:

```bash
git push origin main
```

Deploy on the droplet:

```bash
ssh root@45.55.196.120 "git -C /var/www/html pull --ff-only origin main"
```

## Production Smoke Checks

Homepage and app routes:

```bash
for url in \
  https://tglauner.com/ \
  https://tglauner.com/mastering_interest_rate_derivatives/ \
  https://tglauner.com/mastering_mbs_and_abs/ \
  https://tglauner.com/frtb_fundamentals/ \
  https://tglauner.com/value_at_risk/ \
  https://course-xva-essentials.tglauner.com/ \
  https://tglauner.com/dashboard/ \
  https://tglauner.com/visitor_log/ \
  https://openclaw.tglauner.com/ \
  https://quant.tglauner.com/ \
  https://tglauner.com/mcp
do
  echo "-- $url"
  curl -I -L -sS "$url" | sed -n '1,10p'
  echo
done
```

Health-oriented checks:

```bash
curl -sS https://tglauner.com/healthz
curl -sS "https://course-xva-essentials.tglauner.com/api/metrics/site_snapshot?host=course-xva-essentials.tglauner.com"
curl -sS https://quant.tglauner.com/health
```

## Rollback

If the latest homepage change needs to be reverted:

```bash
git revert HEAD
git push origin main
ssh root@45.55.196.120 "git -C /var/www/html pull --ff-only origin main"
```

## Course offers and shared skills

See `COUPON_OPERATIONS.md` and `course-offers.json` for the four-course inventory, shared coupon names, verified prices, and individual expirations. VaR is served from this repository's `value_at_risk/` directory.

Open `tglauner.code-workspace` to see the homepage, all course repositories, analytics, and shared skill repository together. Install the versioned coupon command and canonical skill discovery links:

```bash
bash scripts/install_coupon_skills.sh
python3 scripts/test_coupon_rollover.py
python3 scripts/validate_course_offers.py
python3 scripts/check_production_links.py --report output/production-links.json
```

The production checker visits the homepage and all four course sites, follows their legal pages, checks anchors and referenced assets, and reports external browser checks separately. Mail and phone links receive syntax checks; the checker does not send messages or place calls.
