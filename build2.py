#!/usr/bin/env python3
import os
from build import page, breadcrumb, ROOT

# =================================================================
# ROADSIDE PACKAGE (membership / pricing)
# =================================================================
body = """
<section class="page-hero">
  <div class="container">
    <p class="eyebrow" style="color:#ffb020">Membership</p>
    <h1>Roadside Package</h1>
    <p>Annual roadside assistance membership — unlimited SOS call-outs, priority dispatch, and discounted labour on every repair.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Pick a plan</p>
      <h2>Membership Plans</h2>
      <p>All plans include 24×7 RSA dispatch across our network cities.</p>
    </div>
    <div class="pricing-grid">
      <div class="price-card">
        <h3>Basic</h3>
        <div class="amount">₹999<span>/year</span></div>
        <ul>
          <li>4 RSA call-outs/year</li>
          <li>Battery jumpstart &amp; flat tyre</li>
          <li>Standard dispatch priority</li>
          <li>10% off workshop labour</li>
        </ul>
        <a href="/contact.html" class="btn btn-ghost btn-block">Choose Basic</a>
      </div>
      <div class="price-card featured">
        <h3>Family</h3>
        <div class="amount">₹1,999<span>/year</span></div>
        <ul>
          <li>Unlimited RSA call-outs</li>
          <li>Covers up to 2 vehicles</li>
          <li>Priority dispatch (avg 18 min)</li>
          <li>20% off workshop labour</li>
          <li>Free annual inspection</li>
        </ul>
        <a href="/contact.html" class="btn btn-sos btn-block">Choose Family</a>
      </div>
      <div class="price-card">
        <h3>Premium Fleet</h3>
        <div class="amount">₹4,999<span>/year</span></div>
        <ul>
          <li>Unlimited RSA, up to 5 vehicles</li>
          <li>Dedicated relationship manager</li>
          <li>Premium car service specialists</li>
          <li>30% off workshop labour</li>
          <li>Free pickup &amp; drop</li>
        </ul>
        <a href="/contact.html" class="btn btn-ghost btn-block">Choose Premium</a>
      </div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="table-wrap">
      <table>
        <caption>PLAN COMPARISON</caption>
        <thead><tr><th>Feature</th><th>Basic</th><th>Family</th><th>Premium Fleet</th></tr></thead>
        <tbody>
          <tr><td>RSA call-outs</td><td>4/year</td><td>Unlimited</td><td>Unlimited</td></tr>
          <tr><td>Vehicles covered</td><td>1</td><td>2</td><td>5</td></tr>
          <tr><td>Avg. dispatch time</td><td>25 min</td><td>18 min</td><td>15 min</td></tr>
          <tr><td>Workshop labour discount</td><td>10%</td><td>20%</td><td>30%</td></tr>
          <tr><td>Pickup &amp; drop</td><td>—</td><td>Paid</td><td>Free</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="container">
    <h2>Never face a breakdown alone.</h2>
    <p>Activate your Roadside Package today — instant coverage.</p>
    <a href="/contact.html" class="btn btn-amber">Get Started</a>
  </div>
</section>
"""
page("roadside-package.html", "Roadside Package", "FixMyCar annual roadside assistance membership plans — Basic, Family and Premium Fleet.", 0, body,
     trail=[("Roadside Package", None)])


# =================================================================
# ABOUT
# =================================================================
about_body = """
<section class="page-hero">
  <div class="container">
    <p class="eyebrow" style="color:#ffb020">Since 2018</p>
    <h1>About FixMyCar</h1>
    <p>We built FixMyCar because breakdowns don't wait for business hours — and neither do we.</p>
  </div>
</section>
<section class="section">
  <div class="container content-grid">
    <div class="prose">
      <h2>Our story</h2>
      <p>FixMyCar started as a two-mechanic helpline for a single neighbourhood. Today, our network covers 38 cities with over 1,200 verified mechanics, dispatched through one simple call or tap.</p>
      <h2>What we stand for</h2>
      <ul>
        <li>Verified mechanics — background-checked and skill-tested</li>
        <li>Transparent pricing — quoted before work begins</li>
        <li>Live tracking — know exactly when help arrives</li>
        <li>24×7 availability — highways, cities, no exceptions</li>
      </ul>
    </div>
    <aside class="side-card">
      <h3>Talk to us</h3>
      <p>Questions about our network or want to partner as a garage?</p>
      <a href="/contact.html" class="btn btn-amber btn-block">Contact Us</a>
    </aside>
  </div>
</section>
"""
page("about/about-us.html", "About Us", "FixMyCar's story, mission and coverage — 24x7 roadside assistance across 38 cities.", 1, about_body,
     trail=[("About", None), ("About Us", None)])

team_body = """
<section class="page-hero">
  <div class="container">
    <p class="eyebrow" style="color:#ffb020">The people behind dispatch</p>
    <h1>Our Team</h1>
    <p>A mix of master mechanics, dispatch engineers and support staff keeping the network running 24×7.</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="grid">
      <div class="card"><span class="rt">FOUNDER</span><h3>Rakesh Sharma</h3><p>Co-founder &amp; CEO — 15 years in automotive service operations.</p></div>
      <div class="card"><span class="rt">CO-FOUNDER</span><h3>Anita Verma</h3><p>Co-founder &amp; Head of Network — built the mechanic verification program.</p></div>
      <div class="card"><span class="rt">OPS</span><h3>Imran Khan</h3><p>Head of Dispatch — manages live routing across all 38 cities.</p></div>
      <div class="card"><span class="rt">TECH</span><h3>Priya Nair</h3><p>Lead, Master Technician Panel — oversees premium car service quality.</p></div>
      <div class="card"><span class="rt">SUPPORT</span><h3>Deepak Rao</h3><p>Customer Support Lead — runs the 24×7 helpline desk.</p></div>
      <div class="card"><span class="rt">QUALITY</span><h3>Sana Sheikh</h3><p>Quality Assurance — audits mechanic jobs and customer feedback.</p></div>
    </div>
  </div>
</section>
"""
page("about/team.html", "Team", "Meet the FixMyCar team running our 24x7 roadside assistance and repair network.", 1, team_body,
     trail=[("About", None), ("Team", None)])

gallery_body = """
<section class="page-hero">
  <div class="container">
    <p class="eyebrow" style="color:#ffb020">On the job</p>
    <h1>Gallery</h1>
    <p>A look at our garages, mobile units and technicians at work.</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="grid grid-2">
      <div class="card"><span class="rt">01</span><h3>Mobile Repair Van</h3><p>Fully equipped mobile units dispatched for on-site fixes.</p></div>
      <div class="card"><span class="rt">02</span><h3>Partner Garage</h3><p>One of 60+ partner garages in our network.</p></div>
      <div class="card"><span class="rt">03</span><h3>Diagnostic Bay</h3><p>Computerised diagnostic equipment used for engine and electronics checks.</p></div>
      <div class="card"><span class="rt">04</span><h3>Towing Fleet</h3><p>GPS-tracked flatbed tow trucks stationed across the city.</p></div>
    </div>
  </div>
</section>
"""
page("about/gallery.html", "Gallery", "Photos of FixMyCar's garages, mobile repair vans and towing fleet.", 1, gallery_body,
     trail=[("About", None), ("Gallery", None)])


# =================================================================
# CONTACT US
# =================================================================
contact_body = """
<section class="page-hero">
  <div class="container">
    <p class="eyebrow" style="color:#ffb020">We're listening, 24×7</p>
    <h1>Contact Us</h1>
    <p>Reach out for bookings, partnerships, or feedback on a completed job.</p>
  </div>
</section>
<section class="section">
  <div class="container content-grid">
    <div class="form-card">
      <form data-demo-form>
        <div class="form-row">
          <div class="field"><label for="name">Full Name</label><input id="name" type="text" placeholder="Your name" required></div>
          <div class="field"><label for="phone">Phone Number</label><input id="phone" type="tel" placeholder="+91 9XXXXXXXXX" required></div>
        </div>
        <div class="form-row">
          <div class="field"><label for="city">City</label><input id="city" type="text" placeholder="e.g. Hyderabad" required></div>
          <div class="field"><label for="service">Service Needed</label>
            <select id="service">
              <option>Roadside Assistance (RSA)</option>
              <option>Services (Body/Brake/AC/Engine/etc.)</option>
              <option>Premium Car Service</option>
              <option>Roadside Package Membership</option>
              <option>Other</option>
            </select>
          </div>
        </div>
        <div class="field" style="margin-bottom:14px;">
          <label for="msg">Message</label>
          <textarea id="msg" rows="4" placeholder="Tell us what's going on with your car"></textarea>
        </div>
        <button type="submit" class="btn btn-sos btn-block">Send Request</button>
      </form>
    </div>
    <aside class="side-card">
      <h3>Prefer to call?</h3>
      <p>Our 24×7 helpline connects you directly to dispatch.</p>
      <a href="tel:+911800266990" class="btn btn-amber btn-block">📞 1800-266-9900</a>
      <p style="margin-top:18px;">Garage or mechanic wanting to join our network?</p>
      <a href="https://fixmycar24.com/join-network" target="_blank" rel="noopener" class="btn btn-ghost btn-block">Join FixMyCar Network</a>
    </aside>
  </div>
</section>
"""
page("contact.html", "Contact Us", "Contact FixMyCar for bookings, roadside assistance, or partnership enquiries — 24x7 helpline available.", 0, contact_body,
     trail=[("Contact Us", None)])


# =================================================================
# LEGAL PAGES
# =================================================================
def legal_page(path, title, desc, heading, sections):
    prose = "".join(f"<h2>{h}</h2><p>{p}</p>" for h, p in sections)
    body = f"""
<section class="page-hero">
  <div class="container">
    <p class="eyebrow" style="color:#ffb020">Legal</p>
    <h1>{heading}</h1>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="prose" style="max-width:800px;margin:0 auto;">
      {prose}
    </div>
  </div>
</section>
"""
    page(path, title, desc, 0, body, trail=[(title, None)])

legal_page("privacy-policy.html", "Privacy Policy", "How FixMyCar collects, uses and protects your personal data.", "Privacy Policy", [
    ("Information we collect", "We collect your name, phone number, location and vehicle details when you request a service, to dispatch the nearest mechanic and keep you updated on arrival status."),
    ("How we use your information", "Your information is used solely to fulfil service requests, process payments, and improve our dispatch network. We do not sell your data to third parties."),
    ("Data security", "All customer data is stored on encrypted servers with restricted access limited to authorised dispatch and support staff."),
    ("Your rights", "You may request access to, correction of, or deletion of your personal data at any time by contacting our support team."),
])

legal_page("terms-conditions.html", "Terms &amp; Conditions", "Terms of use for booking FixMyCar's car repair and roadside assistance services.", "Terms &amp; Conditions", [
    ("Service availability", "FixMyCar facilitates connections between customers and independent verified mechanics and garages. Arrival times are estimates and may vary due to traffic, weather or location accessibility."),
    ("Pricing", "All service prices are shared as an estimate before work begins. Final billing may vary based on additional parts or labour required, with customer consent."),
    ("Customer responsibilities", "Customers must provide accurate location and vehicle details to enable timely dispatch."),
    ("Limitation of liability", "FixMyCar is not liable for pre-existing vehicle damage discovered during service, or for delays caused by circumstances beyond our control."),
])

legal_page("cancellation-refund-policy.html", "Cancellation &amp; Refund Policy", "FixMyCar's policy on cancelling a service request and refund eligibility.", "Cancellation &amp; Refund Policy", [
    ("Cancelling a request", "You may cancel a service request free of charge before a mechanic has been dispatched. Cancellations after dispatch may incur a nominal call-out charge."),
    ("Refund eligibility", "Refunds are processed if a service was booked but not delivered due to a fault on FixMyCar's end, within 5-7 business days to the original payment method."),
    ("Membership refunds", "Roadside Package memberships are refundable on a pro-rata basis within 15 days of purchase, provided no RSA call-out has been used."),
])


# =================================================================
# SEO LANDING PAGES (footer-only / hidden pages)
# =================================================================
def seo_page(path, title, desc, eyebrow, heading, lead, sections, cta_text="Call 1800-266-9900"):
    prose = "".join(f"<h2>{h}</h2><p>{p}</p>" for h, p in sections)
    body = f"""
<section class="page-hero">
  <div class="container">
    <p class="eyebrow" style="color:#ffb020">{eyebrow}</p>
    <h1>{heading}</h1>
    <p>{lead}</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="prose" style="max-width:800px;margin:0 auto;">
      {prose}
    </div>
  </div>
</section>
<section class="cta-band">
  <div class="container">
    <h2>Help is one call away.</h2>
    <a href="tel:+911800266990" class="btn btn-amber">📞 {cta_text}</a>
  </div>
</section>
"""
    page(path, title, desc, 0, body, trail=[(title, None)])

seo_page("gadi-kharab.html", "Gadi Kharab? 24x7 Madad", "Gadi kharab ho gayi? FixMyCar se turant 24x7 roadside assistance aur mechanic madad payein.",
    "Hindi Local Help", "Gadi Kharab Ho Gayi? Hum Yahan Hain",
    "Raste mein gadi kharab ho jaaye to ghabraye nahi — FixMyCar ka verified mechanic aapki location par turant pahunchta hai.",
    [("Kya kya madad milegi?", "Battery jumpstart, flat tyre, towing, aur chhoti-moti mechanical kharabi — sab kuch ek call par."),
     ("Kitni der mein mechanic aayega?", "Zyadatar shehron mein average 20-25 minute mein mechanic dispatch ho jaata hai."),
     ("Payment kaise hoga?", "Kaam shuru hone se pehle price bataya jaata hai, koi hidden charge nahi.")])

seo_page("garage-on-road.html", "Garage On-Road — Mobile Car Repair", "On-road mobile garage service — mechanic reaches your car's location for instant repair, no towing needed.",
    "Mobile Garage", "Garage On-Road, Wherever You Are",
    "Why tow your car to a garage when the garage can come to you? Our mobile mechanics carry the tools for most on-site repairs.",
    [("What can be fixed on-road?", "Battery, tyre, minor mechanical faults, fluid top-ups and basic diagnostics can usually be handled without towing."),
     ("When is towing still needed?", "Major engine, transmission or accident damage is towed to the nearest partner garage for a full repair.")])

seo_page("roadside-assistance.html", "Roadside Assistance", "FixMyCar roadside assistance — 24x7 emergency help for battery, tyre, towing and lockouts across India.",
    "24x7 Emergency Help", "Roadside Assistance, Anytime, Anywhere",
    "From a flat tyre on the highway to a dead battery in a parking lot, FixMyCar's roadside assistance network has you covered around the clock.",
    [("Coverage", "Our RSA network is active across 38 cities and major highways connecting them."),
     ("Services covered", "Battery jumpstart, flat tyre, key lockout, towing, and on-site mechanical fault diagnosis."),
     ("Membership option", "Frequent travellers can save with our Roadside Package annual membership for unlimited call-outs.")])


# =================================================================
# SITEMAP.XML
# =================================================================
urls = [
    "", "roadside-package.html", "contact.html",
    "privacy-policy.html", "terms-conditions.html", "cancellation-refund-policy.html",
    "gadi-kharab.html", "garage-on-road.html", "roadside-assistance.html",
    "about/about-us.html", "about/team.html", "about/gallery.html",
] + [f"services/{h}" for h in ["body-repair.html","brake-repair.html","car-ac-repair.html","engine-diagnostic.html","wheel-alignment.html","oil-change.html"]] \
  + [f"premium/{h}" for h in ["audi-repair.html","mercedes-repair.html","bmw-repair.html","jaguar-repair.html","porsche-repair.html","bentley-repair.html","land-rover-repair.html","lexus-repair.html"]] \
  + [f"rsa/{h}" for h in ["battery-jumpstart.html","flat-tyre.html","instant-car-repair.html","key-lockout.html","mechanical-fault.html","towing-services.html"]]

BASE_URL = "https://www.fixmycar-example.com"
entries = "\n".join(
    f'  <url><loc>{BASE_URL}/{u}</loc></url>' for u in urls
)
sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{entries}
</urlset>
"""
with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write(sitemap)
print("wrote sitemap.xml")
print("All support pages generated.")
