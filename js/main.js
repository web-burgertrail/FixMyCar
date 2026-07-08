// Nav interactions — re-initialized after header partial loads
window.initNav = function () {
  const navToggle = document.getElementById("navToggle");
  const navMenu = document.getElementById("navMenu");
  const CLOSE_DELAY = 180; // ms — grace period before a dropdown closes

  if (navToggle && navMenu) {
    navToggle.addEventListener("click", () => {
      const isOpen = navMenu.classList.toggle("is-active");
      navToggle.setAttribute("aria-expanded", isOpen);
      document.body.style.overflow = isOpen ? "hidden" : "";
      if (!isOpen) closeAllDropdowns();
    });
  }

  function isMobile() {
    return window.innerWidth <= 980;
  }

  function openDropdown(li, btn) {
    document.querySelectorAll(".has-dropdown").forEach((el) => {
      if (el !== li) closeDropdown(el);
    });
    clearTimeout(li._closeTimer);
    li.classList.add("is-open");
    if (btn) btn.setAttribute("aria-expanded", "true");
  }

  function closeDropdown(li) {
    li.classList.remove("is-open");
    const btn = li.querySelector(":scope > button");
    if (btn) btn.setAttribute("aria-expanded", "false");
  }

  function scheduleClose(li) {
    clearTimeout(li._closeTimer);
    li._closeTimer = setTimeout(() => closeDropdown(li), CLOSE_DELAY);
  }

  function closeAllDropdowns() {
    document.querySelectorAll(".has-dropdown").forEach((el) => {
      clearTimeout(el._closeTimer);
      closeDropdown(el);
    });
  }

  document.querySelectorAll(".has-dropdown").forEach((li) => {
    const btn = li.querySelector(":scope > button");
    const panel = li.querySelector(":scope > .dropdown");
    if (!btn) return;

    // Click / tap — works on both mobile and desktop, and is keyboard-triggerable.
    btn.addEventListener("click", (e) => {
      e.preventDefault();
      const wasOpen = li.classList.contains("is-open");
      if (wasOpen) {
        closeDropdown(li);
      } else {
        openDropdown(li, btn);
      }
    });

    if (!isMobile()) {
      // Hover support with a short close delay so moving the cursor from the
      // trigger into the panel (or briefly off it) doesn't collapse the menu.
      li.addEventListener("mouseenter", () => openDropdown(li, btn));
      li.addEventListener("mouseleave", () => scheduleClose(li));
      if (panel) {
        panel.addEventListener("mouseenter", () => clearTimeout(li._closeTimer));
        panel.addEventListener("mouseleave", () => scheduleClose(li));
      }
    }

    // Keyboard: close on Escape, return focus to the trigger.
    li.addEventListener("keydown", (e) => {
      if (e.key === "Escape") {
        closeDropdown(li);
        btn.focus();
      }
    });
  });

  // Close dropdowns when clicking/tapping outside
  document.addEventListener("click", (e) => {
    if (!e.target.closest(".has-dropdown")) closeAllDropdowns();
  });

  // Close dropdowns when focus moves entirely outside the nav (keyboard users)
  document.addEventListener(
    "focusout",
    (e) => {
      const li = e.target.closest && e.target.closest(".has-dropdown");
      if (!li) return;
      requestAnimationFrame(() => {
        if (!li.contains(document.activeElement)) closeDropdown(li);
      });
    },
    true
  );
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
