from pathlib import Path
import tempfile
import importlib.util
import json
import unittest
from test_delivery import b
from make_fixture import fixture
spec=importlib.util.spec_from_file_location('installer',Path(__file__).resolve().parents[1]/'voice-foundation/scripts/install_personal_skill.py')
i=importlib.util.module_from_spec(spec);spec.loader.exec_module(i)
class InstallTests(unittest.TestCase):
 def test_install_and_reviewed_update(self):
  with tempfile.TemporaryDirectory() as t:
   root=Path(t).resolve();d=fixture();a=b.build(d,root/'exports');target=i.install(a,root/'skills')
   self.assertEqual((target/'references/voice_foundation.md').read_text(),(a/'voice_foundation.md').read_text())
   self.assertEqual(json.loads((a/'delivery.json').read_text())['installation_status'],'installed_files_pending_discovery')
   d['revision']=2;new=b.build(d,root/'exports')
   with self.assertRaises(ValueError):i.install(new,root/'skills')
   self.assertEqual(target,i.install(new,root/'skills',update=True))
   self.assertEqual(len(list((root/'voice-foundation-skill-backups').iterdir())),1)
   self.assertEqual(len(list((root/'skills').iterdir())),1)
 def test_tamper_and_collision(self):
  with tempfile.TemporaryDirectory() as t:
   root=Path(t).resolve();a=b.build(fixture(),root/'exports');rec=json.loads((a/'delivery.json').read_text());sk=a/'personal-skill'/rec['skill_name']
   ref=sk/'references/voice_foundation.md';orig=ref.read_text();ref.write_text('changed')
   with self.assertRaises(ValueError):i.install(a,root/'skills')
   ref.write_text(orig);target=root/'skills'/rec['skill_name'];target.mkdir(parents=True);(target/'SKILL.md').write_text('unrelated skill')
   with self.assertRaises(ValueError):i.install(a,root/'skills',update=True)
   self.assertEqual((target/'SKILL.md').read_text(),'unrelated skill')
