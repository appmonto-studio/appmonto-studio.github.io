#!/usr/bin/env python3
"""Validate and export the static production site; no framework or npm install.

GitHub Pages still serves the committed root directly. dist/ is a clean local
production artifact for inspection or a future Pages artifact deployment.
"""
from pathlib import Path
import shutil
import subprocess
import sys
ROOT=Path(__file__).resolve().parents[1]
subprocess.run([sys.executable,str(ROOT/'tools/generate_site.py'),'--check'],check=True)
subprocess.run([sys.executable,str(ROOT/'tools/check_site.py')],check=True)
out=ROOT/'dist'
if out.exists(): shutil.rmtree(out)
out.mkdir()
for name in ['index.html','404.html','CNAME','.nojekyll','robots.txt','sitemap.xml','favicon.png','assets','apps','games','support','de','es','legal','privacy']:
    src=ROOT/name
    if src.is_dir(): shutil.copytree(src,out/name)
    else: shutil.copy2(src,out/name)
subprocess.run([sys.executable,str(ROOT/'tools/check_site.py'),str(out)],check=True)
print('Production export: dist/')
