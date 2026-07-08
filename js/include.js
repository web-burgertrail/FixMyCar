/* Includes shared header/footer partials on every page.
   Works on Vercel static hosting via same-origin fetch. */
(function () {
  async function include(selector, url) {
    const el = document.querySelector(selector);
    if (!el) return;
    try {
      const res = await fetch(url);
      const html = await res.text();
      el.innerHTML = html;
    } catch (e) {
      console.error("Include failed:", url, e);
    }
  }

  // depth = how many folders deep the current page is from root (0 = root)
  const depth = Number(document.documentElement.getAttribute("data-depth") || 0);
  const root = depth > 0 ? "../".repeat(depth) : "./";

  window.addEventListener("DOMContentLoaded", async () => {
    await Promise.all([
      include("#site-header", root + "partials/header.html"),
      include("#site-footer", root + "partials/footer.html"),
    ]);
    // Fix root-relative "/xxx" links to work when hosted in a subpath / locally
    document.querySelectorAll('a[href^="/"]').forEach((a) => {
      const href = a.getAttribute("href");
      if (href.startsWith("//")) return;
      a.setAttribute("href", root + href.slice(1));
    });
    if (window.initNav) window.initNav();
  });
})();
