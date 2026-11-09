"""Offline preflight of the exact distribution ZIP; not an OpenAI scan."""
from pathlib import Path, PurePosixPath
import ast, hashlib, json, re, stat, unicodedata, zipfile
from xml.etree import ElementTree
root=Path(__file__).resolve().parents[1]
version=json.loads((root/'voice-foundation/plugin.json').read_text())['version']
archive=root/'dist'/f'voice-foundation-chatgpt-v{version}.zip'
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    items=z.infolist(); names=z.namelist(); prefix='voice-foundation/'
    assert archive.stat().st_size <= 25*1024*1024
    assert len(items)<=5000 and sum(i.file_size for i in items)<=512*1024*1024
    normalized=set()
    for i in items:
        name=i.filename; path=PurePosixPath(name)
        assert name.startswith(prefix) and not path.is_absolute() and '..' not in path.parts and '\\' not in name
        assert not stat.S_ISLNK(i.external_attr>>16) and not (i.flag_bits & 1)
        key=unicodedata.normalize('NFC',name).casefold(); assert key not in normalized; normalized.add(key)
        assert not any(s in path.parts for s in ('output','tests','__pycache__','.git','personal-skill','personal-plugin'))
        assert path.name not in ('foundation.json','.env','.DS_Store')
        if path.suffix in ('.md','.json','.py','.yaml','.txt'):
            text=z.read(name).decode()
            assert '/Users/' not in text and '/private/tmp' not in text
            assert not re.search(r'GOCSPX-|sk-(?:proj-|ant-)|-----BEGIN (?:RSA |EC )?PRIVATE KEY-----',text)
        if path.suffix=='.py':
            tree=ast.parse(z.read(name))
            imports={n.names[0].name.split('.')[0] for n in ast.walk(tree) if isinstance(n,ast.Import)}
            imports|={n.module.split('.')[0] for n in ast.walk(tree) if isinstance(n,ast.ImportFrom) and n.module}
            assert not imports & {'requests','urllib','socket','http','subprocess'},(name,imports)
    portable=json.loads(z.read(prefix+'plugin.json'))
    codex=json.loads(z.read(prefix+'.codex-plugin/plugin.json'))
    interface=codex['interface'];assert portable['extensions']['com.openai']['interface']==interface
    assert codex['version']==portable['version']==version
    for field,limit in [('displayName',30),('shortDescription',30),('longDescription',4000),('developerName',80)]:
        assert 0<len(interface[field])<=limit,field
    assert len(interface['defaultPrompt'])<=3 and len(set(interface['defaultPrompt']))==len(interface['defaultPrompt'])
    assert all(len(p)<=128 and '@' not in p for p in interface['defaultPrompt'])
    for field in ('logo','composerIcon'):
        image=prefix+interface[field].removeprefix('./'); assert image in names
        if image.endswith('.svg'):
            svg=ElementTree.fromstring(z.read(image));assert int(svg.attrib['width'])==int(svg.attrib['height'])>=48
    skills=sorted(n for n in names if n.endswith('/SKILL.md'))
    assert len(skills)==3
    for skill in skills:
        skillroot=PurePosixPath(skill).parent
        text=z.read(skill).decode();assert text.startswith('---\n')
        assert re.search(r'^name: [a-z0-9-]+$',text,re.M) and '\ndescription:' in text
        for n in names:
            if n.startswith(str(skillroot)+'/') and n.endswith('.md'):
                for link in re.findall(r'\]\(([^)]+)\)',z.read(n).decode()):
                    if link.startswith(('https:','http:','#','mailto:')):continue
                    parts=list(PurePosixPath(n).parent.parts)
                    for part in link.split('#')[0].split('/'):
                        if part=='..':parts.pop()
                        elif part not in ('','.'):parts.append(part)
                    target='/'.join(parts)
                    assert target.startswith(str(skillroot)+'/') and target in names,(n,link)
    for name in ('start-voice-foundation','update-voice-foundation'):
        base=prefix+'skills/'+name+'/'
        for file in ('build_foundation.py','install_personal_skill.py'):
            assert z.read(base+'scripts/'+file)==(root/'voice-foundation/scripts'/file).read_bytes()
        assert base+'assets/FONT-LICENSE.txt' in names
report={'version':version,'archive':archive.name,'sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),'compressed_bytes':archive.stat().st_size,'files':len(items),'skills':skills,'result':'PASS','scope':'Offline package checks only; OpenAI automated scans and live import are separate.'}
if (root/'submission').is_dir():(root/'submission/PACKAGE-CHECK.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
