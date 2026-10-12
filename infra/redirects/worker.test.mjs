import { test } from 'node:test';
import assert from 'node:assert/strict';
import { existsSync } from 'node:fs';
import worker, { destination } from './worker.mjs';
import routes from './routes.json' with { type: 'json' };

test('every legacy route reaches an existing final file in one permanent hop', () => {
  for (const [path, target] of Object.entries(routes)) {
    assert.ok(existsSync(new URL('../../' + target.slice(1) + (target.endsWith('/') ? 'index.html' : ''), import.meta.url)), target);
    for (const host of ['kidlogicloft.com', 'www.kidlogicloft.com']) {
      for (const protocol of ['http', 'https']) {
        const response = worker.fetch(new Request(`${protocol}://${host}${path}?ref=store`));
        assert.equal(response.status, 301);
        assert.equal(response.headers.get('location'), `https://appmonto.com${target}?ref=store`);
      }
    }
    if (path.endsWith('/')) {
      assert.equal(destination(path+'index.html'),target);
      assert.equal(destination(path.slice(0,-1)), target);
    }
  }
});
test('privacy stays distinct from website privacy and preserves locale', () => {
  for (const prefix of ['', '/de', '/es']) {
    assert.equal(destination(prefix+'/privacy/'),prefix+'/games/privacy/');
    assert.equal(destination(prefix+'/apps/cozy-meadow-farm/'),prefix+'/apps/closer-look-farm/');
  }
});
test('unknown paths and destination host cannot loop or redirect externally', () => {
  for (const url of ['https://appmonto.com/privacy/', 'https://kidlogicloft.com/missing', 'https://kidlogicloft.com//evil.example/', 'https://kidlogicloft.com/__proto__']) {
    assert.equal(worker.fetch(new Request(url)).status,404);
  }
});
