#!/usr/bin/env python3
"""Read-only crawl of the four course sites, homepage, links, and assets."""
import argparse
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import time
from urllib.error import HTTPError, URLError
from urllib.parse import quote, unquote, urldefrag, urljoin, urlsplit, urlunsplit
from urllib.request import Request, urlopen

COURSES = ('mastering_interest_rate_derivatives', 'mastering_mbs_and_abs', 'frtb_fundamentals', 'value_at_risk')

class Document(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.links, self.assets, self.ids = [], [], set()
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get('id'): self.ids.add(attrs['id'])
        if tag == 'a' and attrs.get('name'): self.ids.add(attrs['name'])
        if tag == 'a' and attrs.get('href'):
            self.links.append({'href': attrs['href'], 'control': attrs.get('id') == 'cookie-preferences-link' or bool(attrs.get('onclick'))})
        if tag in ('img', 'script', 'iframe', 'source') and attrs.get('src'):
            self.assets.append(attrs['src'])
        if tag == 'link' and attrs.get('href') and any(r in attrs.get('rel', '').split() for r in ('stylesheet', 'icon')):
            self.assets.append(attrs['href'])

def safe_url(url):
    parsed = urlsplit(url)
    return urlunsplit((parsed.scheme, parsed.netloc, quote(parsed.path, safe='/%:@+~-._()'), parsed.query, ''))

def fetch(url, method='GET'):
    request = Request(safe_url(url), method=method, headers={'User-Agent': 'TGIR production link verification', 'Accept': 'text/html,application/json,text/event-stream,*/*;q=0.8'})
    started = time.monotonic()
    try:
        with urlopen(request, timeout=15) as response:
            content_type = response.headers.get('Content-Type', '')
            body = response.read(2_000_000) if method == 'GET' and ('text/html' in content_type or 'text/css' in content_type) else b''
            return {'url': url, 'status': response.status, 'final_url': response.url, 'content_type': content_type, 'seconds': round(time.monotonic() - started, 2), 'body': body.decode('utf-8', errors='replace')}
    except HTTPError as error:
        return {'url': url, 'status': error.code, 'final_url': error.url, 'content_type': error.headers.get('Content-Type', ''), 'body': ''}
    except (URLError, TimeoutError, OSError) as error:
        return {'url': url, 'status': None, 'error': str(error), 'body': ''}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base', default='https://tglauner.com/')
    parser.add_argument('--report', type=Path, required=True)
    args = parser.parse_args()
    base = args.base.rstrip('/') + '/'
    origin = urlsplit(base).netloc

    def normalize(href, page):
        url = urljoin(page, href)
        parsed = urlsplit(url)
        if parsed.netloc in ('tglauner.com', 'www.tglauner.com'):
            url = urlunsplit((urlsplit(base).scheme, origin, parsed.path, parsed.query, parsed.fragment))
        return url

    def is_page(url):
        parsed = urlsplit(url)
        path = parsed.path
        return parsed.netloc == origin and (path in ('/', '/index.html', '/golden_selling.html', '/alternative-site/', '/alternative-site/index.html') or any(path.startswith('/'+c+'/') and (path.endswith('/') or path.endswith('.html')) for c in COURSES))

    queue = [base] + [urljoin(base, course+'/') for course in COURSES]
    queue += [urljoin(base, p) for p in ('alternative-site/', 'golden_selling.html')]
    queue += [urljoin(base, course+'/'+name) for course in COURSES[:3] for name in ('footer.html', 'pre-checkout.html')]
    pages, references, protocols = {}, {}, []

    def reference(url, page, kind):
        parsed = urlsplit(url)
        if parsed.scheme not in ('http', 'https'):
            if parsed.scheme in ('mailto', 'tel'):
                protocols.append({'url': url, 'page': page, 'valid': bool(parsed.path)})
            return
        target, fragment = urldefrag(url)
        references.setdefault(target, []).append({'page': page, 'kind': kind, 'fragment': unquote(fragment)})
        if is_page(target) and target not in pages and target not in queue:
            queue.append(target)

    while queue:
        url = queue.pop(0)
        if url in pages: continue
        result = fetch(url)
        pages[url] = result
        print(f"PAGE {result['status']} {url}", flush=True)
        if result['status'] != 200: continue
        doc = Document(result['body'])
        result['ids'] = sorted(doc.ids)
        for link in doc.links:
            if link['control'] and link['href'].startswith('#'): continue
            reference(normalize(link['href'], url), url, 'link')
        for asset in doc.assets:
            reference(normalize(asset, url), url, 'asset')

    pending = [url for url in references if url not in pages]
    def check(url):
        result = fetch(url, 'HEAD')
        if result['status'] in (400, 403, 404, 405): result = fetch(url)
        return url, result
    checked = dict(pages)
    with ThreadPoolExecutor(max_workers=6) as pool:
        for url, result in pool.map(check, pending):
            checked[url] = result
    # CSS often references fonts or images that do not appear in HTML.
    css_urls = [url for url in references if urlsplit(url).path.endswith('.css')]
    extra = []
    for url in css_urls:
        result = fetch(url)
        if result['status'] == 200:
            for value in re.findall(r'url\(\s*[\'"]?([^\)\'"\s]+)', result['body']):
                target = normalize(value, url)
                if urlsplit(target).scheme in ('http', 'https'):
                    reference(target, url, 'css_asset')
                    if target not in checked and target not in extra: extra.append(target)
    with ThreadPoolExecutor(max_workers=6) as pool:
        for url, result in pool.map(check, extra): checked[url] = result

    broken, blocked, protected, api = [], [], [], []
    for url, result in checked.items():
        status = result['status']
        if status and 200 <= status < 400: continue
        if status == 401:
            protected.append(url)
        elif urlsplit(url).path == '/mcp' and status in (400, 405, 406):
            api.append({'url': url, 'status': status})
        elif status in (403, 429) and urlsplit(url).netloc != origin:
            blocked.append({'url': url, 'status': status})
        else:
            broken.append({'url': url, 'status': status, 'error': result.get('error'), 'references': references.get(url, [])})
    for url, refs in references.items():
        if url not in pages or pages[url]['status'] != 200: continue
        for ref in refs:
            if ref['fragment'] and ref['fragment'] not in pages[url].get('ids', []):
                broken.append({'url': url+'#'+ref['fragment'], 'issue': 'missing fragment', 'page': ref['page']})
    for item in protocols:
        if not item['valid']: broken.append(item)
    clean_results = {url: {key: value for key, value in result.items() if key not in ('body', 'ids')} for url, result in checked.items()}
    summary = {'pages': len(pages), 'unique_http_targets': len(checked), 'broken': len(broken), 'external_browser_checks_required': len(blocked), 'protected': len(protected), 'api_endpoints': len(api), 'email_or_phone_links': len(protocols)}
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps({'summary': summary, 'broken': broken, 'external_browser_checks_required': blocked, 'protected': protected, 'api_endpoints': api, 'results': clean_results}, indent=2)+'\n')
    print(json.dumps(summary, indent=2), flush=True)
    return 1 if broken else 0

if __name__ == '__main__': raise SystemExit(main())
