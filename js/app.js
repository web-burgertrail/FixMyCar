/* FixMyCar — icons, service-request modal (-> WhatsApp), hero slider, typing effect. */
(function () {
  const WA_NUMBER = "919281410305";

  /* ---------- Inject SVG icons wherever [data-icon] is used ---------- */
  function paintIcons(root) {
    (root || document).querySelectorAll("[data-icon]").forEach((el) => {
      const key = el.getAttribute("data-icon");
      if (window.FMC_ICONS && window.FMC_ICONS[key] && !el.dataset.painted) {
        el.innerHTML = window.FMC_ICONS[key];
        el.dataset.painted = "1";
      }
    });
  }

  /* ---------- Service request modal ---------- */
  function buildModal() {
    if (document.getElementById("fmcModal")) return;
    const wrap = document.createElement("div");
    wrap.id = "fmcModal";
    wrap.className = "fmc-modal";
    wrap.innerHTML = `
      <div class="fmc-modal__backdrop" data-close></div>
      <div class="fmc-modal__panel" role="dialog" aria-modal="true" aria-labelledby="fmcModalTitle">
        <button type="button" class="fmc-modal__close" data-close aria-label="Close" data-icon="close"></button>
        <p class="eyebrow" style="color:#ffb020">Request this service</p>
        <h3 id="fmcModalTitle">Service Request</h3>
        <p class="fmc-modal__sub">Fill this in — we'll open WhatsApp with your request ready to send.</p>
        <form id="fmcModalForm">
          <div class="field" style="margin-bottom:12px;">
            <label for="fmcName">Full Name</label>
            <input id="fmcName" type="text" placeholder="Your name" required>
          </div>
          <div class="field" style="margin-bottom:12px;">
            <label for="fmcPhone">Phone Number</label>
            <input id="fmcPhone" type="tel" placeholder="+91 9XXXXXXXXX" required>
          </div>
          <div class="form-row">
            <div class="field"><label for="fmcCity">City / Location</label><input id="fmcCity" type="text" placeholder="e.g. Hyderabad" required></div>
            <div class="field"><label for="fmcVehicle">Car Model</label><input id="fmcVehicle" type="text" placeholder="e.g. Hyundai i20"></div>
          </div>
          <button type="submit" class="btn btn-sos btn-block" style="margin-top:6px;">
            <span data-icon="whatsapp" class="btn-icon"></span> Send Request on WhatsApp
          </button>
        </form>
      </div>`;
    document.body.appendChild(wrap);
    paintIcons(wrap);

    wrap.querySelectorAll("[data-close]").forEach((el) =>
      el.addEventListener("click", closeModal)
    );
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape") closeModal();
    });

    document.getElementById("fmcModalForm").addEventListener("submit", (e) => {
      e.preventDefault();
      const name = document.getElementById("fmcName").value.trim();
      const phone = document.getElementById("fmcPhone").value.trim();
      const city = document.getElementById("fmcCity").value.trim();
      const vehicle = document.getElementById("fmcVehicle").value.trim();
      const service = wrap.dataset.service || "General Enquiry";

      let msg = `Hi FixMyCar, I need help with *${service}*.%0A`;
      msg += `Name: ${name}%0A`;
      msg += `Phone: ${phone}%0A`;
      msg += `Location: ${city}%0A`;
      if (vehicle) msg += `Car: ${vehicle}%0A`;
      msg += `(sent via fixmycar website)`;

      window.open(`https://wa.me/${WA_NUMBER}?text=${msg}`, "_blank", "noopener");
      closeModal();
      e.target.reset();
    });
  }

  function openModal(serviceName) {
    buildModal();
    const wrap = document.getElementById("fmcModal");
    wrap.dataset.service = serviceName || "General Enquiry";
    wrap.querySelector("#fmcModalTitle").textContent = serviceName || "Service Request";
    wrap.classList.add("is-open");
    document.body.style.overflow = "hidden";
    setTimeout(() => wrap.querySelector("#fmcName").focus(), 150);
  }
  function closeModal() {
    const wrap = document.getElementById("fmcModal");
    if (!wrap) return;
    wrap.classList.remove("is-open");
    document.body.style.overflow = "";
  }
  window.openServiceForm = openModal;

  /* ---------- SOS quick-contact popup (Call Now / WhatsApp) ---------- */
  const CALL_NUMBER = "+919281410305";
  const WA_TEXT = "Hi%20FixMyCar%2C%20I%20need%20roadside%20help.";

  function buildSosModal() {
    if (document.getElementById("sosModal")) return;
    const wrap = document.createElement("div");
    wrap.id = "sosModal";
    wrap.className = "sos-modal";
    wrap.innerHTML = `
      <div class="sos-modal__backdrop" data-sos-close></div>
      <div class="sos-modal__panel" role="dialog" aria-modal="true" aria-labelledby="sosModalTitle">
        <button type="button" class="sos-modal__close" data-sos-close aria-label="Close" data-icon="close"></button>
        <div class="sos-modal__icon" data-icon="phone"></div>
        <h3 id="sosModalTitle">Need help right now?</h3>
        <p>Reach our 24×7 dispatch team the way that's easiest for you.</p>
        <div class="sos-modal__actions">
          <a class="btn btn-sos" href="tel:${CALL_NUMBER}"><span data-icon="phone" class="btn-icon"></span> Call Now</a>
          <a class="btn btn-amber" href="https://wa.me/${CALL_NUMBER.replace("+", "")}?text=${WA_TEXT}" target="_blank" rel="noopener"><span data-icon="whatsapp" class="btn-icon"></span> WhatsApp</a>
        </div>
      </div>`;
    document.body.appendChild(wrap);
    paintIcons(wrap);
    wrap.querySelectorAll("[data-sos-close]").forEach((el) => el.addEventListener("click", closeSosModal));
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape") closeSosModal();
    });
  }

  function openSosModal() {
    buildSosModal();
    const wrap = document.getElementById("sosModal");
    wrap.classList.add("is-open");
    document.body.style.overflow = "hidden";
  }
  function closeSosModal() {
    const wrap = document.getElementById("sosModal");
    if (!wrap) return;
    wrap.classList.remove("is-open");
    document.body.style.overflow = "";
  }
  window.openSOS = openSosModal;

  function wireSosButtons() {
    document.querySelectorAll("[data-sos-trigger]").forEach((btn) => {
      if (btn.dataset.sosWired) return;
      btn.dataset.sosWired = "1";
      btn.addEventListener("click", (e) => {
        e.preventDefault();
        openSosModal();
      });
    });
  }

  /* ---------- Hero typing effect ---------- */
  function startTyping() {
    const words = window.FMC_TYPE_WORDS || [
      "Battery Jumpstart",
      "Flat Tyre Repair",
      "Towing Service",
      "Engine Diagnostic",
      "Key Lockout Help",
    ];
    const el = document.getElementById("heroTyping");
    if (!el) return;
    let wi = 0, ci = 0, deleting = false;

    function tick() {
      const word = words[wi];
      if (!deleting) {
        ci++;
        el.textContent = word.slice(0, ci);
        if (ci === word.length) {
          deleting = true;
          setTimeout(tick, 1400);
          return;
        }
      } else {
        ci--;
        el.textContent = word.slice(0, ci);
        if (ci === 0) {
          deleting = false;
          wi = (wi + 1) % words.length;
        }
      }
      setTimeout(tick, deleting ? 35 : 65);
    }
    tick();
  }

  /* ---------- Hero image slider ---------- */
  function initHeroSlider() {
    const slider = document.querySelector(".hero-slider");
    if (!slider) return;
    const slides = slider.querySelectorAll(".hero-slide");
    const dotsWrap = slider.querySelector(".hero-slider__dots");
    let idx = 0, timer;

    slides.forEach((_, i) => {
      const dot = document.createElement("button");
      dot.type = "button";
      dot.setAttribute("aria-label", "Go to slide " + (i + 1));
      if (i === 0) dot.classList.add("is-active");
      dot.addEventListener("click", () => go(i));
      dotsWrap.appendChild(dot);
    });

    function go(i) {
      slides[idx].classList.remove("is-active");
      dotsWrap.children[idx].classList.remove("is-active");
      idx = (i + slides.length) % slides.length;
      slides[idx].classList.add("is-active");
      dotsWrap.children[idx].classList.add("is-active");
      restart();
    }
    function restart() {
      clearInterval(timer);
      timer = setInterval(() => go(idx + 1), 4200);
    }
    slider.querySelector(".hero-slider__next")?.addEventListener("click", () => go(idx + 1));
    slider.querySelector(".hero-slider__prev")?.addEventListener("click", () => go(idx - 1));
    restart();
  }

  window.FMC_INIT = function () {
    paintIcons(document);
    startTyping();
    initHeroSlider();
    wireSosButtons();
  };

  document.addEventListener("DOMContentLoaded", () => {
    // If header/footer already injected synchronously (rare), init now too.
    paintIcons(document);
  });
})();
