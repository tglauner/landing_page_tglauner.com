#!/usr/bin/env bash
# Install local adapters without replacing any real skill directory with a link.
set -euo pipefail
site_root="$(cd "$(dirname "$0")/.." && pwd)"
shared_root="$(cd "$site_root/../../cross_project_tools" && pwd)"
for skill in coupon-rollover tgir-visitor-analytics; do
    test -f "$shared_root/skills/$skill/SKILL.md"
done
bash "$shared_root/scripts/link_skills.sh"
TGIR_SITE_ROOT="$site_root" TGIR_SHARED_ROOT="$shared_root" python3 - <<'PY'
import os
from pathlib import Path

site = Path(os.environ['TGIR_SITE_ROOT'])
shared = Path(os.environ['TGIR_SHARED_ROOT'])
installed = Path.home() / '.codex/skills'
for name in ('coupon-rollover', 'tgir-visitor-analytics'):
    canonical = shared / 'skills' / name / 'SKILL.md'
    frontmatter = canonical.read_text().split('---', 2)[1]
    folder = installed / name
    folder.mkdir(parents=True, exist_ok=True)
    # Existing real folders remain in place. Only their entry instructions change.
    (folder / 'SKILL.md').write_text(
        '---' + frontmatter + '---\n\n'
        '# Canonical skill\n\n'
        f'Read and follow the complete canonical instructions at [{name} SKILL.md](<{canonical}>). '
        'That version-controlled file is the source of truth.\n'
    )
scripts = installed / 'coupon-rollover/scripts'
scripts.mkdir(parents=True, exist_ok=True)
for name in ('coupon_rollover.py', 'test_coupon_rollover.py'):
    source = site / 'scripts' / name
    (scripts / name).write_text(
        '#!/usr/bin/env python3\n'
        'import runpy\n'
        f'source = {str(source)!r}\n'
        'if __name__ == "__main__":\n'
        '    runpy.run_path(source, run_name="__main__")\n'
        'else:\n'
        '    globals().update(runpy.run_path(source))\n'
    )
command = Path.home() / '.local/bin/coupon-rollover'
command.parent.mkdir(parents=True, exist_ok=True)
command.write_text(
    '#!/usr/bin/env bash\nset -euo pipefail\n'
    'exec python3 "$HOME/.codex/skills/coupon-rollover/scripts/coupon_rollover.py" "$@"\n'
)
command.chmod(0o755)
print('Installed canonical skill adapters and the coupon-rollover command.')
PY
bash "$shared_root/scripts/link_skills.sh" --check
