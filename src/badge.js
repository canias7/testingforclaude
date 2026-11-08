// Made by Coder
function badge(text) {
  const safe = String(text)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
  return `<span class="badge badge-green badge-large" style="background:#16a34a;color:#fff;font-size:1.25rem;padding:0.5rem 1rem;border-radius:999px">${safe}</span>`;
}

module.exports = { badge };
