import importlib.util
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).with_name('coupon_rollover.py')
spec = importlib.util.spec_from_file_location('rollover', SCRIPT)
rollover = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rollover)

class RolloverTests(unittest.TestCase):
    def test_shared_migration_keeps_free(self):
        for prefix in ('IRDERIVS25', 'MBSABS25', 'FRTB25', '25OFF_TG'):
            result = rollover.transform(prefix+'_OCT_2026 FREE_TG_OCT_2026', 'OCT_2026', 'NOV_2026', '25OFF_TG')
            self.assertEqual(result, '25OFF_TG_NOV_2026 FREE_TG_NOV_2026')

    def test_same_month_migration_and_idempotency(self):
        result = rollover.transform('FRTB25_OCT_2026', 'OCT_2026', 'OCT_2026', '25OFF_TG')
        self.assertEqual(result, '25OFF_TG_OCT_2026')
        self.assertEqual(rollover.transform(result, 'OCT_2026', 'OCT_2026', '25OFF_TG'), result)

    def test_preview_and_private_generated_exclusions(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            for name in ('index.html', '.env', 'credentials.json', 'tokens.json', 'keys.yml', 'secrets/notes.txt', 'output/recording.html', '.git/history.md', '.playwright-cli/page.yml', 'confidential/private.md'):
                path = root/name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text('FRTB25_OCT_2026')
            (root/'link.html').symlink_to(root/'index.html')
            env = dict(os.environ, COUPON_ROOT=folder, COUPON_AUTO_APPLY='1')
            preview = subprocess.run([sys.executable,str(SCRIPT),'OCT_2026','NOV_2026','--paid-prefix','25OFF_TG','--preview'],env=env,capture_output=True,text=True)
            self.assertEqual(preview.returncode, 0, preview.stderr)
            self.assertIn('--- a/index.html', preview.stdout)
            self.assertEqual((root/'index.html').read_text(), 'FRTB25_OCT_2026')
            apply = subprocess.run([sys.executable,str(SCRIPT),'OCT_2026','NOV_2026','--paid-prefix','25OFF_TG'],env=env,capture_output=True,text=True)
            self.assertEqual(apply.returncode, 0, apply.stderr)
            self.assertEqual((root/'index.html').read_text(), '25OFF_TG_NOV_2026')
            for name in ('credentials.json', 'tokens.json', 'keys.yml', 'secrets/notes.txt'):
                self.assertEqual((root/name).read_text(), 'FRTB25_OCT_2026')
            self.assertEqual((root/'output/recording.html').read_text(), 'FRTB25_OCT_2026')
            self.assertEqual((root/'.env').read_text(), 'FRTB25_OCT_2026')

    def test_invalid_month(self):
        with self.assertRaises(ValueError): rollover.normalize_token('XYZ_2026')

if __name__ == '__main__': unittest.main()
