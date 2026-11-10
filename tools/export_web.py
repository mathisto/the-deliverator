"""Export a self-contained, revision-stamped Deliverator web runtime to a consumer."""
from pathlib import Path
import argparse
import hashlib
import json
import shutil
import subprocess

ROOT=Path(__file__).resolve().parents[1]
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True);args=parser.parse_args()
    target=args.output.resolve();target.mkdir(parents=True,exist_ok=True)
    files=['dist/deliverator.js','dist/icons.svg','dist/PHOSPHOR-LICENSE.txt','palette/signal.css','palette/signal.json','ui/tokens.css','ui/fonts.css','ui/controls.css','ui/motion.css','ui/code.css','ui/application.css','ui/application.js']
    files += [str(p.relative_to(ROOT)).replace('\\','/') for p in (ROOT/'assets/fonts').iterdir() if p.is_file()]
    manifest={}
    for name in files:
        source=ROOT/name;dest=target/name;dest.parent.mkdir(parents=True,exist_ok=True);data=source.read_bytes()
        if source.suffix in {'.css','.js','.svg','.json','.md','.txt'}:data=data.replace(b'\r\n',b'\n')
        dest.write_bytes(data)
        manifest[name]=hashlib.sha256(dest.read_bytes()).hexdigest()
    imports=['palette/signal.css','ui/tokens.css','ui/fonts.css','ui/controls.css','ui/code.css']
    css=''.join('@import "./'+name+'?v='+manifest[name][:12]+'";\n' for name in imports)
    (target/'deliverator.css').write_bytes(css.encode('utf-8'))
    manifest['deliverator.css']=hashlib.sha256((target/'deliverator.css').read_bytes()).hexdigest()
    revision=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()
    (target/'manifest.json').write_bytes((json.dumps({'library':'mathisto/the-deliverator','revision':revision,'files':manifest},indent=2)+'\n').encode('utf-8'))
    print(f'Exported {len(manifest)} files to {target}')
