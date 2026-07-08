#!/usr/bin/env python3
"""Generates every page of the FixMyCar static site from shared templates.
Run: python3 build.py
Output pages are written directly into the site folders (services/, rsa/, premium/, about/, root).
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

HEAD = """<!DOCTYPE html>
<html lang="en" data-depth="{depth}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | FixMyCar</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}css/style.css">
</head>
<body>
<div id="site-header"></div>
"""

FOOT = """
<div id="site-footer"></div>
<script src="{root}js/main.js"></script>
<script src="{root}js/include.js"></script>
</body>
</html>
"""

def breadcrumb(root, trail):
    """trail: list of (label, href_or_None)"""
    parts = [f'<a href="{root}index.html">Home</a>']
    for label, href in trail:
        parts.append('<span>/</span>')
        if href:
            parts.append(f'<a href="{root}{href}">{label}</a>')
        else:
            parts.append(f'<span style="color:#f5f3ee">{label}</span>')
    return f'<div class="breadcrumb"><div class="container">{"".join(parts)}</div></div>'


def page(path, title, desc, depth, body, trail=None):
    root = "../" * depth if depth else "./"
    html = HEAD.format(title=title, desc=desc, depth=depth, root=root)
    if trail is not None:
        html += breadcrumb(root, trail)
    html += body
    html += FOOT.format(root=root)
    full_path = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", path)


# ---------------------------------------------------------------
# Detail-page template used for Services / Premium / RSA items
# ---------------------------------------------------------------
def detail_page(path, depth, section_label, section_href, name, rt_code,
                 tagline, includes, issues, faqs, related, eta="25-30 min", price_from="₹499"):
    root = "../" * depth
    body = f"""
<section class="page-hero">
  <div class="container">
    <p class="eyebrow" style="color:#ffb020">{section_label} · {rt_code}</p>
    <h1>{name}</h1>
    <p>{tagline}</p>
  </div>
</section>

<section class="section">
  <div class="container content-grid">
    <div class="prose">
      <h2>What's included</h2>
      <ul>
        {''.join(f'<li>{item}</li>' for item in includes)}
      </ul>

      <h2>Common issues we fix</h2>
      <ul>
        {''.join(f'<li>{item}</li>' for item in issues)}
      </ul>

      <h2>Frequently asked questions</h2>
      {''.join(f'''<details class="faq-item"><summary>{q}</summary><p>{a}</p></details>''' for q, a in faqs)}
    </div>

    <aside class="side-card">
      <p class="eyebrow" style="color:#ffb020">Dispatch status</p>
      <h3>{eta} avg. arrival</h3>
      <p>Verified mechanic dispatched from the nearest FixMyCar garage. Live tracking link sent by SMS. Starting at <strong style="color:#fff">{price_from}</strong>.</p>
      <a href="tel:+911800266990" class="btn btn-sos btn-block">📞 Request {name}</a>
      <a href="{root}contact.html" class="btn btn-ghost btn-block" style="margin-top:10px;">Get a Quote</a>
    </aside>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Related</p>
      <h2>You might also need</h2>
    </div>
    <div class="grid">
      {''.join(f'''<div class="card"><span class="rt">{r[2]}</span><h3>{r[0]}</h3><p>{r[3]}</p><a class="card-link" href="{root}{r[1]}">View details →</a></div>''' for r in related)}
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="container">
    <h2>Stuck on the road right now?</h2>
    <p>Our nearest mechanic is already on standby.</p>
    <a href="tel:+911800266990" class="btn btn-amber">📞 Call 1800-266-9900</a>
  </div>
</section>
"""
    page(path, name, tagline, depth, body,
         trail=[(section_label, section_href), (name, None)])


# =================================================================
# SERVICES
# =================================================================
services = [
    ("Body Repair", "body-repair.html", "RT-01",
     "Dent removal, panel beating and refinishing to restore your car's body to showroom finish.",
     ["Free damage assessment at your location", "Dent & scratch removal", "Panel beating and re-alignment", "Bumper and body kit repair", "Colour-matched refinishing"],
     ["Minor dents from parking scrapes", "Deep scratches down to primer", "Bent or misaligned bumpers", "Rust patches on body panels"],
     [("How long does body repair take?", "Minor dent and scratch jobs are usually done in 2-4 hours; full panel work may take 1-2 days depending on parts availability."),
      ("Do you match my car's paint colour?", "Yes, we scan your factory paint code and colour-match before refinishing.")]),

    ("Brake Repair", "brake-repair.html", "RT-02",
     "Pad replacement, disc resurfacing and full brake system checks for safer stopping power.",
     ["Brake pad and shoe replacement", "Disc/drum resurfacing or replacement", "Brake fluid flush and bleed", "Caliper and cylinder inspection", "ABS sensor check"],
     ["Squeaking or grinding noise while braking", "Soft or spongy brake pedal", "Car pulling to one side while braking", "Brake warning light on dashboard"],
     [("How do I know my brake pads need changing?", "A high-pitched squeal or grinding sound, or a longer stopping distance, usually means the pads are worn and due for replacement."),
      ("Can this be done at my home or office?", "Yes, our mobile mechanic carries standard pads and tools for most models; heavier jobs are routed to the nearest garage.")]),

    ("Car AC Repair", "car-ac-repair.html", "RT-03",
     "Gas refilling, compressor repair and full AC servicing to keep your cabin cool.",
     ["AC gas top-up and leak test", "Compressor inspection and repair", "Cabin filter replacement", "Cooling coil cleaning", "Full AC performance check"],
     ["AC blowing warm or weak air", "Unusual smell from vents", "Compressor clutch not engaging", "Gas leakage at fittings"],
     [("Why is my car AC not cooling?", "The most common cause is low refrigerant due to a slow leak; a gas top-up with a leak test usually resolves it."),
      ("How often should AC gas be refilled?", "Under normal use, once every 1-2 years is typical, sooner if there's an active leak.")]),

    ("Engine Diagnostic", "engine-diagnostic.html", "RT-04",
     "Computerised OBD scanning to pinpoint check-engine faults before they become expensive.",
     ["Full OBD-II computer scan", "Check-engine light diagnosis", "Sensor and wiring inspection", "Fuel and ignition system check", "Printed diagnostic report"],
     ["Check-engine light stays on", "Rough idling or stalling", "Sudden drop in mileage", "Unusual engine noises"],
     [("Is diagnostic scanning free?", "The scan fee is adjusted against the repair if you proceed with us."),
      ("Will you tell me the exact fault code?", "Yes, you get a printed report with fault codes and a plain-language explanation.")]),

    ("Wheel Alignment", "wheel-alignment.html", "RT-05",
     "Computerised 4-wheel alignment and balancing for even tyre wear and a straight, stable drive.",
     ["Computerised 4-wheel alignment", "Wheel balancing", "Tyre rotation", "Suspension and steering check", "Alignment report print-out"],
     ["Car pulling left or right", "Uneven tyre wear pattern", "Steering wheel off-centre", "Vibration at highway speed"],
     [("How often should I get alignment done?", "Every 10,000 km, or immediately after hitting a pothole hard or replacing tyres."),
      ("Is balancing included with alignment?", "We recommend both together; they're billed separately but often bundled at a discount.")]),

    ("Oil Change", "oil-change.html", "RT-06",
     "Engine oil and filter replacement using OEM-grade or fully synthetic oil, at your doorstep.",
     ["Engine oil drain and refill", "Oil filter replacement", "Multi-point vehicle check", "Fluid top-up (coolant, wiper)", "Old oil disposed responsibly"],
     ["Oil change due / warning light on", "Noisy engine due to old oil", "Burning oil smell", "Dark, gritty oil on dipstick"],
     [("Which oil do you use?", "We stock mineral, semi-synthetic and full-synthetic grades — you choose based on your car's manual and budget."),
      ("Can this be done at home?", "Yes, our doorstep oil-change service carries everything needed for most hatchback and sedan models.")]),
]

svc_related_pool = [(n, href, rt, tag) for n, href, rt, tag, *_ in services]

for i, (name, href, rt, tag, includes, issues, faqs) in enumerate(services):
    related = [r for r in svc_related_pool if r[1] != href][:3]
    related = [(r[0], "services/" + r[1], r[2], r[3]) for r in related]
    detail_page(f"services/{href}", 1, "Services", "index.html#services", name, rt, tag, includes, issues, faqs, related)


# =================================================================
# PREMIUM CAR SERVICES
# =================================================================
premium = [
    ("Audi Repair", "audi-repair.html", "quattro drivetrain, TFSI engines and Audi-specific electronics — serviced by brand-trained technicians."),
    ("Mercedes Repair", "mercedes-repair.html", "AIRMATIC suspension, COMAND systems and Mercedes engines diagnosed with OEM-level tools."),
    ("BMW Repair", "bmw-repair.html", "BMW engine, iDrive electronics and run-flat tyre systems handled by specialists."),
    ("Jaguar Repair", "jaguar-repair.html", "Aluminium body repair and Jaguar's electronic systems serviced with factory-approved parts."),
    ("Porsche Repair", "porsche-repair.html", "PDK gearboxes, PASM suspension and high-performance engines maintained to Porsche spec."),
    ("Bentley Repair", "bentley-repair.html", "Handcrafted interiors and W12/V8 engines serviced with the discretion a Bentley deserves."),
    ("Land Rover Repair", "land-rover-repair.html", "Terrain-response systems and air suspension diagnosed and repaired by 4x4 specialists."),
    ("Lexus Repair", "lexus-repair.html", "Hybrid drivetrains and Lexus electronics serviced with manufacturer-grade diagnostic tools."),
]
prem_related_pool = premium

for i, (name, href, tag) in enumerate(premium):
    includes = ["Brand-specific diagnostic scan", "OEM or OE-equivalent parts", "Certified technician assigned", "Detailed job-card and warranty on repair", "Doorstep pickup & drop available"]
    issues = ["Dashboard warning lights / electronic faults", "Suspension and ride-height issues", "Engine or transmission performance drop", "Infotainment and electrical glitches"]
    faqs = [(f"Do you use genuine parts for {name.split()[0]}?", "We use OEM parts where available, and OE-equivalent alternatives with your consent for non-critical parts."),
            ("Is doorstep pickup available for luxury cars?", "Yes, we offer insured pickup and drop for premium vehicles across the city.")]
    related = [(r[0], "premium/" + r[1], "★", r[2]) for r in prem_related_pool if r[1] != href][:3]
    detail_page(f"premium/{href}", 1, "Premium Car Services", "index.html#premium", name, "PREMIUM", tag, includes, issues, faqs, related, eta="35-45 min", price_from="₹1,499")


# =================================================================
# RSA (ROADSIDE ASSISTANCE) SERVICES
# =================================================================
rsa_services = [
    ("Battery Jumpstart", "battery-jumpstart.html", "SOS-01",
     "Dead battery? Our nearest mechanic reaches you with a jumpstart kit in minutes.",
     ["On-spot battery jumpstart", "Battery health check", "Terminal cleaning", "New battery replacement if needed"],
     ["Car won't start / clicking sound", "Dim headlights or dashboard lights", "Battery drained after long parking"]),
    ("Flat Tyre", "flat-tyre.html", "SOS-02",
     "Puncture or blowout on the road — we fit your spare or repair on the spot.",
     ["Spare wheel fitment", "On-spot puncture repair", "Tyre pressure check", "Tow to nearest garage if unrepairable"],
     ["Sudden tyre burst on highway", "Slow puncture / losing air", "No spare wheel available"]),
    ("Instant Car Repair", "instant-car-repair.html", "SOS-03",
     "A mobile mechanic reaches your location for small fixes so you don't need a tow.",
     ["On-site fault diagnosis", "Minor part replacement", "Fluid top-ups", "Temporary fix to reach a garage safely"],
     ["Warning light suddenly on", "Strange noise while driving", "Car stalls but restarts"]),
    ("Key Lockout", "key-lockout.html", "SOS-04",
     "Locked your keys inside? Our technician gets you back in without damaging your car.",
     ["Non-destructive lock opening", "Spare key cutting (select models)", "Central locking system check"],
     ["Keys locked inside the car", "Key snapped in the lock", "Central locking malfunction"]),
    ("Mechanical Fault", "mechanical-fault.html", "SOS-05",
     "Any unexpected mechanical breakdown — a technician is dispatched to diagnose and fix on-site.",
     ["On-site mechanical diagnosis", "Belt, hose and clamp fixes", "Coolant/oil leak temporary fix", "Tow arrangement if not fixable on-site"],
     ["Engine overheating", "Unusual smell or smoke", "Loss of power while driving"]),
    ("Towing Services", "towing-services.html", "SOS-06",
     "Flatbed towing to your preferred garage or our nearest FixMyCar service centre.",
     ["Flatbed towing (no drag damage)", "Accident vehicle recovery", "Long-distance towing available", "GPS-tracked tow truck"],
     ["Accident or major breakdown", "Vehicle won't start after diagnostics", "Need to move car to a specific garage"]),
]
rsa_related_pool = [(n, href, rt) for n, href, rt, *_ in rsa_services]

for name, href, rt, tag, includes, issues in rsa_services:
    faqs = [("How fast can you reach me?", "Average arrival time is 20-30 minutes in city areas, depending on traffic and your location."),
            ("Is this available at night?", "Yes, all RSA services run 24×7, including highways and outstation routes.")]
    related = [(r[0], "rsa/" + r[1], r[2], "24×7 roadside help") for r in rsa_related_pool if r[1] != href][:3]
    detail_page(f"rsa/{href}", 1, "RSA Services", "index.html#rsa", name, rt, tag, includes, issues, faqs, related, eta="20-25 min", price_from="₹299")

print("All detail pages generated.")
