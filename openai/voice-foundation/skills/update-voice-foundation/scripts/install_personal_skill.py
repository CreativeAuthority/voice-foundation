#!/usr/bin/env python3
"""Install a generated private skill in a confirmed local host skill directory."""
from pathlib import Path
import argparse
import hashlib
import json
import re
import shutil
import tempfile

def install(delivery, skills_dir, update=False):
    delivery=Path(delivery).resolve();skills_dir=Path(skills_dir).expanduser().absolute()
    record=json.loads((delivery/'delivery.json').read_text())
    name=record['skill_name'];agent_id=record['agent_id']
    if not re.fullmatch(r'write-in-my-voice-[a-z0-9-]{1,46}',name):raise ValueError('Invalid generated skill name')
    source=delivery/'personal-skill'/name
    if source.is_symlink() or any(p.is_symlink() for p in source.rglob('*')):raise ValueError('Symlink source is not supported')
    ref=(source/'references/voice_foundation.md').read_bytes()
    if hashlib.sha256(ref).hexdigest()!=record['foundation_sha256']:raise ValueError('Source foundation changed since export; rebuild the revision')
    for parent in [skills_dir,*skills_dir.parents]:
        if parent.is_symlink():raise ValueError('Use the real host skill directory, not a symlink')
    skills_dir.mkdir(parents=True,exist_ok=True)
    target=skills_dir/name;backup=None
    if target.exists():
        if target.is_symlink():raise ValueError('Refusing to replace a symlink')
        old=target/'references/voice_foundation.md'
        if not old.exists() or f'Agent ID: {agent_id} |' not in old.read_text():raise ValueError('Existing skill belongs to an unknown/different agent')
        if old.read_bytes()==ref:return target
        if not update:raise ValueError('Existing revision differs; use --update only for a reviewed revision')
        match=re.search(r'Agent ID: '+re.escape(agent_id)+r' \| Revision: (\d+)',old.read_text())
        if not match or int(match[1])>=record['revision']:raise ValueError('Update must advance the reviewed revision')
        # Backups live outside skill discovery so duplicate skills do not appear.
        backups=skills_dir.parent/'voice-foundation-skill-backups';backups.mkdir(exist_ok=True)
        backup=backups/(name+'-r'+match[1])
        if backup.exists():raise ValueError('Backup already exists; inspect before replacing the skill')
    stage=Path(tempfile.mkdtemp(prefix='.vf-install-',dir=skills_dir.parent))
    staged=stage/name
    try:
        shutil.copytree(source,staged)
        if backup:target.rename(backup)
        try:staged.rename(target)
        except BaseException:
            if backup and not target.exists():backup.rename(target)
            raise
    finally:shutil.rmtree(stage)
    record['installation_status']='installed_files_pending_discovery'
    record['installation_path']=str(target)
    record['installation_evidence']='Files copied and foundation hash verified; host menu discovery still required.'
    (delivery/'delivery.json').write_text(json.dumps(record,indent=2)+'\n')
    return target

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('delivery',type=Path);p.add_argument('--skills-dir',required=True,type=Path)
    p.add_argument('--update',action='store_true');a=p.parse_args()
    try:print(install(a.delivery,a.skills_dir,a.update))
    except (ValueError,KeyError) as e:p.exit(2,f'Skill not installed: {e}\n')
