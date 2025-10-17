export function route(name, params = [], query = {}) {
  if (!window.Urls || typeof window.Urls[name] !== 'function') {
    throw new Error(`Unknown route: ${name}`);
  }
  const path = Array.isArray(params)
    ? window.Urls[name](...params)
    : window.Urls[name](params);

  const qs = new URLSearchParams(query).toString();
  return qs ? `${path}?${qs}` : path;
}