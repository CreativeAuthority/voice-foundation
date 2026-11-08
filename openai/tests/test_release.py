import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
import zipfile
from unittest.mock import patch
from test_delivery import b, ROOT
from make_fixture import fixture

class ReleaseTests(unittest.TestCase):
 def test_pdf_failure_keeps_complete_delivery(self):
  with tempfile.TemporaryDirectory() as t:
   d=fixture();d['identity']['name']='<script>alert(1)</script>'
   with patch.object(b,'pdf',side_effect=ImportError('missing optional engine')):
    out=b.build(d,t)
   html=(out/'Voice_Foundation.html').read_text()
   self.assertNotIn('<script>alert(1)</script>',html)
   self.assertIn('&lt;script&gt;',html)
   self.assertIn('@media print',html);self.assertIn('.print-banner{display:none!important}',html)
   self.assertIn('data:image/png;base64,',html)
   self.assertFalse((out/'Voice_Foundation.pdf').exists())
   self.assertTrue((out/'my-writing-skill.zip').exists())
   self.assertIn(d['written']['anchor']['text'],(out/'voice_foundation.md').read_text())
   self.assertEqual('html',json.loads((out/'delivery.json').read_text())['document_format'])
 def test_correction_must_retain_link_to_previous_evidence(self):
  d=fixture();d['evidence'].append(dict(id='change',kind='correction',text='Changed preference',source='test',confirmed=True))
  with self.assertRaises(b.FoundationError):b.validate(d)
  d['evidence'][-1]['supersedes']='patterns';b.validate(d)
 def test_uploaded_skills_work_without_plugin_parent(self):
  version=json.loads((ROOT/'voice-foundation/plugin.json').read_text())['version']
  archive=ROOT/f'dist/voice-foundation-chatgpt-v{version}.zip'
  with tempfile.TemporaryDirectory() as t,zipfile.ZipFile(archive) as z:
   root=Path(t)
   for name in ['start-voice-foundation','update-voice-foundation']:
    prefix='voice-foundation/skills/'+name+'/'
    target=root/name
    for entry in z.namelist():
     if entry.startswith(prefix):
      f=target/entry[len(prefix):];f.parent.mkdir(parents=True,exist_ok=True);f.write_bytes(z.read(entry))
    spec=importlib.util.spec_from_file_location(name,target/'scripts/build_foundation.py');module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    out=module.build(fixture(),root/(name+'-out'))
    self.assertTrue((out/'Voice_Foundation.pdf').exists())
    with zipfile.ZipFile(out/'my-writing-skill.zip') as personal:
     self.assertTrue(any(n.endswith('/references/drafting.md') for n in personal.namelist()))
     self.assertTrue(any(n.endswith('/references/foundation.json') for n in personal.namelist()))
