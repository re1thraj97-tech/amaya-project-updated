#!/usr/bin/env python3
"""
AMAYA Project — static site generator.

Shared chrome lives here: <head>, meta/Open Graph, header + navigation,
breadcrumbs, previous/next pager, footer and JSON-LD.
Page bodies live in pages.py.

Rebuild:  python3 build.py
"""
import os
from pages import BODIES

BASE = "https://re1thraj97-tech.github.io/amaya-project-updated/"
OG_IMAGE = BASE + "copper-band.jpg"

# key, output file, header/footer nav label, full label (crumbs, pager, sitemap)
NAV = [
    ("index",      "index.html",      "Home",                 "Home"),
    ("project",    "project.html",    "The Project",          "The Project"),
    ("mines",      "mines.html",      "Our Mines",            "Our Mines"),
    ("location",   "location.html",   "Location",             "Location & Logistics"),
    ("market",     "market.html",     "Copper Market",        "Copper Market"),
    ("leadership", "leadership.html", "Leadership",           "Leadership"),
    ("about",      "about.html",      "About",                "About"),
]

META = {
    "index": dict(
        title="AMAYA — Copper Exploration Project, Atacama Desert, Chile",
        desc="AMAYA is a copper exploration project in the Atacama Desert, Chile, comprising 9 copper concessions covering 2,353 hectares (5,814 acres) at 3,800 m above sea level, 80 km north of Calama.",
        ld_desc="AMAYA comprises 9 copper concessions covering a total area of 2,353 hectares, equivalent to approximately 5,814 acres, in the Atacama Desert at 3,800 metres above sea level, 80 km north of Calama, Chile.",
    ),
    "project": dict(
        title="The Project — Concessions & Geology | AMAYA",
        desc="AMAYA comprises 9 copper concessions covering 2,353 hectares (5,814 acres) on the West Fault corridor in the Atacama Desert, Chile. Full concession breakdown, geology and exploration programme.",
        ld_desc="Full breakdown of AMAYA's 9 copper concessions totalling 2,353 hectares (5,814 acres), the West Fault structural setting and the exploration programme.",
    ),
    "mines": dict(
        title="Our Mines — Copper Ore & Iron Ore Mining Assets | AMAYA",
        desc="AMAYA holds two mining assets: a copper ore mine and an iron ore mine, both currently in progress. Site galleries, footage and operational detail as the company releases them.",
        ld_desc="AMAYA's mining assets comprise a copper ore mine and an iron ore mine, both currently in progress.",
    ),
    "location": dict(
        title="Location & Logistics — Calama Airport & Export Ports | AMAYA",
        desc="AMAYA is 80 km north of Calama in the Atacama Desert, Chile: approx. 85 km from Calama Airport (CJC), with Tocopilla the nearest port at approx. 125–130 km, plus Puerto Angamos (Mejillones) and Antofagasta.",
        ld_desc="Distances from the AMAYA copper exploration project to Calama Airport and to the Tocopilla, Puerto Angamos (Mejillones) and Antofagasta export ports, plus neighbouring producing operations in the Atacama mining district.",
    ),
    "market": dict(
        title="Copper Market — Indicative Price per Metric Tonne | AMAYA",
        desc="Current indicative copper market reference price per metric tonne in USD, with source and date, plus the electrification and grid demand backdrop for copper exploration in Chile.",
        ld_desc="Indicative copper market reference price per metric tonne and the demand context for copper exploration in northern Chile.",
    ),
    "leadership": dict(
        title="Leadership — Executive Team | AMAYA",
        desc="The people leading AMAYA: B. Satish Naidu, Chief Executive Officer, with the Managing Director, Chief Financial Officer and Chief Geologist.",
        ld_desc="The executive team leading the AMAYA Project: Chief Executive Officer, Managing Director, Chief Financial Officer and Chief Geologist.",
    ),
    "about": dict(
        title="About — Responsible Exploration & Contact | AMAYA",
        desc="AMAYA's approach to responsible exploration in the Atacama Desert, Chile, and investor contact details for the copper exploration project.",
        ld_desc="Responsible exploration approach and investor contact details for the AMAYA copper exploration project in the Atacama Desert, Chile.",
    ),
}

SVG_DEFS = """<svg width="0" height="0" style="position:absolute" aria-hidden="true">
  <defs>
    <linearGradient id="cu" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#f7c898"/><stop offset="35%" stop-color="#f0a868"/>
      <stop offset="65%" stop-color="#c87533"/><stop offset="100%" stop-color="#7a3f18"/>
    </linearGradient>
    <linearGradient id="cu2" x1="0" y1="1" x2="1" y2="0">
      <stop offset="0%" stop-color="#8a4a1e"/><stop offset="50%" stop-color="#c87533"/><stop offset="100%" stop-color="#f7c898"/>
    </linearGradient>
    <radialGradient id="core" cx="38%" cy="32%">
      <stop offset="0%" stop-color="#ffe3c4"/><stop offset="42%" stop-color="#f0a868"/>
      <stop offset="78%" stop-color="#b9682c"/><stop offset="100%" stop-color="#5e2f10"/>
    </radialGradient>
    <linearGradient id="fe" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#cfd6df"/><stop offset="40%" stop-color="#93a0b0"/>
      <stop offset="72%" stop-color="#5d6a7a"/><stop offset="100%" stop-color="#2e3844"/>
    </linearGradient>
    <linearGradient id="sweepg" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#4fbfa8" stop-opacity="0"/>
      <stop offset="72%" stop-color="#4fbfa8" stop-opacity=".13"/>
      <stop offset="100%" stop-color="#9fffe9" stop-opacity=".45"/>
    </linearGradient>
  </defs>
</svg>"""


def url_for(fname):
    return BASE if fname == "index.html" else BASE + fname


def head(key, fname):
    m = META[key]
    t = m["title"].replace("&", "&amp;")
    d = m["desc"].replace("&", "&amp;")
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t}</title>
<meta name="description" content="{d}">
<meta name="theme-color" content="#07090d">
<link rel="canonical" href="{url_for(fname)}">
<link rel="icon" href="logo.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="AMAYA Project">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:url" content="{url_for(fname)}">
<meta property="og:image" content="{OG_IMAGE}">
<meta property="og:locale" content="en">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{t}">
<meta name="twitter:description" content="{d}">
<meta name="twitter:image" content="{OG_IMAGE}">
<link rel="stylesheet" href="styles.css">
</head>
<body>

<a class="skip" href="#main">Skip to content</a>

<canvas id="dust" aria-hidden="true"></canvas>
<div class="glow" aria-hidden="true"></div>
<div class="grid" aria-hidden="true"></div>
<div class="scan" aria-hidden="true"></div>

{SVG_DEFS}
"""


def header(key):
    items = []
    for k, fname, nav_label, _full in NAV:
        cur = ' aria-current="page"' if k == key else ''
        items.append(f'      <li><a href="{fname}"{cur}>{nav_label.replace("&", "&amp;")}</a></li>')
    links = "\n".join(items)
    return f"""<header>
  <div class="wrap nav">
    <a class="brand" href="index.html" aria-label="AMAYA Project — home"><img src="logo.png" alt="AMAYA Project logo" width="110" height="32"><span>Amaya</span></a>
    <button class="burger" id="burger" type="button" aria-expanded="false" aria-controls="menu" aria-label="Open navigation menu">
      <span></span><span></span><span></span>
    </button>
    <ul id="menu">
{links}
    </ul>
  </div>
  <div id="prog" aria-hidden="true"></div>
</header>

<main id="main">
"""


def pager(key):
    keys = [n[0] for n in NAV]
    if key == "index":
        return ""
    i = keys.index(key)
    prev = NAV[i - 1]
    nxt = NAV[(i + 1) % len(NAV)]
    return f"""
<section style="padding-top:0"><div class="wrap"><div class="pager">
  <a class="prev" href="{prev[1]}"><small>Previous</small><b>{prev[3]}</b></a>
  <a class="next" href="{nxt[1]}"><small>Next</small><b>{nxt[3]}</b></a>
</div></div></section>
"""


def footer():
    links = "\n".join(
        f'        <a href="{f}">{full.replace("&", "&amp;")}</a>' for _k, f, _lbl, full in NAV
    )
    return f"""</main>

<footer>
  <div class="wrap foot">
    <div>
      <div style="color:var(--txt);margin-bottom:8px">AMAYA Project</div>
      <div>Copper exploration &middot; Atacama Desert<br>Regi&oacute;n de Antofagasta, Chile</div>
      <div style="margin-top:14px"><a href="mailto:info@amayaproject.com" style="color:var(--cu-lt)">info@amayaproject.com</a></div>
    </div>
    <nav class="foot-links" aria-label="Footer">
{links}
    </nav>
    <div>&copy; <span id="yr">2026</span> AMAYA Project.<br>All rights reserved.</div>
  </div>
</footer>
"""


def jsonld(key, fname):
    m = META[key]
    page_id = (BASE + "#webpage") if fname == "index.html" else (BASE + fname + "#webpage")
    graph = f"""    {{
      "@type": "WebSite",
      "@id": "{BASE}#website",
      "url": "{BASE}",
      "name": "AMAYA Project",
      "description": "AMAYA is a copper exploration project in the Atacama Desert, Chile, comprising 9 copper concessions covering 2,353 hectares (5,814 acres).",
      "inLanguage": "en"
    }},
    {{
      "@type": "Organization",
      "@id": "{BASE}#organization",
      "name": "AMAYA Project",
      "url": "{BASE}",
      "logo": "{BASE}logo.png",
      "email": "info@amayaproject.com",
      "description": "Copper exploration project in the Atacama Desert, Región de Antofagasta, Chile.",
      "address": {{
        "@type": "PostalAddress",
        "addressRegion": "Región de Antofagasta",
        "addressCountry": "CL"
      }}
    }},
    {{
      "@type": "WebPage",
      "@id": "{page_id}",
      "url": "{url_for(fname)}",
      "name": "{m['title']}",
      "isPartOf": {{
        "@id": "{BASE}#website"
      }},
      "about": {{
        "@id": "{BASE}#organization"
      }},
      "description": "{m['ld_desc']}",
      "inLanguage": "en"
    }}"""
    if fname != "index.html":
        full = dict((n[0], n[3]) for n in NAV)[key]
        graph += f""",
    {{
      "@type": "BreadcrumbList",
      "@id": "{BASE}{fname}#breadcrumb",
      "itemListElement": [
        {{
          "@type": "ListItem",
          "position": 1,
          "name": "Amaya",
          "item": "{BASE}"
        }},
        {{
          "@type": "ListItem",
          "position": 2,
          "name": "{full}",
          "item": "{BASE}{fname}"
        }}
      ]
    }}"""
    return f"""
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@graph": [
{graph}
  ]
}}
</script>
<script src="app.js" defer></script>
</body>
</html>
"""


def sitemap():
    rows = "\n".join(
        f"""  <url>
    <loc>{url_for(f)}</loc>
    <changefreq>monthly</changefreq>
    <priority>{'1.0' if f == 'index.html' else '0.8'}</priority>
  </url>"""
        for _k, f, _l, _x in NAV
    )
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{rows}
</urlset>
"""


def main():
    for key, fname, _l, _x in NAV:
        html = head(key, fname) + header(key) + BODIES[key] + pager(key) + footer() + jsonld(key, fname)
        with open(fname, "w", encoding="utf-8") as fh:
            fh.write(html)
        print(f"{fname} {os.path.getsize(fname)} bytes")
    with open("sitemap.xml", "w", encoding="utf-8") as fh:
        fh.write(sitemap())
    print("sitemap.xml written")


if __name__ == "__main__":
    main()
