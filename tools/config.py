# -*- coding: utf-8 -*-
"""
CONFIGURATION DU SITE — À COMPLÉTER AVANT LA MISE EN LIGNE
Toutes les valeurs marquées  # À REMPLACER  doivent être remplacées par vos vraies informations.
Puis relancez :  python3 tools/build.py
"""

SITE_URL = "https://www.poncage-parquet-haussmannien.fr"  # À REMPLACER par votre nom de domaine définitif (sans / final)

BRAND = "SGE"
SITE_NAME = "Ponçage Parquet Haussmannien"
LEGAL_NAME = "SGE"                         # À REMPLACER : raison sociale exacte (ex. « SGE SARL »)
PHONE_DISPLAY = "01 00 00 00 00"           # À REMPLACER
PHONE_E164 = "+33100000000"                # À REMPLACER (format international, sans espaces)
WHATSAPP_E164 = ""                         # Optionnel : ex. "33600000000" (sans +) pour afficher un bouton WhatsApp
EMAIL = "contact@poncage-parquet-haussmannien.fr"  # À REMPLACER
STREET = "Adresse à compléter"             # À REMPLACER : adresse du siège (doit être identique à la fiche Google Business)
POSTAL_CODE = "75008"                      # À REMPLACER
CITY = "Paris"
SIRET = "000 000 000 00000"                # À REMPLACER
RCS = "RCS Paris (à compléter)"            # À REMPLACER
DIRECTOR = "Nom du dirigeant (à compléter)"  # À REMPLACER (mentions légales + page À propos)
INSURER = "Assureur décennale (à compléter)"  # À REMPLACER : nom de l'assureur + zone de couverture (obligatoire sur les devis)
HOST_NAME = "Netlify, Inc. — 512 2nd Street, Suite 200, San Francisco, CA 94107, USA"  # hébergeur (modifier si autre)
GOOGLE_BUSINESS_URL = ""                   # À COMPLÉTER : lien de votre fiche Google Business (avis)
SAME_AS = []                               # Liens de vos profils : Instagram, Facebook, Houzz, LinkedIn…
OPENING_HOURS = [("Mo-Fr", "08:00", "19:00"), ("Sa", "09:00", "13:00")]
OPENING_HOURS_TEXT = "Lundi – vendredi : 8 h – 19 h · Samedi : 9 h – 13 h"
GEO = (48.8738, 2.3090)                    # Coordonnées GPS du siège (À AJUSTER)

# Formulaire de devis.
#  - Hébergement Netlify : laissez FORM_ENDPOINT vide, les demandes arrivent dans Netlify > Forms (notification email à activer).
#  - Autre hébergeur : créez un formulaire gratuit sur formspree.io et collez son URL ici, ex. "https://formspree.io/f/abcd1234".
FORM_ENDPOINT = ""

# Mesure d'audience (optionnel) : ID Google Analytics 4 « G-XXXXXXX ». Vide = aucun traceur, donc aucun bandeau cookies nécessaire.
GA4_ID = ""
# Vérification Google Search Console (balise meta) : collez uniquement la valeur du content.
GSC_VERIFICATION = ""

PRICE_FROM = 70  # €/m²
PRICE_NOTE = "Prix indicatifs HT au m², hors fournitures spécifiques. TVA à 10 % pour les travaux de rénovation dans un logement de plus de 2 ans."  # À VÉRIFIER

# Grille tarifaire (modifiable). (prestation, prix, détail)
TARIFS = [
    ("Ponçage + vitrification (3 couches)", "dès 70 €/m²", "Ponçage 3 passes, aspiration intégrée, fond dur + 2 couches de vitrificateur mat, satiné ou ciré-mat."),
    ("Ponçage + huile à l'ancienne", "dès 75 €/m²", "Ponçage 3 passes, huile-cire dure en 2 applications, lustrage mécanique."),
    ("Ponçage + cire naturelle", "dès 85 €/m²", "Bouche-pores, cire d'abeille appliquée et lustrée à la monobrosse, rendu patiné traditionnel."),
    ("Teinte (option)", "+ 12 €/m²", "Teinte à l'eau ou à l'huile, échantillons réalisés sur place avant validation."),
    ("Rebouchage des joints (option)", "+ 8 €/m²", "Mastic bois teinté ou fil de chêne collé pour les joints larges."),
    ("Remplacement de lames anciennes", "sur devis", "Lames de chêne de récupération ou neuves vieillies, posées selon le motif d'origine."),
    ("Ponçage de plinthes, seuils, escaliers", "sur devis", "Travail à la main et à la ponceuse d'angle, finition assortie au sol."),
]

UPDATED = "2026-11-17"
UPDATED_FR = "17 novembre 2026"
