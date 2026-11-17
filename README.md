# SGE — Ponçage Parquet Haussmannien

Site vitrine statique (HTML/CSS, sans framework) optimisé pour le référencement local (SEO) et les moteurs de réponse IA (GEO), conçu pour générer des demandes de devis qualifiées.

## Structure
- `tools/config.py` — **vos informations** (téléphone, adresse, SIRET, assurance, domaine, tarifs). À compléter en premier.
- `tools/content.py` — textes des prestations, zones, guides et FAQ.
- `tools/build.py` — génère le site dans `public/`.
- `tools/gen_images.py` — visuels de parquet générés (à remplacer par vos photos).
- `public/` — le site prêt à publier (31 pages indexables + sitemap.xml, robots.txt, llms.txt).

Après toute modification : `python3 tools/build.py`

## Mise en ligne (Netlify, gratuit, formulaire inclus)
1. Créez un compte sur netlify.com → *Add new site* → *Import from GitHub* → choisissez ce dépôt.
2. Netlify lit `netlify.toml` automatiquement (dossier publié : `public`). Déployez.
3. *Domain management* → ajoutez votre domaine (ex. `poncage-parquet-haussmannien.fr`), HTTPS est automatique.
4. *Forms* → activez la détection des formulaires puis une notification e-mail pour le formulaire « devis ».
5. Mettez `SITE_URL` à jour dans `tools/config.py` si le domaine diffère, puis rebuild.

## Checklist SEO après mise en ligne
- [ ] Remplacer tous les « À REMPLACER » de `tools/config.py` (même nom/adresse/téléphone partout = NAP cohérent).
- [ ] Créer / optimiser la **fiche Google Business Profile** (catégorie « Entreprise de ponçage de parquets »), ajouter son lien dans `GOOGLE_BUSINESS_URL`.
- [ ] Google Search Console : vérifier le domaine, soumettre `sitemap.xml`. Idem Bing Webmaster Tools (alimente ChatGPT/Copilot).
- [ ] Remplacer les visuels générés par **vos vraies photos avant/après** (mêmes noms de fichiers dans `public/img/`, en .jpg et .webp).
- [ ] Demander un avis Google à chaque client satisfait (lien direct par SMS après chantier).
- [ ] Inscrire l'entreprise sur Pages Jaunes, Houzz, Habitatpresto, Travaux.com, Obat, avec exactement les mêmes coordonnées.
- [ ] Publier un nouveau guide ou une réalisation par mois (quartier + motif + surface + photos).
