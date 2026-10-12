import redirects from './routes.json' with { type: 'json' };

const hosts = new Set(['kidlogicloft.com', 'www.kidlogicloft.com']);

export function destination(pathname) {
  // Normalize only page spellings; asset paths retain their exact extension.
  let path = pathname.replace(/\/index\.html$/, '/');
  if (!path.endsWith('/') && !path.split('/').at(-1).includes('.')) path += '/';
  return Object.hasOwn(redirects, path) ? redirects[path] : null;
}

export default {
  fetch(request) {
    const url = new URL(request.url);
    if (!hosts.has(url.hostname)) return new Response('Unknown host', { status: 404 });
    const path = destination(url.pathname);
    if (!path) return new Response('Page not found. Visit https://appmonto.com/games/', { status: 404 });
    const target = new URL(path, 'https://appmonto.com');
    target.search = url.search;
    return Response.redirect(target.href, 301);
  }
};
