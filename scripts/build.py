#!/usr/bin/env python3
"""Build the static website with the Python standard library."""
from pathlib import Path
import html
import json
import shutil

ROOT = Path(__file__).resolve().parent.parent
PAPERS = json.loads((ROOT / 'content/research.json').read_text())
escape = html.escape
EMAIL = 'oliyide.ayobamij@gmail.com'
SOCIAL = [
    ('GitHub', 'https://github.com/JohnsonOliyide'),
    ('LinkedIn', 'https://www.linkedin.com/in/johnson-oliyide-a6816a178/'),
    ('X', 'https://twitter.com/JohnsonOliyide'),
]
NAV = [('About', ''), ('Research', 'research'), ('CV', 'cv'),
       ('Macro Lab', 'macro-lab'), ('Contact', 'contact')]

def external(label, url, css=''):
    return f'<a class="{css}" href="{escape(url, quote=True)}" target="_blank" rel="noopener noreferrer">{escape(label)}</a>'

def page(title, slug, content, description):
    base = '../' if slug else './'
    nav = ''.join(
        f'<a href="{base}{path + "/" if path else ""}"'
        + (' aria-current="page"' if path == slug else '')
        + f'>{label}</a>' for label, path in NAV)
    socials = ''.join(external(label, url) for label, url in SOCIAL)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light">
<title>{escape(title)} | Johnson Oliyide</title>
<meta name="description" content="{escape(description, quote=True)}">
<link rel="icon" href="{base}assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{base}assets/site.css">
<script defer src="{base}assets/site.js"></script>
</head>
<body>
<a class="skip-link" href="#main">Skip to main content</a>
<header class="site-header"><div class="header-inner"><a class="wordmark" href="{base}" aria-label="Johnson Oliyide home">JO.</a><nav class="site-nav" aria-label="Main navigation">{nav}</nav></div></header>
{content}
<footer class="site-footer"><div><div class="footer-name">Johnson Oliyide</div><a class="footer-email" href="mailto:{EMAIL}">{EMAIL}</a><div class="footer-social">{socials}</div></div><p class="disclaimer">The views expressed here are my own and do not represent the Federal Reserve Bank of Kansas City or the Federal Reserve System.</p></footer>
</body></html>
'''

def paper(item):
    links = ''
    if item.get('pdf'):
        links += f'<a href="../{escape(item["pdf"], quote=True)}" download aria-label="Download PDF: {escape(item["title"], quote=True)}">Download PDF <span aria-hidden="true">↓</span></a>'
    else:
        links += '<span class="pdf-pending">PDF file forthcoming</span>'
    links += external('Publication ↗', item['url'])
    extras = []
    for extra in item.get('extras', []):
        extras.append(external(extra['label'], extra['url']))
    return f'''<article class="paper" id="{item['id']}"><div class="paper-year">{item['year']}</div><div>
<h3><a href="{escape(item['url'], quote=True)}" target="_blank" rel="noopener noreferrer">{escape(item['title'])}</a></h3>
<p class="paper-authors">With {escape(item['coauthors'])}</p>
<p class="paper-venue">{escape(item['venue'])}</p>
<div class="paper-actions"><button class="abstract-toggle" type="button" data-abstract aria-expanded="false" aria-controls="abstract-{item['id']}" hidden>Abstract <span data-sign aria-hidden="true">+</span><span class="sr-only"> for {escape(item['title'])}</span></button>{links}</div>
<div class="paper-abstract" id="abstract-{item['id']}" role="region" aria-label="Abstract: {escape(item['title'], quote=True)}"><p>{escape(item['abstract'])}</p></div>
{('<p class="paper-extras">' + ' · '.join(extras) + '</p>') if extras else ''}
</div></article>'''

def write(slug, title, content, description):
    folder = ROOT / slug
    folder.mkdir(parents=True, exist_ok=True)
    (folder / 'index.html').write_text(page(title, slug, content, description))

home = '''<main id="main"><section class="hero"><div><h1>Johnson Ayobami<br>Oliyide</h1><p class="role">Research Associate<br><span>Federal Reserve Bank of Kansas City</span></p><div class="interests"><p class="eyebrow">Research interests</p><p>Macroeconomics<br>Monetary Economics<br>Finance</p></div><div class="actions"><a class="button" href="research/">View research <span aria-hidden="true">↗</span></a><a class="text-link" href="cv/">Curriculum vitae</a></div></div><figure class="portrait"><img src="assets/johnson-oliyide.jpg" alt="Johnson Oliyide" width="1280" height="1922" fetchpriority="high"></figure></section></main>
<section class="bio-band" aria-labelledby="background-label"><div class="bio-inner"><p id="background-label" class="eyebrow">Background</p><p>I hold an M.S. in Economics from the University of Maine and a B.Sc. in Economics from the Federal University of Agriculture, Abeokuta. My research experience began in 2020 and includes work at the University of Maine’s Market Integration Research Lab and the Kansas City Fed.</p></div></section>
<section class="research-index" style="max-width:1100px;margin:auto" aria-labelledby="research-heading"><p class="eyebrow">Explore my work</p><h2 id="research-heading">Research</h2><article><div><h3>Policy Research</h3><p>Research on monetary policy and labor market conditions.</p></div><a class="text-link" href="research/#policy-research">View policy research <span aria-hidden="true">↗</span></a></article><article><div><h3>Academic Journal Publications</h3><p>Published work on financial markets, energy, and economic development.</p></div><a class="text-link" href="research/#academic-publications">View publications <span aria-hidden="true">↗</span></a></article><article><div><h3>Work in Progress</h3><p>Ongoing research projects.</p></div><a class="text-link" href="research/#work-in-progress">View work in progress <span aria-hidden="true">↗</span></a></article></section>'''
write('', 'About', home, 'Johnson Ayobami Oliyide is a Research Associate at the Federal Reserve Bank of Kansas City. Research in macroeconomics, monetary economics, and finance.')

policy = ''.join(paper(p) for p in PAPERS if p['category'] == 'policy')
academic = ''.join(paper(p) for p in PAPERS if p['category'] == 'academic')
research = f'''<main id="main" class="page"><h1>Research</h1><section class="research-section" id="policy-research" aria-labelledby="policy-heading"><h2 id="policy-heading">Policy Research</h2>{policy}</section><section class="research-section" id="academic-publications" aria-labelledby="academic-heading"><h2 id="academic-heading">Academic Journal Publications</h2>{academic}</section><section class="research-section" id="work-in-progress" aria-labelledby="progress-heading"><h2 id="progress-heading">Work in Progress</h2><p class="empty-state">Details of ongoing projects will be posted here.</p></section></main>'''
write('research', 'Research', research, 'Policy research, academic journal publications, and work in progress by Johnson Oliyide, with abstracts and available paper PDFs.')

cv = '''<main id="main" class="page"><h1>Curriculum vitae</h1><button class="print-button" type="button" data-print hidden>Print / Save as PDF</button><section class="cv-section"><h2>Research experience</h2><div class="cv-row"><div class="cv-date">June 2024–present</div><div><h3>Research Associate</h3><p>Economic Research Department<br>Federal Reserve Bank of Kansas City</p></div></div><div class="cv-row"><div class="cv-date">August 2022–May 2024</div><div><h3>Graduate Research Assistant</h3><p>Market Integration Research Lab, University of Maine<br>Professors Thomas Wiesen and Todd Gabe</p></div></div><div class="cv-row"><div class="cv-date">June 2020–August 2022</div><div><h3>Research Assistant</h3><p>Professor Ismail Fasanya<br>School of Economics and Finance, University of the Witwatersrand</p></div></div></section><section class="cv-section"><h2>Professional experience</h2><div class="cv-row"><div class="cv-date">July 2021–April 2022</div><div><h3>Economic Analyst</h3><p>Economic Development and Investment Desk<br>Development Agenda for Western Nigeria Commission</p></div></div></section><section class="cv-section"><h2>Education</h2><div class="cv-row"><div class="cv-date">2022–2024</div><div><h3>M.S. in Economics</h3><p>University of Maine, United States</p></div></div><div class="cv-row"><div class="cv-date">2015–2021</div><div><h3>B.Sc. in Economics</h3><p>Federal University of Agriculture, Abeokuta, Nigeria</p></div></div></section><section class="cv-section"><h2>Publications and policy research</h2><p><a href="../research/">View the complete research list, abstracts, and available PDFs.</a></p></section></main>'''
write('cv', 'CV', cv, 'Education and research experience of Johnson Ayobami Oliyide.')

lab = '''<main id="main" class="page"><h1>Macro Lab</h1><p class="page-intro">Interactive dashboards exploring labor markets and the U.S. economy using publicly available data.</p><article class="tool"><p class="eyebrow">U.S. labor markets</p><h2>U.S. Labor Market Tightness Dashboard</h2><p>Explore labor market tightness using the unemployment gap (u − u*), including uncertainty around the natural unemployment rate and alternative ways to scale the gap.</p><a class="text-link" href="https://johnsonoliyide.github.io/labor-market-dashboard/" target="_blank" rel="noopener noreferrer">Open dashboard ↗</a></article><article class="tool"><p class="eyebrow">U.S. payroll employment</p><h2>U.S. Employment Dynamics Dashboard</h2><p>Track payroll employment growth across major industries and states, including sector contributions, employment shares, and monthly and annual comparisons using Current Employment Statistics data.</p><a class="text-link" href="https://johnsonoliyide.github.io/employment_dynamics_dashboard/" target="_blank" rel="noopener noreferrer">Open dashboard ↗</a></article><article class="tool" id="r-packages"><h2>R Packages</h2><p>Coming soon.</p></article></main>'''
write('macro-lab', 'Macro Lab', lab, 'Interactive U.S. labor market dashboards and research tools by Johnson Oliyide.')
contact = f'''<main id="main" class="page"><p class="eyebrow">Get in touch</p><h1>Contact</h1><p>I welcome conversations about economics and research.</p><p class="email-address"><a href="mailto:{EMAIL}">{EMAIL}</a></p><p class="page-intro">Research Associate<br>Federal Reserve Bank of Kansas City<br>Kansas City, Missouri</p><div class="contact-links">{''.join(external(label + ' ↗', url) for label, url in SOCIAL)}</div></main>'''
write('contact', 'Contact', contact, 'Contact Johnson Ayobami Oliyide.')

for old, target in [('resume', '../cv/'), ('home', '../'), ('about', '../'), ('r-packages', '../macro-lab/#r-packages')]:
    path = ROOT / old
    path.mkdir(exist_ok=True)
    (path / 'index.html').write_text(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta http-equiv="refresh" content="0;url={target}"><title>Johnson Oliyide</title></head><body><a href="{target}">Continue to Johnson Oliyide’s website</a></body></html>')

(ROOT / '404.html').write_text(page('Page not found', '', '<main id="main" class="page"><h1>Page not found</h1><p><a href="/">Return to the homepage.</a></p></main>', 'Page not found.'))
preview = ROOT / 'dist'
preview.mkdir(exist_ok=True)
for name in ['index.html', '404.html', '.nojekyll', 'assets', 'papers', 'research', 'cv', 'macro-lab', 'contact', 'resume', 'home', 'about', 'r-packages']:
    source = ROOT / name
    target = preview / name
    if source.is_dir():
        shutil.copytree(source, target, dirs_exist_ok=True)
    else:
        shutil.copy2(source, target)
print(f'Built five pages and migrated {len(PAPERS)} research entries.')
