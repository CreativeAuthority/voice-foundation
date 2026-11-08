"""Package the three self-contained generic skills; exclude private output."""
from pathlib import Path
import hashlib,json,zipfile
root=Path(__file__).resolve().parents[1]
plugin=root/'voice-foundation'
version=json.loads((plugin/'plugin.json').read_text())['version']
out=root/'dist';out.mkdir(exist_ok=True)
target=out/f'voice-foundation-chatgpt-v{version}.zip'
with zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED) as z:
    for top in ['skills','assets/logo.png','assets/icon.svg','.codex-plugin','plugin.json','LICENSE']:
        path=plugin/top
        files=sorted(path.rglob('*')) if path.is_dir() else [path]
        for f in files:
            if f.is_symlink(): raise ValueError('No symlinks in customer package')
            if f.is_file() and '__pycache__' not in f.parts and f.suffix != '.pyc' and f.name != '.DS_Store':
                z.write(f,Path('voice-foundation')/f.relative_to(plugin))
with zipfile.ZipFile(target) as z:
    assert z.testzip() is None
    for name in ['start-voice-foundation','update-voice-foundation']:
        base='voice-foundation/skills/'+name+'/'
        for file in ['scripts/build_foundation.py','scripts/install_personal_skill.py','assets/DejaVuSans.ttf','assets/DejaVuSans-Bold.ttf','assets/logo.png','references/drafting.md','references/delivery.md']:
            assert base+file in z.namelist(),base+file
(out/(target.name+'.sha256')).write_text(hashlib.sha256(target.read_bytes()).hexdigest()+'  '+target.name+'\n')
print(target)

# ChatGPT's single-skill uploader imports only one skill from a plugin ZIP.
# Provide separate, byte-identical skill contents for that installation path.
with zipfile.ZipFile(target) as source:
    for name in ['start-voice-foundation','write-with-voice-foundation','update-voice-foundation']:
        prefix='voice-foundation/skills/'+name+'/'
        single=out/f'{name}-v{version}.zip'
        with zipfile.ZipFile(single,'w',zipfile.ZIP_DEFLATED) as z:
            for member in source.namelist():
                if member.startswith(prefix):
                    z.writestr(name+'/'+member[len(prefix):],source.read(member))
        with zipfile.ZipFile(single) as z:
            assert z.testzip() is None
            assert name+'/SKILL.md' in z.namelist()
            for member in z.namelist():
                assert z.read(member)==source.read(prefix+member[len(name)+1:])
        (out/(single.name+'.sha256')).write_text(hashlib.sha256(single.read_bytes()).hexdigest()+'  '+single.name+'\n')
        print(single)
