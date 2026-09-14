"""Build only the generic OpenAI plugin; never include private interview output."""
from pathlib import Path
import hashlib
import json
import zipfile
root=Path(__file__).resolve().parents[1]
plugin=root/'plugins/voice-foundation'
manifest=json.loads((plugin/'plugin.json').read_text())
out=root/'dist';out.mkdir(exist_ok=True)
target=out/f'voice-foundation-openai-v{manifest["version"]}.zip'
with zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED) as z:
    for f in sorted(plugin.rglob('*')):
        if f.is_symlink():raise ValueError('Do not package symlinks')
        if f.is_file() and '__pycache__' not in f.parts and f.suffix!='.pyc':
            z.write(f,f.relative_to(plugin.parent))
with zipfile.ZipFile(target) as z:
    assert z.testzip() is None
(root/'dist/SHA256SUMS.txt').write_text(hashlib.sha256(target.read_bytes()).hexdigest()+'  '+target.name+'\n')
print(target)
