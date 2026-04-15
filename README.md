# landing_page_tglauner.com

Static landing page for `https://tglauner.com/`.

## Scope

- Main homepage markup: `index.html`
- Main homepage styles: `styles.css`
- Static assets: `assets/`

## Current Homepage Structure

- Course cards for Interest Rate Derivatives, MBS/ABS, and FRTB
- XVA Essentials launch section
- Live Systems Directory for demo navigation
- Public MCP section
- GitHub repositories section

## Verified Live Systems

The homepage `Systems` section is based on a droplet audit performed on April 14, 2026.

- `https://tglauner.com/`
- `https://tglauner.com/mastering_interest_rate_derivatives/`
- `https://tglauner.com/mastering_mbs_and_abs/`
- `https://tglauner.com/frtb_fundamentals/`
- `https://course-xva-essentials.tglauner.com/`
- `https://tglauner.com/dashboard/`
- `https://tglauner.com/multi_model_talkshow/`
- `https://tglauner.com/ai_value_advisor/`
- `https://tglauner.com/visitor_log/`
- `https://openclaw.tglauner.com/`
- `https://quant.tglauner.com/`
- `https://oil-gasoline-simulator-iran-war-2026.tglauner.com/`
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
  https://course-xva-essentials.tglauner.com/ \
  https://tglauner.com/dashboard/ \
  https://tglauner.com/multi_model_talkshow/ \
  https://tglauner.com/ai_value_advisor/ \
  https://tglauner.com/visitor_log/ \
  https://openclaw.tglauner.com/ \
  https://quant.tglauner.com/ \
  https://oil-gasoline-simulator-iran-war-2026.tglauner.com/ \
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
curl -sS https://oil-gasoline-simulator-iran-war-2026.tglauner.com/health
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
