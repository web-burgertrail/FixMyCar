# FixMyCar — Roadside Assistance & Car Repair Website

Pure static website (HTML + CSS + JS, koi build step nahi) — seedhe GitHub se Vercel par deploy ho jaayegi.

## Site structure

```
index.html                     → Home
services/                      → Body Repair, Brake Repair, Car AC Repair, Engine Diagnostic, Wheel Alignment, Oil Change
premium/                       → Audi, Mercedes, BMW, Jaguar, Porsche, Bentley, Land Rover, Lexus Repair
rsa/                            → Battery Jumpstart, Flat Tyre, Instant Car Repair, Key Lockout, Mechanical Fault, Towing
pricing.html                   → Transparent Pricing Policy
about/                          → About Us, Team, Gallery
contact.html                   → Contact form
privacy-policy.html, terms-conditions.html, cancellation-refund-policy.html
gadi-kharab.html, garage-on-road.html, roadside-assistance.html   → SEO landing pages (footer-only)
sitemap.xml
partials/header.html, partials/footer.html   → Shared nav & footer (loaded via js/include.js)
css/style.css                  → Design system (dispatch-board / highway-signage theme)
js/main.js, js/include.js      → Nav dropdowns, mobile menu, partial includes
build.py, build2.py            → Python generator scripts used to create all pages (optional, for future edits)
```

**Login** aur **Join FixMyCar Network** links abhi `https://fixmycar24.com/login` aur `/join-network` (external subdomain) par point karte hain — apna actual customer-portal/partner-portal URL daalne ke liye `partials/header.html` aur `partials/footer.html` mein edit karein.

## Local preview

```bash
python3 -m http.server 8000
# phir browser mein: http://localhost:8000
```

## GitHub par push karna

```bash
git init
git add .
git commit -m "Initial FixMyCar website"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo>.git
git push -u origin main
```

## Vercel par deploy karna

1. [vercel.com](https://vercel.com) par login karein (GitHub account se sign-in karna sabse aasan hai).
2. **"Add New" → "Project"** click karein.
3. Apna GitHub repo import karein.
4. Framework preset: **"Other"** (ya "Static") select karein — koi build command ki zaroorat nahi, root directory hi output hai.
5. **Deploy** dabayein. 30-60 second mein live URL mil jaayegi (e.g. `your-repo.vercel.app`).
6. Custom domain (e.g. `roadmech.com`) baad mein **Project → Settings → Domains** se add kar sakte hain.

Future mein koi bhi change GitHub par push karte hi Vercel automatically re-deploy kar dega.

## Content edit karna

- Har page plain HTML hai — text seedhe `.html` files mein edit karein.
- Nav menu ya footer change karna ho to sirf `partials/header.html` / `partials/footer.html` edit karein — sabhi pages automatically update ho jaayenge.
- Naya service/RSA/premium page add karna ho to `build.py` mein list mein entry add karke `python3 build.py` re-run karein, ya manually naya `.html` file existing pattern copy karke banayein.
