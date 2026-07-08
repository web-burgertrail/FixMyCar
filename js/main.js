// Nav interactions — re-initialized after header partial loads
window.initNav = function () {
  const navToggle = document.getElementById("navToggle");
  const navMenu = document.getElementById("navMenu");

  if (navToggle && navMenu) {
    navToggle.addEventListener("click", () => {
      const isOpen = navMenu.classList.toggle("is-active");
      navToggle.setAttribute("aria-expanded", isOpen);
      document.body.style.overflow = isOpen ? "hidden" : "";
    });
  }

  document.querySelectorAll(".has-dropdown > button").forEach((btn) => {
    btn.addEventListener("click", (e) => {
      e.preventDefault();
      const li = btn.parentElement;
      const isMobile = window.innerWidth <= 980;
      const wasOpen = li.classList.contains("is-open");

      document.querySelectorAll(".has-dropdown").forEach((el) => {
        if (!isMobile || el !== li) el.classList.remove("is-open");
      });
      li.classList.toggle("is-open", !wasOpen);
      btn.setAttribute("aria-expanded", !wasOpen);
    });
  });

  // Close dropdowns when clicking outside (desktop)
  document.addEventListener("click", (e) => {
    if (!e.target.closest(".has-dropdown")) {
      document.querySelectorAll(".has-dropdown").forEach((el) => el.classList.remove("is-open"));
    }
  });

  // Desktop hover support
  if (window.innerWidth > 980) {
    document.querySelectorAll(".has-dropdown").forEach((li) => {
      li.addEventListener("mouseenter", () => li.classList.add("is-open"));
      li.addEventListener("mouseleave", () => li.classList.remove("is-open"));
    });
  }
};

// Simple contact/booking form handler (static demo — replace action with real endpoint)
document.addEventListener("submit", function (e) {
  if (e.target.matches("[data-demo-form]")) {
    e.preventDefault();
    const btn = e.target.querySelector('button[type="submit"]');
    const original = btn.textContent;
    btn.textContent = "Dispatching...";
    btn.disabled = true;
    setTimeout(() => {
      btn.textContent = "Request Sent ✓";
      setTimeout(() => {
        btn.textContent = original;
        btn.disabled = false;
        e.target.reset();
      }, 2000);
    }, 900);
  }
});
