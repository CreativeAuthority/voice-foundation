import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
import zipfile
from pypdf import PdfReader
from make_fixture import fixture

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('builder',ROOT/'voice-foundation/scripts/build_foundation.py')
b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)

class DeliveryTests(unittest.TestCase):
    def test_outputs_agree_and_are_private(self):
        with tempfile.TemporaryDirectory() as t:
            d=fixture();out=b.build(d,t);md=(out/'voice_foundation.md').read_text()
            self.assertIn(md,(out/'operating-instructions.txt').read_text())
            self.assertEqual(md,next((out/'personal-skill').glob('*/references/voice_foundation.md')).read_text())
            record=json.loads((out/'delivery.json').read_text())
            self.assertEqual(record['installation_status'],'created_not_installed')
            pdf='\n'.join(p.extract_text() for p in PdfReader(out/'Voice_Foundation.pdf').pages)
            for heading in ['Mission','Decision Rules','Written Voice','Spoken Voice','Portable operating instructions']:
                self.assertIn(heading,pdf)
            for channel in ('written','spoken'):
                self.assertIn(d[channel]['anchor']['text'],md)
                self.assertIn(' '.join(d[channel]['anchor']['text'].split()),' '.join(pdf.split()))
            for archive in ('my-writing-skill.zip','my-voice-plugin.zip'):
                with zipfile.ZipFile(out/archive) as z:
                    self.assertIsNone(z.testzip());self.assertTrue(any(n.endswith('SKILL.md') for n in z.namelist()))
                    self.assertFalse(any(n.startswith('/') or '..' in Path(n).parts for n in z.namelist()))
    def test_rejects_unreviewed_and_missing_evidence(self):
        mutations=[lambda d:d['review'].update(final_confirmed=False),lambda d:d['review'].update(open_gaps=['spoken sample']),lambda d:d['review'].update(confirmation_quote='fabricated approval'),lambda d:d['written']['anchor'].update(text='AI invented sample'),lambda d:d['written']['anchor'].update(evidence_id='s'),lambda d:d['spoken'].update(failure_signature=[]),lambda d:d['decision_rules'][0].update(evidence_ids=['missing']),lambda d:d['decision_rules'][0].update(evidence_ids=['price']),lambda d:d['evidence'][0].update(confirmed=False),lambda d:d.update(agent_id='../../escape')]
        for change in mutations:
            d=fixture();change(d)
            with self.subTest(change=change):
                with self.assertRaises(b.FoundationError):b.validate(d)
    def test_version_collision_preserves_original(self):
        with tempfile.TemporaryDirectory() as t:
            d=fixture();out=b.build(d,t);original=(out/'Voice_Foundation.pdf').read_bytes()
            with self.assertRaises(b.FoundationError):b.build(d,t)
            self.assertEqual(original,(out/'Voice_Foundation.pdf').read_bytes())
            d['revision']=2;new=b.build(d,t)
            self.assertNotEqual(out,new)
            self.assertEqual(json.loads((new/'delivery.json').read_text())['skill_name'],json.loads((out/'delivery.json').read_text())['skill_name'])
    def test_pdf_handles_long_and_markup_like_agent_text(self):
        with tempfile.TemporaryDirectory() as t:
            d=fixture();d['identity']['name']='Avery <Example> & Team';d['mission'][0]+=' Context and a concrete next step.'*120
            out=b.build(d,t)
            pdf=' '.join(p.extract_text() for p in PdfReader(out/'Voice_Foundation.pdf').pages)
            self.assertIn('Avery <Example> & Team',pdf)
    def test_no_public_personal_data(self):
        public=ROOT/'voice-foundation'
        for p in public.rglob('*'):
            if p.suffix in ('.md','.json','.py','.yaml'):
                s=p.read_text()
                self.assertNotIn('18bda2ac-f404-43a7-bf2b-671323c2ac55',s)
                self.assertNotIn('/Users/mattgoldman',s)
if __name__=='__main__':unittest.main(verbosity=2)
