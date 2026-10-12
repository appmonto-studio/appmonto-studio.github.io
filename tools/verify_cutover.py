#!/usr/bin/env python3
"""Read-only production verification. Run ONLY after the owner performs cutover."""
import concurrent.futures
import json
from pathlib import Path
import urllib.request
import urllib.error

ROOT=Path(__file__).resolve().parents[1]
MAP=json.loads((ROOT/'infra/redirects/routes.json').read_text())
class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,req,fp,code,msg,headers,newurl):
        return None

def check(case):
    old,target=case
    try:
        urllib.request.build_opener(NoRedirect).open(old,timeout=20)
        return f'FAIL {old}: no redirect'
    except urllib.error.HTTPError as error:
        if error.code!=301 or error.headers.get('Location')!=target:
            return f'FAIL {old}: {error.code} {error.headers.get("Location")}'
    except Exception as error:
        return f'FAIL {old}: {error}'
    return None

cases=[]
for host in ['kidlogicloft.com','www.kidlogicloft.com']:
    for scheme in ['http','https']:
        for old,target in MAP.items():
            spellings=[old]
            if old.endswith('/'):
                spellings += [old+'index.html']
                if old!='/': spellings += [old.rstrip('/')]
            for spelling in spellings:
                cases.append((f'{scheme}://{host}{spelling}?ref=cutover',f'https://appmonto.com{target}?ref=cutover'))
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    errors=[x for x in pool.map(check,cases) if x]
for target in sorted(set(MAP.values())):
    try:
        with urllib.request.urlopen('https://appmonto.com'+target,timeout=20) as response:
            assert response.status==200 and response.url=='https://appmonto.com'+target
    except Exception as error: errors.append(f'FAIL destination {target}: {error}')
print('\n'.join(errors) if errors else f'PASS: {len(cases)} direct 301 checks and all final targets.')
raise SystemExit(bool(errors))
