export function getCsrf() {
    const meta = document.querySelector('meta[name="csrf-token"]');
    if (meta?.content && meta.content !== 'NOTPROVIDED') return meta.content;
    // fallback: cookie
    return document.cookie.split('; ')
        .find(r => r.startsWith('csrftoken='))?.split('=')[1];
}

const qs = (obj = {}) => {
    const s = new URLSearchParams(obj).toString();
    return s ? `?${s}` : '';
};

export function route(name, params = undefined, query = undefined, { absolute = false } = {}) {
    if (name === undefined) return route;

    if (!window.Urls) throw new Error('django-js-reverse not loaded.');

        console.log("name-->" + name, window.Urls);
        let path;
        if (params === undefined) {
            path = window.Urls[name]();
        } else if (Array.isArray(params)) {
            path = window.Urls[name](...params);
        } else {
            path = window.Urls[name](params);
        }

        const url = `${path}${qs(query)}`;
        return absolute ? new URL(url, window.location.origin).toString() : url;
}


route.abs = (name, p, q) => route(name, p, q, { absolute: true });

const normalize = (u) => {
  const { pathname } = new URL(u, window.location.origin);
  // strip trailing slash except root
  const clean = pathname.replace(/\/+$/, '');
  return clean === '' ? '/' : clean;
};

route.current = (names, params = undefined, { exact = true } = {}) => {
    const current = normalize(window.location.pathname);
    const list = Array.isArray(names) ? names : [names];

    return list.some((n) => {
        const target = normalize(route(n, params));
        if (exact) return current === target;
        // non-exact: treat "on this section" as current if current starts with target/
        const prefix = target.endsWith('/') ? target : `${target}/`;
        return current === target || current.startsWith(prefix);
    });
}