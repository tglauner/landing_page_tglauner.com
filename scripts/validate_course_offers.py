#!/usr/bin/env python3
"""Validate the four paid course URLs and expiration timestamps in source."""
import json
import re
from pathlib import Path

MAIN = Path(__file__).resolve().parents[1]
ROOT = MAIN.parent
offers = json.loads((MAIN / 'course-offers.json').read_text())
assert re.fullmatch(r'25OFF_TG_(JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)_\d{4}', offers['paid_code'])
assert offers['free_code'] == offers['paid_code'].replace('25OFF_TG_', 'FREE_TG_')
assert len(offers['courses']) == 4
assert len({course['course_id'] for course in offers['courses']}) == 4
homepage = (MAIN / 'index.html').read_text()
for course in offers['courses']:
    folder = MAIN / course['folder'] if course['folder'] == 'value_at_risk' else ROOT / course['folder']
    page = (folder / 'index.html').read_text()
    url = f"https://www.udemy.com/course/{course['slug']}/?couponCode={offers['paid_code']}"
    assert url in homepage, f"Homepage misses {course['folder']}"
    assert url in page, f"Course page misses {course['folder']}"
    assert f'data-offer-deadline="{course["expires_at"]}"' in page
    assert re.search(r'data-copy-coupon="' + re.escape(offers['paid_code']) + r'"', page)
    assert '149.99' in page and '199.99' in page
    for path in folder.glob('*'):
        if path.is_file() and path.suffix in {'.html', '.js', '.md'}:
            text = path.read_text()
            assert not re.search(r'(IRDERIVS25|MBSABS25|FRTB25)_(SEP|OCT)_2026', text), path
    print(f"PASS {course['folder']}: {offers['paid_code']}, USD {offers['paid_price_usd']}, {course['expires_at']}")
print('All four offers match the verified metadata.')
