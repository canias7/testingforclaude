// Made by Coder
function badge(text) {
  const safe = String(text)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
  return `<span class="badge badge-green badge-large" style="background:#16a34a;color:#fff;font-size:1.25rem;padding:0.5rem 1rem;border-radius:999px">${safe}</span>`;
}

function small(text) {
  const safe = String(text)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
  return `<span class="badge badge-green badge-small" style="background:#16a34a;color:#fff;font-size:0.75rem;padding:0.15rem 0.4rem;border-radius:999px">${safe}</span>`;
}

module.exports = { badge, small };
