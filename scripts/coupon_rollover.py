#!/usr/bin/env python3
"""Preview and roll source coupon codes without reading private/generated files."""
from __future__ import annotations
import argparse
import difflib
import os
import re
from pathlib import Path

ALLOWED_EXTENSIONS = {'.css', '.csv', '.html', '.htm', '.js', '.json', '.jsx', '.md', '.php', '.py', '.sh', '.sql', '.toml', '.ts', '.tsx', '.txt', '.xml', '.yaml', '.yml'}
SKIP_DIRS = {'venv', '__pycache__', 'build', 'dist', 'node_modules', 'out', 'output', 'target', 'confidential', 'data', 'logs', 'sessions', 'recordings', 'secrets', 'credentials', 'keys', 'tokens'}
PRIVATE_NAME = re.compile(r'(?:secret|credential|private[_-]?key|(?:^|[_.-])(?:keys?|tokens?)(?:[_.-]|$))', re.I)
MONTH_YEAR = re.compile(r'(?:JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)_\d{4}')
LEGACY_PAID = r'(?:IRDERIVS25|MBSABS25|FRTB25|DEAL_TG|25OFF_TG)'

def normalize_token(raw):
    token = raw.strip().upper().lstrip('_')
    if not MONTH_YEAR.fullmatch(token):
        raise ValueError('expected a month/year such as OCT_2026')
    return token

def transform(text, old, new, paid_prefix=None):
    result = text.replace('_' + old, '_' + new)
    if paid_prefix:
        pattern = r'(?<![A-Z0-9_])' + LEGACY_PAID + '_' + re.escape(new) + r'(?![A-Z0-9_])'
        result = re.sub(pattern, paid_prefix + '_' + new, result)
    return result

def candidates(root):
    for dirpath, dirnames, filenames in os.walk(root):
        base = Path(dirpath)
        dirnames[:] = sorted(d for d in dirnames if not d.startswith('.') and d not in SKIP_DIRS and not (base/d).is_symlink())
        for name in sorted(filenames):
            path = base/name
            if name.startswith('.') or PRIVATE_NAME.search(name) or path.is_symlink() or path.suffix.lower() not in ALLOWED_EXTENSIONS:
                continue
            yield path

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('oldmonth_year')
    parser.add_argument('newmonth_year')
    parser.add_argument('--paid-prefix', help='normalize legacy TGIR paid codes, usually 25OFF_TG')
    parser.add_argument('--preview', action='store_true', help='show the full diff without applying')
    args = parser.parse_args()
    try:
        old, new = normalize_token(args.oldmonth_year), normalize_token(args.newmonth_year)
        prefix = args.paid_prefix.strip().upper() if args.paid_prefix else None
        if prefix and (not re.fullmatch(r'[A-Z0-9_-]+', prefix) or len(prefix+'_'+new) > 20):
            raise ValueError('paid coupon must use uppercase letters/digits/_/- and be at most 20 characters')
        root = Path(os.environ.get('COUPON_ROOT', os.getcwd())).resolve()
        if not root.is_dir():
            raise ValueError('COUPON_ROOT must be an existing directory')
        changes = []
        for path in candidates(root):
            try:
                before = path.read_text(encoding='utf-8')
            except UnicodeDecodeError:
                continue
            if '\x00' in before:
                continue
            after = transform(before, old, new, prefix)
            if before != after:
                changes.append((path, before, after))
        print(f'Target root: {root}\nChanged source files: {len(changes)}')
        if not changes:
            print('Already up to date. No files changed.')
            return 0
        for path, before, after in changes:
            rel = path.relative_to(root)
            print(''.join(difflib.unified_diff(before.splitlines(True), after.splitlines(True), fromfile='a/'+str(rel), tofile='b/'+str(rel))), end='')
        auto = os.environ.get('COUPON_AUTO_APPLY', '').strip().lower() in {'1', 'true', 'yes'}
        if args.preview or (not auto and not os.isatty(0)):
            print('Preview only. No files changed.')
            return 0
        if not auto and input('Apply these changes? [y/N]: ').strip().lower() not in {'y', 'yes'}:
            print('No files changed.')
            return 0
        # Detect edits made since preview before writing any file.
        for path, before, _ in changes:
            if path.read_text(encoding='utf-8') != before:
                raise ValueError(f'File changed after preview: {path}')
        for path, _, after in changes:
            path.write_text(after, encoding='utf-8')
        for path, _, after in changes:
            current = path.read_text(encoding='utf-8')
            if current != after or transform(current, old, new, prefix) != current:
                raise ValueError(f'Verification failed: {path}')
        print(f'Applied and verified {len(changes)} files.')
        return 0
    except (ValueError, OSError) as exc:
        parser.exit(2, f'Coupon rollover failed: {exc}\n')

if __name__ == '__main__':
    raise SystemExit(main())
