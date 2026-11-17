# -*- coding: utf-8 -*-
"""Génère le site statique dans public/.  Usage : python3 tools/build.py"""
import json, os, html, re, shutil, sys
sys.path.insert(0, os.path.dirname(__file__))
import config as C
from content import FAQ, SERVICES, ZONES, OTHER_AREAS, GUIDES

ROOT = os.path.join(os.path.dirname(__file__), "..", "public")
U = C.SITE_URL.rstrip("/")
ORG_ID = U + "/#entreprise"
WEB_ID = U + "/#site"
PAGES = []  # (path, priority, changefreq)

e = html.escape


def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)


def pic(P, name, alt, w=1200, h=800, eager=False, cls=""):
    load = 'fetchpriority="high" decoding="async"' if eager else 'loading="lazy" decoding="async"'
    return (f'<picture class="{cls}"><source srcset="{P}img/{name}.webp" type="image/webp">'
            f'<img src="{P}img/{name}.jpg" alt="{e(alt)}" width="{w}" height="{h}" {load}></picture>')


def ld(obj):
    return f'<script type="application/ld+json">{json.dumps(obj, ensure_ascii=False, separators=(",", ":"))}</script>'


def business_schema():
    days = {"Mo": "Monday", "Tu": "Tuesday", "We": "Wednesday", "Th": "Thursday", "Fr": "Friday", "Sa": "Saturday", "Su": "Sunday"}
    ohs = []
    for d, o, c in C.OPENING_HOURS:
        if "-" in d:
            a, b = d.split("-"); keys = list(days); dl = [days[k] for k in keys[keys.index(a):keys.index(b) + 1]]
        else:
            dl = [days[d]]
        ohs.append({"@type": "OpeningHoursSpecification", "dayOfWeek": dl, "opens": o, "closes": c})
    areas = [{"@type": "City", "name": "Paris"}] + [{"@type": "Place", "name": z["full"]} for z in ZONES] + [{"@type": "Place", "name": a} for a in OTHER_AREAS]
    s = {
        "@context": "https://schema.org", "@type": ["HomeAndConstructionBusiness", "LocalBusiness"], "@id": ORG_ID,
        "name": f"{C.BRAND} — {C.SITE_NAME}", "alternateName": [C.BRAND, C.SITE_NAME],
        "description": "Entreprise spécialisée dans le ponçage, la vitrification, l'huilage et la restauration de parquets anciens (point de Hongrie, bâton rompu, Versailles) à Paris et en Île-de-France.",
        "url": U + "/", "logo": U + "/img/logo.svg", "image": [U + "/img/og-image.jpg", U + "/img/hero-point-de-hongrie.jpg"],
        "telephone": C.PHONE_E164, "email": C.EMAIL, "priceRange": "€€€",
        "currenciesAccepted": "EUR", "paymentAccepted": "Virement, chèque, carte bancaire",
        "address": {"@type": "PostalAddress", "streetAddress": C.STREET, "postalCode": C.POSTAL_CODE, "addressLocality": C.CITY, "addressRegion": "Île-de-France", "addressCountry": "FR"},
        "geo": {"@type": "GeoCoordinates", "latitude": C.GEO[0], "longitude": C.GEO[1]},
        "openingHoursSpecification": ohs, "areaServed": areas,
        "knowsAbout": ["Ponçage de parquet", "Parquet point de Hongrie", "Parquet bâton rompu", "Parquet Versailles", "Vitrification de parquet", "Huilage de parquet", "Cirage de parquet", "Restauration de parquet ancien", "Appartements haussmanniens"],
        "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Prestations parquet", "itemListElement": [
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": s_["name"], "url": f"{U}/{s_['slug']}/"}} for s_ in SERVICES]},
    }
    if C.SAME_AS or C.GOOGLE_BUSINESS_URL:
        s["sameAs"] = [x for x in C.SAME_AS + [C.GOOGLE_BUSINESS_URL] if x]
    return s


def website_schema():
    return {"@context": "https://schema.org", "@type": "WebSite", "@id": WEB_ID, "url": U + "/", "name": f"{C.SITE_NAME} — {C.BRAND}", "inLanguage": "fr-FR", "publisher": {"@id": ORG_ID}}


def breadcrumb_schema(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": U + p} for i, (n, p) in enumerate(items)]}


def faq_schema(ids):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": FAQ[i][0], "acceptedAnswer": {"@type": "Answer", "text": FAQ[i][1]}} for i in ids]}


def service_schema(name, desc, path, area=None):
    return {"@context": "https://schema.org", "@type": "Service", "name": name, "description": desc, "url": U + path,
            "serviceType": "Ponçage et rénovation de parquet", "provider": {"@id": ORG_ID},
            "areaServed": area or [{"@type": "City", "name": "Paris"}, {"@type": "AdministrativeArea", "name": "Île-de-France"}],
            "offers": {"@type": "Offer", "priceCurrency": "EUR", "availability": "https://schema.org/InStock",
                       "priceSpecification": {"@type": "UnitPriceSpecification", "price": C.PRICE_FROM, "priceCurrency": "EUR", "unitCode": "MTK", "unitText": "m²", "valueAddedTaxIncluded": False, "description": "Prix de départ au m²"}}}


# ------------------------------------------------------------------ layout
NAV = [("Prestations", "poncage-parquet/"), ("Tarifs", "tarifs/"), ("Réalisations", "realisations/"),
       ("Zones", "zones-intervention/"), ("Guides", "guides/"), ("FAQ", "faq/")]

LOGO = '''<svg viewBox="0 0 48 48" width="40" height="40" aria-hidden="true"><rect width="48" height="48" rx="6" fill="#1c2333"/><g stroke="#c9a45c" stroke-width="3" fill="none" stroke-linecap="square"><path d="M8 34 16 26 24 34 32 26 40 34"/><path d="M8 24 16 16 24 24 32 16 40 24" opacity=".55"/></g></svg>'''


def head(P, title, desc, path, extra_ld=(), og_img="og-image.jpg", preload=None, noindex=False, otype="website"):
    canon = U + path
    tags = [ld(website_schema()), ld(business_schema())] + [ld(x) for x in extra_ld]
    ga = ""
    if C.GA4_ID:
        ga = f'<script async src="https://www.googletagmanager.com/gtag/js?id={C.GA4_ID}"></script><script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag("js",new Date());gtag("config","{C.GA4_ID}");</script>'
    pre = f'<link rel="preload" as="image" href="{P}img/{preload}.webp" type="image/webp" fetchpriority="high">' if preload else ""
    gsc = f'<meta name="google-site-verification" content="{C.GSC_VERIFICATION}">' if C.GSC_VERIFICATION else ""
    return f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="robots" content="{"noindex,follow" if noindex else "index,follow,max-image-preview:large,max-snippet:-1"}">
<link rel="canonical" href="{canon}">
<meta property="og:type" content="{otype}"><meta property="og:locale" content="fr_FR"><meta property="og:site_name" content="{e(C.SITE_NAME)} — {C.BRAND}">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{canon}">
<meta property="og:image" content="{U}/img/{og_img}"><meta name="twitter:card" content="summary_large_image">
<meta name="geo.region" content="FR-75"><meta name="geo.placename" content="Paris"><meta name="geo.position" content="{C.GEO[0]};{C.GEO[1]}"><meta name="ICBM" content="{C.GEO[0]}, {C.GEO[1]}">
<meta name="theme-color" content="#1c2333">
<link rel="icon" href="{P}img/logo.svg" type="image/svg+xml">
<link rel="stylesheet" href="{P}assets/style.css">
{pre}{gsc}
{chr(10).join(tags)}
{ga}
</head>
<body>
<a class="skip" href="#contenu">Aller au contenu</a>
<header class="hdr"><div class="wrap hdr-in">
<a class="brand" href="{P or './'}" aria-label="{C.BRAND} — {C.SITE_NAME}, accueil">{LOGO}<span><strong>{C.BRAND}</strong><small>Ponçage Parquet Haussmannien</small></span></a>
<button class="burger" aria-expanded="false" aria-controls="nav" aria-label="Menu"><span></span><span></span><span></span></button>
<nav id="nav" class="nav" aria-label="Navigation principale">
{"".join(f'<a href="{P}{h}">{n}</a>' for n, h in NAV)}
<a class="tel" href="tel:{C.PHONE_E164}">☎ {C.PHONE_DISPLAY}</a>
<a class="btn btn-sm" href="{P}devis/">Devis gratuit</a>
</nav></div></header>
<main id="contenu">
'''


def foot(P):
    wa = f'<a class="mb-wa" href="https://wa.me/{C.WHATSAPP_E164}">WhatsApp</a>' if C.WHATSAPP_E164 else ""
    return f'''</main>
<footer class="ftr"><div class="wrap ftr-grid">
<div><p class="ftr-brand">{LOGO}<strong>{C.BRAND} · {C.SITE_NAME}</strong></p>
<p>Spécialiste du ponçage et de la restauration de parquets anciens à Paris et en Île-de-France : point de Hongrie, bâton rompu, Versailles.</p>
<address>{e(C.LEGAL_NAME)}<br>{e(C.STREET)}<br>{C.POSTAL_CODE} {C.CITY}<br><a href="tel:{C.PHONE_E164}">{C.PHONE_DISPLAY}</a><br><a href="mailto:{C.EMAIL}">{C.EMAIL}</a><br>{C.OPENING_HOURS_TEXT}</address></div>
<div><p class="ftr-h">Prestations</p><ul>{"".join(f'<li><a href="{P}{s["slug"]}/">{s["short"]}</a></li>' for s in SERVICES)}<li><a href="{P}tarifs/">Tarifs</a></li></ul></div>
<div><p class="ftr-h">Zones d'intervention</p><ul>{"".join(f'<li><a href="{P}poncage-parquet-{z["slug"]}/">Ponçage parquet {z["name"]}</a></li>' for z in ZONES)}</ul></div>
<div><p class="ftr-h">Ressources</p><ul>{"".join(f'<li><a href="{P}guides/{g["slug"]}/">{g["h1"]}</a></li>' for g in GUIDES)}<li><a href="{P}a-propos/">À propos de {C.BRAND}</a></li><li><a href="{P}faq/">FAQ</a></li><li><a href="{P}mentions-legales/">Mentions légales</a></li><li><a href="{P}confidentialite/">Confidentialité</a></li></ul></div>
</div><p class="wrap copy">© 2026 {e(C.LEGAL_NAME)} — Ponçage, vitrification et restauration de parquets anciens à Paris. Mis à jour le {C.UPDATED_FR}.</p></footer>
<div class="mobilebar"><a href="tel:{C.PHONE_E164}">☎ Appeler</a>{wa}<a class="hl" href="{P}devis/">Devis gratuit</a></div>
<script src="{P}assets/app.js" defer></script>
</body></html>'''


def crumbs(P, items):
    out = []
    for i, (n, p) in enumerate(items):
        if i < len(items) - 1:
            out.append(f'<a href="{P}{p.lstrip("/")}">{e(n)}</a>' if p != "/" else f'<a href="{P or "./"}">{e(n)}</a>')
        else:
            out.append(f'<span aria-current="page">{e(n)}</span>')
    return f'<nav class="crumbs wrap" aria-label="Fil d\'Ariane">{" › ".join(out)}</nav>'


def faq_html(ids, h="Questions fréquentes"):
    items = "".join(f'<details><summary>{e(FAQ[i][0])}</summary><p>{e(FAQ[i][1])}</p></details>' for i in ids)
    return f'<section class="sec"><div class="wrap narrow"><h2>{h}</h2><div class="faq">{items}</div></div></section>'


def tarif_table():
    rows = "".join(f'<tr><td>{e(a)}</td><td class="pr">{e(b)}</td><td>{e(c)}</td></tr>' for a, b, c in C.TARIFS)
    return f'<div class="tblwrap"><table class="table"><thead><tr><th>Prestation</th><th>Tarif</th><th>Inclus</th></tr></thead><tbody>{rows}</tbody></table></div><p class="note">{e(C.PRICE_NOTE)}</p>'


def trust_strip():
    items = [("Devis gratuit sous 24 h", "Visite ou estimation sur photos"), ("Ponçage aspiré", "Poussière captée à la source"),
             ("Spécialistes du parquet ancien", "Point de Hongrie, bâton rompu, Versailles"), ("Assurance décennale", "Attestation fournie avec le devis"),
             ("Produits à faible COV", "Vitrificateurs en phase aqueuse"), ("Devis ligne par ligne", "Aucun frais caché")]
    return '<ul class="trust">' + "".join(f'<li><strong>{a}</strong><span>{b}</span></li>' for a, b in items) + "</ul>"


def calculator():
    return f'''<div class="calc" data-price="{C.PRICE_FROM}"><p class="calc-h">Estimez votre budget</p>
<label for="calc-m2">Surface à poncer : <output id="calc-out">40</output> m²</label>
<input id="calc-m2" type="range" min="10" max="200" step="5" value="40">
<label for="calc-fin">Finition</label><select id="calc-fin"><option value="70">Vitrification (dès 70 €/m²)</option><option value="75">Huile (dès 75 €/m²)</option><option value="85">Cire naturelle (dès 85 €/m²)</option></select>
<label class="chk"><input type="checkbox" id="calc-teinte"> Teinte (+12 €/m²)</label>
<label class="chk"><input type="checkbox" id="calc-joints"> Rebouchage des joints (+8 €/m²)</label>
<p class="calc-res">À partir de <strong id="calc-res">2 800 €</strong> HT</p>
<p class="note">Estimation indicative. Prix ferme après diagnostic gratuit.</p></div>'''


def cta_band(P):
    return f'''<section class="cta-band"><div class="wrap cta-in"><div><h2>Votre parquet mérite un spécialiste</h2><p>Devis gratuit et détaillé sous 24 h ouvrées. Déplacement offert à Paris et en proche banlieue.</p></div>
<div class="cta-btns"><a class="btn btn-gold" href="{P}devis/">Demander mon devis</a><a class="btn btn-ghost" href="tel:{C.PHONE_E164}">☎ {C.PHONE_DISPLAY}</a></div></div></section>'''


def form_html(P):
    action = C.FORM_ENDPOINT or f"{P}merci/"
    return f'''<form class="form" name="devis" method="POST" action="{action}" data-netlify="true" netlify-honeypot="societe" enctype="multipart/form-data">
<input type="hidden" name="form-name" value="devis">
<p class="hp"><label>Ne pas remplir : <input name="societe" tabindex="-1" autocomplete="off"></label></p>
<div class="row"><label>Nom et prénom*<input name="nom" required autocomplete="name"></label><label>Téléphone*<input name="telephone" type="tel" required autocomplete="tel" pattern="[0-9 +().-]{{10,}}"></label></div>
<div class="row"><label>E-mail*<input name="email" type="email" required autocomplete="email"></label><label>Code postal du chantier*<input name="code_postal" required inputmode="numeric" pattern="[0-9]{{5}}" autocomplete="postal-code"></label></div>
<div class="row"><label>Surface approximative*<select name="surface" required><option value="">Choisir…</option><option>Moins de 20 m²</option><option>20 à 40 m²</option><option>40 à 70 m²</option><option>70 à 120 m²</option><option>Plus de 120 m²</option></select></label>
<label>Type de parquet<select name="type_parquet"><option>Point de Hongrie</option><option>Bâton rompu</option><option>Versailles / panneaux</option><option>À l'anglaise (lames droites)</option><option>Je ne sais pas</option></select></label></div>
<div class="row"><label>Prestation souhaitée<select name="prestation"><option>Ponçage + vitrification</option><option>Ponçage + huile</option><option>Ponçage + cire</option><option>Réparation / remplacement de lames</option><option>Je souhaite un conseil</option></select></label>
<label>Délai souhaité<select name="delai"><option>Dès que possible</option><option>Dans le mois</option><option>Dans 1 à 3 mois</option><option>Plus tard / projet d'achat</option></select></label></div>
<label>Votre projet<textarea name="message" rows="4" placeholder="Étage, ascenseur, état du parquet, pièces concernées…"></textarea></label>
<label>Photos du parquet (facultatif, accélère le devis)<input type="file" name="photos" accept="image/*" multiple></label>
<label class="chk"><input type="checkbox" name="budget_ok" value="oui"> J'ai noté que les prestations débutent à {C.PRICE_FROM} €/m².</label>
<label class="chk"><input type="checkbox" name="rgpd" required> J'accepte que mes données soient utilisées pour être recontacté au sujet de ma demande (<a href="{P}confidentialite/">politique de confidentialité</a>).*</label>
<button class="btn btn-gold btn-lg" type="submit">Recevoir mon devis gratuit</button>
<p class="note">Réponse sous 24 h ouvrées. Vos données ne sont jamais revendues.</p>
</form>'''


def page(path, depth, title, desc, body, extra_ld=(), crumb=None, priority="0.7", freq="monthly", preload=None, noindex=False, otype="website"):
    P = "../" * depth
    b = crumbs(P, crumb) if crumb else ""
    lds = list(extra_ld) + ([breadcrumb_schema(crumb)] if crumb else [])
    out = head(P, title, desc, path, lds, preload=preload, noindex=noindex, otype=otype) + b + body.replace("{P}", P) + foot(P)
    write((path.strip("/") + "/index.html") if path != "/" else "index.html", out)
    if not noindex:
        PAGES.append((path, priority, freq))


def hero(P, h1, lead, img, tldr=None, small=False):
    t = f'<p class="tldr"><strong>En bref :</strong> {tldr}</p>' if tldr else ""
    return f'''<section class="hero {'hero-sm' if small else ''}">{pic(P, img, h1, 1600, 1000, eager=True, cls="hero-bg")}<div class="wrap hero-in">
<h1>{h1}</h1><p class="lead">{lead}</p>{t}
<div class="hero-ctas"><a class="btn btn-gold btn-lg" href="{P}devis/">Devis gratuit sous 24 h</a><a class="btn btn-ghost" href="tel:{C.PHONE_E164}">☎ {C.PHONE_DISPLAY}</a></div>
<p class="hero-price">À partir de <strong>{C.PRICE_FROM} €/m²</strong> · Paris & Île-de-France</p></div></section>'''


def service_cards(P, exclude=None):
    cards = "".join(f'''<a class="card" href="{P}{s['slug']}/">{pic(P, s['img'], s['name'], cls="card-img")}<div class="card-b"><h3>{s['name']}</h3><p>{e(s['desc'][:150].rsplit(' ', 1)[0])}…</p><span class="more">En savoir plus →</span></div></a>'''
                    for s in SERVICES if s["slug"] != exclude)
    return f'<div class="cards">{cards}</div>'


def before_after(P):
    return f'''<div class="ba" style="--pos:50%"><div class="ba-img">{pic(P, "apres-point-de-hongrie", "Parquet point de Hongrie après ponçage et finition", 1600, 1000)}</div>
<div class="ba-img ba-before">{pic(P, "avant-point-de-hongrie", "Parquet point de Hongrie grisé et rayé avant ponçage", 1600, 1000)}</div>
<span class="ba-l">Avant</span><span class="ba-r">Après</span><input class="ba-range" type="range" min="0" max="100" value="50" aria-label="Comparer avant et après ponçage"></div>'''


def method_steps():
    st = [("Diagnostic gratuit", "Mesure, épaisseur d'usure, état des lames et conseils de finition."),
          ("Devis détaillé sous 24 h", "Chaque poste chiffré : ponçage, finition, options, réparations."),
          ("Protection du chantier", "Parties communes, portes, plinthes et pièces voisines protégées."),
          ("Ponçage 3 passes aspiré", "Grains progressifs en diagonale du motif, bordures et angles à la main."),
          ("Finition multicouche", "Vitrificateur, huile ou cire appliqués avec égrenage entre couches."),
          ("Réception avec vous", "Contrôle en lumière rasante et remise du guide d'entretien.")]
    return '<ol class="method">' + "".join(f'<li><strong>{a}</strong><span>{b}</span></li>' for a, b in st) + "</ol>"


# ------------------------------------------------------------------ PAGES
def build_home():
    P = ""
    zones = "".join(f'<li><a href="poncage-parquet-{z["slug"]}/">{z["name"]}</a></li>' for z in ZONES)
    howto = {"@context": "https://schema.org", "@type": "HowTo", "name": "Comment SGE rénove un parquet haussmannien",
             "step": [{"@type": "HowToStep", "position": i + 1, "name": n} for i, n in enumerate(["Diagnostic gratuit", "Devis détaillé", "Protection du chantier", "Ponçage 3 passes aspiré", "Finition multicouche", "Réception"])]}
    body = hero(P, "Ponçage de parquet haussmannien à Paris",
                "Point de Hongrie, bâton rompu, parquet Versailles : SGE redonne à vos parquets anciens leur éclat d'origine, avec la méthode et le soin qu'exige un bois centenaire.",
                "hero-point-de-hongrie",
                tldr=f"SGE est une entreprise spécialisée dans le ponçage, la vitrification et la restauration de parquets anciens dans les appartements haussmanniens de Paris et de l'ouest parisien. Tarifs à partir de {C.PRICE_FROM} €/m², devis gratuit sous 24 h.")
    body += f'''<section class="sec sec-tight"><div class="wrap">{trust_strip()}</div></section>
<section class="sec"><div class="wrap"><p class="kicker">Nos prestations</p><h2>Tout pour sublimer un parquet ancien</h2>
<p class="sub">Du simple ponçage à la restauration complète d'un parquet Versailles, nous maîtrisons chaque étape.</p>{service_cards(P)}</div></section>
<section class="sec sec-alt"><div class="wrap split"><div><p class="kicker">Le résultat</p><h2>Du parquet grisé au chêne lumineux</h2>
<p>Faites glisser le curseur pour comparer. Un ponçage en trois passes suivi d'une finition adaptée suffit à révéler la beauté du chêne et le dessin des chevrons, même sur un parquet très encrassé.</p>
<ul class="checks"><li>Rayures, taches grises et ancien vernis jaune éliminés</li><li>Joints rebouchés, lames abîmées remplacées</li><li>Finition mate « bois brut », huilée ou cirée</li></ul>
<a class="btn" href="realisations/">Voir nos réalisations</a></div>{before_after(P)}</div></section>
<section class="sec"><div class="wrap split split-rev"><div>{pic(P, "baton-rompu", "Parquet en bâton rompu ancien rénové", cls="rounded")}</div><div>
<p class="kicker">Notre expertise</p><h2>Pourquoi un parquet haussmannien demande un spécialiste</h2>
<p>Les parquets des immeubles parisiens construits entre 1850 et 1914 sont en chêne massif cloué sur lambourdes, posés en motifs dont le fil change de direction tous les quarante centimètres. Un ponçage standard, mené dans le sens de la pièce, y laisse des marques de disque, des fibres arrachées et des creux dans les passages.</p>
<p>Chez SGE, nous ponçons en diagonale du motif, en trois grains, et terminons chaque pièce à la monobrosse. Nous mesurons l'épaisseur d'usure avant d'intervenir pour ne retirer que le strict nécessaire : votre parquet pourra encore être rénové par les générations suivantes.</p>
<a class="btn btn-outline" href="poncage-parquet/">Notre méthode de ponçage</a></div></div></section>
<section class="sec sec-dark"><div class="wrap"><p class="kicker">Méthode</p><h2>Un chantier propre, organisé, sans surprise</h2>{method_steps()}</div></section>
<section class="sec"><div class="wrap split"><div><p class="kicker">Tarifs transparents</p><h2>À partir de {C.PRICE_FROM} €/m², sans frais cachés</h2>
<p>Notre prix comprend un vrai ponçage en trois passes, les bordures et angles réalisés à la main, la protection du chantier et une finition professionnelle en trois couches. Les options sont chiffrées séparément, ligne par ligne.</p>
<a class="btn" href="tarifs/">Voir la grille complète</a></div>{calculator()}</div></section>
<section class="sec sec-alt"><div class="wrap"><p class="kicker">Avis clients</p><h2>Ils nous ont confié leur parquet</h2>
<div class="reviews-cta"><p>Consultez les avis de nos clients sur Google et partagez le vôtre après votre chantier.</p>{f'<a class="btn btn-outline" href="{C.GOOGLE_BUSINESS_URL}" rel="noopener" target="_blank">Lire les avis Google</a>' if C.GOOGLE_BUSINESS_URL else '<!-- Ajoutez GOOGLE_BUSINESS_URL dans tools/config.py pour afficher le bouton vers vos avis Google -->'}</div></div></section>
<section class="sec"><div class="wrap"><p class="kicker">Zones d'intervention</p><h2>Paris et ouest parisien</h2>
<p class="sub">Nous intervenons dans tous les arrondissements de Paris et dans les communes des Hauts-de-Seine et des Yvelines au riche patrimoine ancien.</p>
<ul class="zones">{zones}<li><a href="zones-intervention/">Toutes les zones →</a></li></ul></div></section>
{faq_html([0, 1, 2, 3, 4, 8])}
<section class="sec sec-alt" id="devis"><div class="wrap split"><div><p class="kicker">Devis gratuit</p><h2>Parlez-nous de votre parquet</h2>
<p>Décrivez votre projet et joignez quelques photos : nous revenons vers vous sous 24 h ouvrées avec une première estimation, puis fixons une visite gratuite.</p>
<ul class="checks"><li>Sans engagement</li><li>Visite et métré offerts à Paris et proche banlieue</li><li>Devis détaillé, valable 3 mois</li></ul>
<p class="contact-direct">Ou appelez-nous : <a href="tel:{C.PHONE_E164}">{C.PHONE_DISPLAY}</a><br><small>{C.OPENING_HOURS_TEXT}</small></p></div>{form_html(P)}</div></section>'''
    page("/", 0, f"Ponçage parquet haussmannien Paris — point de Hongrie dès {C.PRICE_FROM} €/m² | {C.BRAND}",
         f"Spécialiste du ponçage de parquet ancien à Paris : point de Hongrie, bâton rompu, Versailles. Ponçage aspiré, vitrification, huile, cire. Devis gratuit 24 h, dès {C.PRICE_FROM} €/m².",
         body, [faq_schema([0, 1, 2, 3, 4, 8]), howto], priority="1.0", freq="weekly", preload="hero-point-de-hongrie")


def build_services():
    for s in SERVICES:
        P = "../"
        path = f"/{s['slug']}/"
        body = hero(P, s["h1"], s["lead"], s["img"], tldr=s["tldr"], small=True)
        side = f'''<aside class="side"><div class="side-box"><p class="side-h">Devis gratuit</p><p>Réponse sous 24 h ouvrées</p><a class="btn btn-gold" href="{P}devis/">Demander un devis</a><a class="btn btn-ghost-dark" href="tel:{C.PHONE_E164}">☎ {C.PHONE_DISPLAY}</a><p class="side-price">Dès <strong>{C.PRICE_FROM} €/m²</strong></p></div>
<div class="side-box"><p class="side-h">Nos prestations</p><ul>{"".join(f'<li><a href="{P}{x["slug"]}/">{x["short"]}</a></li>' for x in SERVICES)}</ul></div></aside>'''
        body += f'<section class="sec"><div class="wrap with-side"><article class="prose">{s["body"]}<p class="updated">Mis à jour le {C.UPDATED_FR}</p></article>{side}</div></section>'
        body += faq_html(s["faq"])
        body += f'<section class="sec sec-alt"><div class="wrap"><h2>Nos autres prestations</h2>{service_cards(P, exclude=s["slug"])}</div></section>'
        body += cta_band(P)
        page(path, 1, s["title"], s["desc"], body, [service_schema(s["name"], s["desc"], path), faq_schema(s["faq"])],
             crumb=[("Accueil", "/"), (s["short"], path)], priority="0.9", preload=s["img"])


def build_zones():
    for i, z in enumerate(ZONES):
        P = "../"
        path = f"/poncage-parquet-{z['slug']}/"
        imgs = ["hero-point-de-hongrie", "baton-rompu", "parquet-versailles", "apres-point-de-hongrie", "vitrification-mat", "huilage-cire"]
        img = imgs[i % len(imgs)]
        others = "".join(f'<li><a href="{P}poncage-parquet-{o["slug"]}/">{o["name"]}</a></li>' for o in ZONES if o is not z)
        h1 = f"Ponçage de parquet à {z['name']}" if not z["name"].startswith("Paris") else f"Ponçage de parquet {z['name']}"
        body = hero(P, h1, z["intro"], img, tldr=f"SGE ponce, vitrifie, huile et restaure les parquets anciens à {z['full']} ({z['cp']}). Tarifs à partir de {C.PRICE_FROM} €/m², déplacement et devis gratuits, réponse sous 24 h.", small=True)
        body += f'''<section class="sec"><div class="wrap with-side"><article class="prose">
<h2>Votre spécialiste du parquet ancien à {z['name']}</h2>{z['body']}
<h2>Nos prestations à {z['name']}</h2><ul class="checks">{"".join(f'<li><a href="{P}{s["slug"]}/">{s["name"]}</a></li>' for s in SERVICES)}</ul>
<h2>Comment se déroule une intervention à {z['name']} ?</h2>{method_steps()}
<h2>Tarifs à {z['name']}</h2><p>Nos tarifs sont identiques dans toute notre zone d'intervention : ponçage + vitrification <strong>à partir de {C.PRICE_FROM} €/m²</strong>, sans frais de déplacement pour le diagnostic.</p>{tarif_table()}
<p class="updated">Mis à jour le {C.UPDATED_FR}</p></article>
<aside class="side"><div class="side-box"><p class="side-h">Devis gratuit à {z['name']}</p><a class="btn btn-gold" href="{P}devis/">Demander un devis</a><a class="btn btn-ghost-dark" href="tel:{C.PHONE_E164}">☎ {C.PHONE_DISPLAY}</a></div>
<div class="side-box"><p class="side-h">Autres secteurs</p><ul>{others}</ul></div></aside></div></section>'''
        body += faq_html([0, 6, 1]) + cta_band(P)
        area = [{"@type": "Place", "name": z["full"], "address": {"@type": "PostalAddress", "postalCode": z["cp"], "addressCountry": "FR"}}]
        page(path, 1, f"Ponçage parquet {z['name']} — dès {C.PRICE_FROM} €/m² | {C.BRAND}",
             f"Ponçage et rénovation de parquet ancien à {z['name']} : point de Hongrie, bâton rompu, Versailles. Devis gratuit sous 24 h, dès {C.PRICE_FROM} €/m².",
             body, [service_schema(f"Ponçage de parquet à {z['name']}", z["intro"], path, area), faq_schema([0, 6, 1])],
             crumb=[("Accueil", "/"), ("Zones d'intervention", "/zones-intervention/"), (z["name"], path)], priority="0.8", preload=img)
    # hub
    P = "../"
    lst = "".join(f'<a class="zone-card" href="{P}poncage-parquet-{z["slug"]}/"><strong>{z["name"]}</strong><span>{z["cp"]}</span></a>' for z in ZONES)
    body = hero(P, "Zones d'intervention", "Nous rénovons les parquets anciens dans tout Paris, dans les Hauts-de-Seine et dans les Yvelines.", "parquet-versailles", small=True)
    body += f'''<section class="sec"><div class="wrap"><h2>Nos secteurs principaux</h2><div class="zone-grid">{lst}</div>
<h2>Nous intervenons aussi à</h2><p>{", ".join(OTHER_AREAS)} et dans toutes les communes limitrophes de Paris. Vous ne voyez pas votre ville ? <a href="{P}devis/">Contactez-nous</a>.</p></div></section>''' + cta_band(P)
    page("/zones-intervention/", 1, f"Zones d'intervention — ponçage de parquet Paris & Île-de-France | {C.BRAND}",
         "SGE intervient pour le ponçage et la rénovation de parquets anciens dans tout Paris, à Neuilly, Boulogne, Levallois, Versailles, Saint-Germain-en-Laye et alentours.",
         body, crumb=[("Accueil", "/"), ("Zones d'intervention", "/zones-intervention/")], priority="0.7")


def build_guides():
    for g in GUIDES:
        P = "../../"
        path = f"/guides/{g['slug']}/"
        b = g["body"].replace("{TARIF_TABLE}", tarif_table())
        body = f'''<article class="sec"><div class="wrap narrow prose"><header class="art-h"><p class="kicker">Guide</p><h1>{g['h1']}</h1>
<p class="meta">Par l'équipe {C.BRAND} · Mis à jour le <time datetime="{C.UPDATED}">{C.UPDATED_FR}</time></p></header>
<p class="tldr"><strong>En bref :</strong> {g['tldr']}</p>{pic(P, g['img'], g['h1'], cls="rounded")}{b}</div></article>'''
        body += faq_html(g["faq"]) + cta_band(P)
        art = {"@context": "https://schema.org", "@type": "Article", "headline": g["h1"], "description": g["desc"], "inLanguage": "fr-FR",
               "image": f"{U}/img/{g['img']}.jpg", "datePublished": C.UPDATED, "dateModified": C.UPDATED,
               "author": {"@type": "Organization", "@id": ORG_ID, "name": f"{C.BRAND} — {C.SITE_NAME}"}, "publisher": {"@id": ORG_ID},
               "mainEntityOfPage": U + path}
        page(path, 2, f"{g['title']} | {C.BRAND}", g["desc"], body, [art, faq_schema(g["faq"])],
             crumb=[("Accueil", "/"), ("Guides", "/guides/"), (g["h1"], path)], priority="0.7", otype="article")
    P = "../"
    cards = "".join(f'<a class="card" href="{P}guides/{g["slug"]}/">{pic(P, g["img"], g["h1"], cls="card-img")}<div class="card-b"><h3>{g["h1"]}</h3><p>{e(g["desc"])}</p><span class="more">Lire le guide →</span></div></a>' for g in GUIDES)
    body = hero(P, "Guides et conseils parquet", "Prix, finitions, motifs, entretien : les réponses d'un spécialiste du parquet ancien.", "parquet-anglaise", small=True)
    body += f'<section class="sec"><div class="wrap"><div class="cards">{cards}</div></div></section>' + cta_band(P)
    page("/guides/", 1, f"Guides parquet ancien : prix, finitions, entretien | {C.BRAND}",
         "Nos guides pour comprendre le ponçage, la vitrification et la rénovation des parquets anciens : prix 2026, point de Hongrie, finitions, préparation du chantier.",
         body, crumb=[("Accueil", "/"), ("Guides", "/guides/")], priority="0.6")


def build_misc():
    P = "../"
    # Tarifs
    body = hero(P, "Tarifs du ponçage de parquet", f"Des prix clairs, à partir de {C.PRICE_FROM} €/m², pour un travail de spécialiste.", "vitrification-mat",
                tldr=f"Ponçage + vitrification 3 couches dès {C.PRICE_FROM} €/m² ; ponçage + huile dès 75 €/m² ; ponçage + cire dès 85 €/m². Options teinte et joints chiffrées séparément.", small=True)
    body += f'''<section class="sec"><div class="wrap split"><div class="prose"><h2>Grille tarifaire {C.UPDATED[:4]}</h2>{tarif_table()}
<h2>Ce que comprend notre prix</h2><ul class="checks"><li>Déplacement, diagnostic et métré gratuits</li><li>Protection des parties communes et des pièces voisines</li><li>Ponçage 3 passes, bordures et angles</li><li>Aspiration complète avant chaque couche</li><li>Finition professionnelle 3 couches</li><li>Nettoyage de fin de chantier</li></ul>
<h2>Pourquoi nous ne sommes pas les moins chers</h2><p>Un ponçage haut de gamme se reconnaît à ce qui ne se voit pas sur un devis bas de gamme : un grain de plus, des angles finis à la main, un vitrificateur bi-composant au lieu d'un mono-composant, du temps de séchage respecté. Sur un parquet centenaire, c'est la différence entre un sol qui dure dix ans et un sol à reprendre au bout de deux. Plus de détails dans notre <a href="{P}guides/prix-poncage-parquet-paris/">guide des prix</a>.</p></div>{calculator()}</div></section>'''
    body += faq_html([0, 1]) + cta_band(P)
    offers = {"@context": "https://schema.org", "@type": "OfferCatalog", "name": "Tarifs ponçage de parquet SGE", "itemListElement": [
        {"@type": "Offer", "name": a, "description": c, "priceCurrency": "EUR", **({"price": int(re.search(r"\d+", b).group())} if re.search(r"\d+", b) else {}), "seller": {"@id": ORG_ID}} for a, b, c in C.TARIFS]}
    page("/tarifs/", 1, f"Tarifs ponçage parquet Paris {C.UPDATED[:4]} — dès {C.PRICE_FROM} €/m² | {C.BRAND}",
         f"Prix du ponçage, de la vitrification, de l'huilage et du cirage de parquet ancien à Paris : grille détaillée, simulateur, dès {C.PRICE_FROM} €/m². Devis gratuit.",
         body, [offers, faq_schema([0, 1])], crumb=[("Accueil", "/"), ("Tarifs", "/tarifs/")], priority="0.9")

    # Réalisations
    items = [("hero-point-de-hongrie", "Point de Hongrie — vitrification extra-mat", "Paris 8e · 45 m²"),
             ("baton-rompu", "Bâton rompu — ponçage et vitrification", "Paris 17e · 60 m²"),
             ("parquet-versailles", "Panneaux Versailles — restauration et cire", "Paris 7e · 38 m²"),
             ("teinte-chene-fonce", "Point de Hongrie teinté chêne foncé", "Neuilly-sur-Seine · 72 m²"),
             ("parquet-anglaise", "Parquet à l'anglaise — ponçage et huile", "Boulogne-Billancourt · 55 m²"),
             ("huilage-cire", "Bâton rompu — huile-cire naturelle", "Paris 16e · 40 m²")]
    g = "".join(f'<figure class="gal">{pic(P, i, t)}<figcaption><strong>{t}</strong><span>{l}</span></figcaption></figure>' for i, t, l in items)
    body = hero(P, "Nos réalisations", "Quelques exemples de parquets anciens poncés, réparés et sublimés par nos équipes.", "apres-point-de-hongrie", small=True)
    body += f'<section class="sec"><div class="wrap"><div class="split">{before_after(P)}<div><h2>Avant / après</h2><p>Faites glisser le curseur pour comparer un point de Hongrie avant et après ponçage et finition.</p></div></div><div class="gallery">{g}</div><p class="note">Visuels d\'illustration — <!-- REMPLACEZ ces images par les photos de vos propres chantiers (avant/après) dans public/img/ -->photos de chantiers à venir.</p></div></section>' + cta_band(P)
    page("/realisations/", 1, f"Réalisations — parquets anciens rénovés à Paris | {C.BRAND}",
         "Découvrez nos réalisations de ponçage et de restauration de parquets anciens à Paris : point de Hongrie, bâton rompu, Versailles, avant/après.",
         body, crumb=[("Accueil", "/"), ("Réalisations", "/realisations/")], priority="0.6")

    # FAQ
    body = hero(P, "Questions fréquentes", "Tout ce qu'il faut savoir avant de faire poncer un parquet ancien.", "parquet-anglaise", small=True)
    body += faq_html(range(len(FAQ)), h="Vos questions, nos réponses") + cta_band(P)
    page("/faq/", 1, f"FAQ ponçage de parquet ancien : prix, délais, poussière | {C.BRAND}",
         "Prix, durée des travaux, poussière, finitions, nombre de ponçages possibles : les réponses à vos questions sur le ponçage de parquet ancien à Paris.",
         body, [faq_schema(range(len(FAQ)))], crumb=[("Accueil", "/"), ("FAQ", "/faq/")], priority="0.7")

    # Devis
    body = f'''<section class="sec"><div class="wrap split"><div><p class="kicker">Devis gratuit</p><h1>Demandez votre devis de ponçage de parquet</h1>
<p class="lead-dark">Réponse sous 24 h ouvrées. Joignez quelques photos pour une première estimation encore plus rapide.</p>
<ul class="checks"><li>Diagnostic et métré gratuits à domicile</li><li>Devis détaillé ligne par ligne</li><li>Prestations à partir de {C.PRICE_FROM} €/m²</li><li>Intervention sous 2 à 4 semaines selon planning</li></ul>
{calculator()}<p class="contact-direct">Par téléphone : <a href="tel:{C.PHONE_E164}">{C.PHONE_DISPLAY}</a><br>Par e-mail : <a href="mailto:{C.EMAIL}">{C.EMAIL}</a><br><small>{C.OPENING_HOURS_TEXT}</small></p></div>{form_html(P)}</div></section>'''
    contact = {"@context": "https://schema.org", "@type": "ContactPage", "name": "Devis ponçage de parquet", "url": U + "/devis/", "about": {"@id": ORG_ID}}
    page("/devis/", 1, f"Devis gratuit ponçage de parquet à Paris — réponse 24 h | {C.BRAND}",
         f"Demandez votre devis gratuit de ponçage, vitrification ou restauration de parquet ancien à Paris. Réponse sous 24 h, diagnostic offert, dès {C.PRICE_FROM} €/m².",
         body, [contact], crumb=[("Accueil", "/"), ("Devis gratuit", "/devis/")], priority="0.9")

    # Merci
    body = f'<section class="sec"><div class="wrap narrow center"><h1>Merci, votre demande est bien envoyée</h1><p class="lead-dark">Nous vous recontactons sous 24 h ouvrées. Pour une urgence : <a href="tel:{C.PHONE_E164}">{C.PHONE_DISPLAY}</a>.</p><p><a class="btn" href="{P}guides/preparer-logement-poncage-parquet/">Préparer mon logement</a></p></div></section>'
    page("/merci/", 1, f"Demande envoyée | {C.BRAND}", "Votre demande de devis a bien été envoyée.", body, noindex=True)

    # À propos (E-E-A-T)
    body = hero(P, f"À propos de {C.BRAND}", "Une entreprise dédiée au parquet ancien, à son histoire et à sa transmission.", "huilage-cire", small=True)
    body += f'''<section class="sec"><div class="wrap narrow prose"><h2>Notre spécialité : le parquet ancien</h2>
<p>{C.BRAND} est une entreprise de rénovation spécialisée dans le ponçage, la vitrification, l'huilage et la restauration des parquets anciens des appartements parisiens. Nous avons fait le choix de nous concentrer sur ces sols de chêne massif — point de Hongrie, bâton rompu, panneaux Versailles — qui demandent un savoir-faire spécifique.</p>
<h2>Nos engagements</h2><ul class="checks"><li>Un interlocuteur unique, du devis à la réception</li><li>Des devis détaillés et des prix fermes</li><li>Un chantier protégé, aspiré et rendu propre</li><li>Des produits professionnels à faible émission de COV</li><li>Le respect des règles de copropriété et du voisinage</li><li>Une assurance responsabilité civile et décennale ({e(C.INSURER)})</li></ul>
<h2>Informations légales</h2><p>{e(C.LEGAL_NAME)} — SIRET {e(C.SIRET)} — {e(C.RCS)}<br>Dirigeant : {e(C.DIRECTOR)}<br>{e(C.STREET)}, {C.POSTAL_CODE} {C.CITY}</p></div></section>''' + cta_band(P)
    about = {"@context": "https://schema.org", "@type": "AboutPage", "url": U + "/a-propos/", "about": {"@id": ORG_ID}}
    page("/a-propos/", 1, f"À propos — {C.BRAND}, spécialiste du parquet ancien à Paris", "Découvrez SGE, entreprise spécialisée dans le ponçage et la restauration de parquets anciens à Paris : savoir-faire, engagements, assurances.",
         body, [about], crumb=[("Accueil", "/"), ("À propos", "/a-propos/")], priority="0.5")

    # Mentions légales
    body = f'''<section class="sec"><div class="wrap narrow prose"><h1>Mentions légales</h1>
<h2>Éditeur du site</h2><p>{e(C.LEGAL_NAME)}<br>{e(C.STREET)}, {C.POSTAL_CODE} {C.CITY}<br>SIRET : {e(C.SIRET)} — {e(C.RCS)}<br>Directeur de la publication : {e(C.DIRECTOR)}<br>Téléphone : {C.PHONE_DISPLAY} — E-mail : {C.EMAIL}</p>
<h2>Hébergement</h2><p>{e(C.HOST_NAME)}</p>
<h2>Assurance professionnelle</h2><p>{e(C.INSURER)}</p>
<h2>Propriété intellectuelle</h2><p>L'ensemble des contenus de ce site (textes, visuels, logo) est la propriété de {e(C.LEGAL_NAME)}. Toute reproduction sans autorisation est interdite.</p>
<h2>Médiation de la consommation</h2><p>Conformément à l'article L.612-1 du Code de la consommation, le client consommateur peut recourir gratuitement à un médiateur de la consommation : <!-- À COMPLÉTER -->coordonnées du médiateur à compléter.</p></div></section>'''
    page("/mentions-legales/", 1, f"Mentions légales | {C.BRAND}", "Mentions légales du site Ponçage Parquet Haussmannien — SGE.", body, noindex=True)

    body = f'''<section class="sec"><div class="wrap narrow prose"><h1>Politique de confidentialité</h1>
<p>Les informations transmises via le formulaire de devis (nom, téléphone, e-mail, code postal, description du projet, photos) sont utilisées par {e(C.LEGAL_NAME)} uniquement pour répondre à votre demande et, le cas échéant, établir et suivre votre devis. Base légale : mesures précontractuelles prises à votre demande.</p>
<p>Elles sont conservées 3 ans à compter du dernier contact, puis supprimées. Elles ne sont ni vendues ni cédées. Elles peuvent être hébergées par notre prestataire d'hébergement et de formulaire ({e(C.HOST_NAME.split(' — ')[0])}).</p>
<p>Vous disposez d'un droit d'accès, de rectification, d'effacement, de limitation et d'opposition : écrivez à <a href="mailto:{C.EMAIL}">{C.EMAIL}</a>. Vous pouvez également saisir la CNIL (www.cnil.fr).</p>
<p>{"Ce site utilise Google Analytics pour mesurer l'audience." if C.GA4_ID else "Ce site n'utilise aucun cookie de suivi ni outil de mesure d'audience tiers."}</p></div></section>'''
    page("/confidentialite/", 1, f"Politique de confidentialité | {C.BRAND}", "Politique de confidentialité et de protection des données personnelles.", body, noindex=True)


def build_404():
    P = "/"
    out = head(P, f"Page introuvable | {C.BRAND}", "Cette page n'existe pas.", "/404", noindex=True) + f'<section class="sec"><div class="wrap narrow center"><h1>Page introuvable</h1><p>La page demandée n\'existe pas ou a été déplacée.</p><p><a class="btn" href="/">Retour à l\'accueil</a> <a class="btn btn-outline" href="/devis/">Demander un devis</a></p></div></section>' + foot(P)
    write("404.html", out)


def build_seo_files():
    urls = "".join(f"<url><loc>{U}{p}</loc><lastmod>{C.UPDATED}</lastmod><changefreq>{f}</changefreq><priority>{pr}</priority></url>" for p, pr, f in PAGES)
    write("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    write("robots.txt", f"""User-agent: *
Allow: /
Disallow: /merci/

# Moteurs de réponse IA : autorisés (GEO)
User-agent: GPTBot
Allow: /
User-agent: OAI-SearchBot
Allow: /
User-agent: ChatGPT-User
Allow: /
User-agent: ClaudeBot
Allow: /
User-agent: Claude-SearchBot
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: Google-Extended
Allow: /
User-agent: Applebot-Extended
Allow: /

Sitemap: {U}/sitemap.xml
""")
    svc = "\n".join(f"- [{s['name']}]({U}/{s['slug']}/): {s['tldr']}" for s in SERVICES)
    zn = "\n".join(f"- [Ponçage parquet {z['name']}]({U}/poncage-parquet-{z['slug']}/)" for z in ZONES)
    gd = "\n".join(f"- [{g['h1']}]({U}/guides/{g['slug']}/): {g['tldr']}" for g in GUIDES)
    tf = "\n".join(f"- {a} : {b} — {c}" for a, b, c in C.TARIFS)
    fq = "\n".join(f"### {q}\n{a}\n" for q, a in FAQ)
    write("llms.txt", f"""# {C.BRAND} — {C.SITE_NAME}

> {C.BRAND} est une entreprise spécialisée dans le ponçage, la vitrification, l'huilage, le cirage et la restauration de parquets anciens (point de Hongrie, bâton rompu, parquet Versailles, parquet à l'anglaise) dans les appartements haussmanniens de Paris et de l'ouest parisien. Tarifs à partir de {C.PRICE_FROM} €/m². Devis gratuit sous 24 h ouvrées.

## Informations clés
- Nom : {C.BRAND} — {C.SITE_NAME}
- Activité : ponçage et rénovation de parquets anciens
- Zone : Paris (tous arrondissements), Hauts-de-Seine, Yvelines
- Prix : à partir de {C.PRICE_FROM} €/m² (ponçage 3 passes + vitrification 3 couches)
- Téléphone : {C.PHONE_DISPLAY}
- E-mail : {C.EMAIL}
- Adresse : {C.STREET}, {C.POSTAL_CODE} {C.CITY}
- Horaires : {C.OPENING_HOURS_TEXT}
- Devis : {U}/devis/

## Tarifs
{tf}
{C.PRICE_NOTE}

## Prestations
{svc}

## Zones d'intervention
{zn}
- Autres : {", ".join(OTHER_AREAS)}

## Guides
{gd}

## FAQ
{fq}""")


def build_assets():
    os.makedirs(os.path.join(ROOT, "assets"), exist_ok=True)
    shutil.copy(os.path.join(os.path.dirname(__file__), "style.css"), os.path.join(ROOT, "assets", "style.css"))
    shutil.copy(os.path.join(os.path.dirname(__file__), "app.js"), os.path.join(ROOT, "assets", "app.js"))
    write("img/logo.svg", LOGO.replace('width="40" height="40" aria-hidden="true"', 'xmlns="http://www.w3.org/2000/svg" width="48" height="48"'))


if __name__ == "__main__":
    for d in os.listdir(ROOT) if os.path.isdir(ROOT) else []:
        if d not in ("img",):
            p = os.path.join(ROOT, d)
            shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)
    build_assets(); build_home(); build_services(); build_zones(); build_guides(); build_misc(); build_404(); build_seo_files()
    print(f"{len(PAGES)} pages indexables générées dans public/")
