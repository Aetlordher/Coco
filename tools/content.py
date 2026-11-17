# -*- coding: utf-8 -*-
"""Contenus éditoriaux du site (services, zones, guides, FAQ)."""

# ---------------------------------------------------------------- FAQ globale
FAQ = [
    ("Quel est le prix du ponçage d'un parquet haussmannien à Paris ?",
     "Chez SGE, le ponçage complet d'un parquet ancien avec vitrification 3 couches commence à 70 €/m². Le prix final dépend de l'état du bois (taches, lames abîmées, joints ouverts), du motif (point de Hongrie, bâton rompu, Versailles) et de la finition choisie (vitrificateur, huile ou cire). Le devis est gratuit et détaillé après visite ou envoi de photos."),
    ("Combien de temps durent les travaux ?",
     "Comptez en général 2 à 3 jours pour 30 à 50 m² : une journée de ponçage, puis l'application de la finition en plusieurs couches avec les temps de séchage. On peut marcher en chaussettes 12 à 24 h après la dernière couche et réinstaller les meubles au bout de 48 à 72 h selon le produit."),
    ("Le ponçage fait-il beaucoup de poussière ?",
     "Nos ponceuses sont reliées à des aspirateurs à filtration haute performance. La quasi-totalité de la poussière est captée à la source, les portes et passages sont protégés par des films de confinement, et le chantier est aspiré avant chaque couche de finition."),
    ("Un parquet ancien peut-il être poncé plusieurs fois ?",
     "Oui. Un parquet massif ancien possède généralement une couche d'usure de 6 à 10 mm au-dessus de la languette, ce qui permet plusieurs ponçages au cours de sa vie. Nous mesurons l'épaisseur disponible avant d'intervenir et adaptons le grain pour ne retirer que le strict nécessaire."),
    ("Vitrifier, huiler ou cirer : que choisir ?",
     "La vitrification est la plus résistante et la plus simple d'entretien (idéale pour les pièces de vie et les familles). L'huile donne un aspect naturel et se répare localement. La cire offre la patine la plus authentique pour un parquet haussmannien mais demande un entretien régulier. Nous vous conseillons selon l'usage de chaque pièce."),
    ("Faut-il vider entièrement les pièces ?",
     "Oui, les pièces à poncer doivent être vides de meubles. Si vous le souhaitez, nous pouvons organiser les travaux pièce par pièce pour vous permettre de déplacer le mobilier d'une pièce à l'autre."),
    ("Intervenez-vous dans les appartements occupés et en copropriété ?",
     "Oui, c'est notre quotidien : nous respectons les horaires du règlement de copropriété, protégeons les parties communes et l'ascenseur, et prévenons le gardien ou le syndic si nécessaire."),
    ("Pouvez-vous remplacer des lames abîmées ou manquantes ?",
     "Oui. Nous remplaçons les lames tachées, fendues ou attaquées par des insectes avec du chêne de récupération ou du chêne neuf vieilli, posé dans le respect du motif d'origine (point de Hongrie, bâton rompu ou panneaux Versailles)."),
    ("Comment obtenir un devis ?",
     "Remplissez le formulaire en ligne en joignant quelques photos, ou appelez-nous. Nous vous répondons sous 24 h ouvrées et nous déplaçons gratuitement à Paris et en proche banlieue pour mesurer et diagnostiquer le parquet."),
]

# ---------------------------------------------------------------- SERVICES
SERVICES = [
 dict(
  slug="poncage-parquet", name="Ponçage de parquet ancien", short="Ponçage de parquet",
  img="apres-point-de-hongrie", icon="sand",
  title="Ponçage de parquet ancien à Paris — dès 70 €/m² | SGE",
  desc="Ponçage de parquet haussmannien à Paris et en Île-de-France : point de Hongrie, bâton rompu, Versailles. Ponçage sans poussière, devis gratuit sous 24 h, dès 70 €/m².",
  h1="Ponçage de parquet ancien à Paris",
  lead="Rendre à un parquet de chêne centenaire sa teinte d'origine sans l'abîmer : c'est notre métier. Nous ponçons vos sols en point de Hongrie, bâton rompu ou à l'anglaise avec un matériel aspiré et une méthode adaptée aux bois anciens.",
  tldr="SGE ponce les parquets anciens des appartements parisiens à partir de 70 €/m² (ponçage 3 passes + vitrification 3 couches). Comptez 2 à 3 jours pour 40 m². Devis gratuit après visite ou sur photos.",
  body="""
<h2>Pourquoi poncer un parquet ancien ?</h2>
<p>Avec le temps, un parquet de chêne se grise, se raye et perd sa protection. Les anciens vernis jaunissent, les cires s'encrassent et les zones de passage se creusent. Le ponçage retire cette couche de surface abîmée pour retrouver un bois sain, homogène et prêt à recevoir une nouvelle finition. C'est l'opération qui transforme le plus radicalement l'aspect d'un appartement, pour un coût bien inférieur au remplacement du sol.</p>
<h2>Un ponçage pensé pour les parquets haussmanniens</h2>
<p>Les parquets des immeubles parisiens du XIX<sup>e</sup> siècle sont en chêne massif, cloués sur lambourdes, souvent posés en <a href="../parquet-point-de-hongrie/">point de Hongrie</a> ou en <a href="../parquet-baton-rompu/">bâton rompu</a>. Leurs lames changent de sens tous les quarante centimètres : un ponçage mal conduit laisse des marques de disque et des « vagues » visibles à contre-jour. Nous travaillons donc :</p>
<ul class="checks">
<li>en <strong>trois passes de grains progressifs</strong> (généralement 36/40, 60 puis 100/120), en diagonale du motif ;</li>
<li>avec une <strong>bordureuse et une ponceuse d'angle</strong> pour les rives, les pieds de cheminée et les embrasures ;</li>
<li>en <strong>contrôlant les têtes de clous</strong> et en les rechassant avant chaque passe pour protéger les abrasifs et le bois ;</li>
<li>en terminant par un <strong>égrenage à la monobrosse</strong> qui efface les rayures circulaires et ouvre le pore pour la finition.</li>
</ul>
<h2>Ponçage sans poussière, chantier protégé</h2>
<p>Nos machines sont raccordées à des aspirateurs à haute filtration. Nous posons des protections de sol dans les parties communes, isolons les pièces non traitées avec des films de confinement et aspirons intégralement avant chaque couche. Vous retrouvez un logement propre, prêt à être réaménagé.</p>
<h2>Les étapes d'un ponçage SGE</h2>
<ol class="steps">
<li><strong>Diagnostic gratuit</strong> : mesure des surfaces, épaisseur d'usure, état des lames, humidité, type de finition existante.</li>
<li><strong>Préparation</strong> : protection, rechassage des clous, dépose éventuelle des plinthes ou barres de seuil.</li>
<li><strong>Ponçage</strong> en trois grains, bordures et angles compris.</li>
<li><strong>Réparations</strong> : rebouchage des joints, remplacement de lames si nécessaire.</li>
<li><strong>Finition</strong> : vitrification, huile ou cire, avec ou sans teinte, appliquée en plusieurs couches.</li>
<li><strong>Réception</strong> : contrôle avec vous à la lumière rasante et remise des conseils d'entretien.</li>
</ol>
<h2>Combien coûte un ponçage de parquet ?</h2>
<p>Le ponçage avec vitrification 3 couches commence à <strong>70 €/m²</strong>. Les options (teinte, rebouchage des joints, remplacement de lames) sont chiffrées séparément sur un devis ligne par ligne. Consultez notre <a href="../tarifs/">grille de tarifs détaillée</a> ou notre <a href="../guides/prix-poncage-parquet-paris/">guide des prix 2026</a>.</p>
""",
  faq=[0, 1, 2, 3],
 ),
 dict(
  slug="vitrification-parquet", name="Vitrification de parquet", short="Vitrification",
  img="vitrification-mat", icon="shield",
  title="Vitrification de parquet à Paris — mat, satiné, effet naturel | SGE",
  desc="Vitrification de parquet ancien à Paris : vitrificateurs bi-composants à l'eau, finition mat ou effet bois brut, haute résistance. Ponçage + vitrification dès 70 €/m².",
  h1="Vitrification de parquet à Paris",
  lead="La vitrification protège durablement votre parquet sous un film invisible, résistant aux rayures, aux taches et à l'eau. Nous utilisons des vitrificateurs professionnels en phase aqueuse, sans odeur persistante.",
  tldr="La vitrification est la finition la plus résistante pour un parquet de pièce de vie. SGE applique un fond dur + 2 couches de vitrificateur bi-composant à l'eau (mat, extra-mat ou satiné). Ponçage + vitrification à partir de 70 €/m².",
  body="""
<h2>Une protection durable pour les pièces à vivre</h2>
<p>La vitrification forme un film polyuréthane qui protège le bois du piétinement, des chaises, des animaux et des taches du quotidien. Elle s'entretient simplement avec un balai et une serpillière bien essorée. C'est la finition que nous recommandons pour les séjours, les chambres d'enfants, les couloirs et les cuisines ouvertes.</p>
<h2>Les vitrificateurs que nous utilisons</h2>
<ul class="checks">
<li><strong>Vitrificateurs bi-composants en phase aqueuse</strong> : la meilleure résistance à l'abrasion, très faible teneur en COV, peu d'odeur.</li>
<li><strong>Finition extra-mat « bois brut »</strong> : le parquet semble non traité, tout en étant protégé — le rendu le plus demandé pour les appartements haussmanniens.</li>
<li><strong>Finition mat ou satinée</strong> pour un aspect plus classique.</li>
<li><strong>Fond dur adapté au chêne</strong> pour limiter le jaunissement et l'effet de collage des lames.</li>
</ul>
<h2>Ce qui fait une vitrification réussie</h2>
<p>Une vitrification ne vaut que par la préparation : un ponçage homogène, une aspiration minutieuse, des couches appliquées au rouleau dans le sens du fil de chaque bande du motif et un égrenage entre les couches. Nous travaillons à température et hygrométrie contrôlées pour garantir un film uniforme, sans bulles ni reprises.</p>
<h2>Délais et remise en service</h2>
<p>Pièces praticables en chaussettes après 12 h, meubles réinstallés après 48 h (avec patins feutre), tapis posés après 8 à 10 jours, le temps de la polymérisation complète.</p>
<h2>Vitrification ou huile ?</h2>
<p>Vous hésitez ? Lisez notre comparatif <a href="../guides/vitrifier-ou-huiler-parquet-ancien/">vitrifier ou huiler un parquet ancien</a>, ou découvrez notre service <a href="../huilage-cirage-parquet/">huilage et cirage</a>.</p>
""",
  faq=[4, 1, 2],
 ),
 dict(
  slug="huilage-cirage-parquet", name="Huilage, cirage et teinte", short="Huilage & cirage",
  img="huilage-cire", icon="drop",
  title="Huilage et cirage de parquet ancien à Paris — finition naturelle | SGE",
  desc="Huilage, cirage traditionnel et teinte de parquet ancien à Paris. Finitions naturelles respectueuses du chêne haussmannien. Ponçage + huile dès 75 €/m².",
  h1="Huilage, cirage et teinte de parquet",
  lead="Pour un rendu authentique, mat et chaleureux, rien ne remplace l'huile et la cire. Ces finitions nourrissent le bois en profondeur et lui donnent la patine des beaux appartements anciens.",
  tldr="L'huile pénètre le bois et se répare localement ; la cire offre la patine la plus traditionnelle. SGE propose ponçage + huile dès 75 €/m² et ponçage + cire naturelle dès 85 €/m², avec teintes sur échantillons.",
  body="""
<h2>L'huile : un aspect naturel, facile à réparer</h2>
<p>L'huile-cire dure imprègne les fibres du chêne et durcit à cœur. Le parquet garde un toucher de bois, sans film en surface. En cas de rayure ou de tache, on rénove localement la zone, sans reprendre toute la pièce. Un entretien avec un savon spécifique et un ravivage tous les 1 à 2 ans suffisent.</p>
<h2>La cire : la patine des intérieurs haussmanniens</h2>
<p>Historiquement, les parquets parisiens étaient cirés. Nous perpétuons ce savoir-faire : bouche-pores, cire naturelle appliquée en fines couches puis lustrée à la monobrosse. Le résultat est profond, satiné et chaleureux. La cire demande un entretien plus régulier : nous vous remettons un protocole d'entretien simple.</p>
<h2>Teintes : du chêne clair au noyer</h2>
<p>Blanchi, naturel, miel, chêne fumé, noyer ou wengé : nous réalisons des échantillons directement sur votre parquet poncé, à la lumière de vos pièces, avant de valider la teinte. Une teinte à l'eau sous vitrificateur ou une huile teintée peuvent être proposées selon l'usage.</p>
<figure class="figure"><picture><source srcset="../img/teinte-chene-fonce.webp" type="image/webp"><img src="../img/teinte-chene-fonce.jpg" alt="Parquet point de Hongrie teinté chêne foncé et huilé" width="1200" height="800" loading="lazy"></picture><figcaption>Illustration : point de Hongrie teinté chêne foncé, finition huilée.</figcaption></figure>
<h2>Quelle finition pour quelle pièce ?</h2>
<table class="table"><thead><tr><th>Pièce</th><th>Finition conseillée</th></tr></thead><tbody>
<tr><td>Séjour, salle à manger</td><td>Vitrification extra-mat ou huile-cire dure</td></tr>
<tr><td>Chambres</td><td>Huile ou cire</td></tr>
<tr><td>Entrée, couloir</td><td>Vitrification (forte usure)</td></tr>
<tr><td>Cuisine ouverte</td><td>Vitrification bi-composant</td></tr>
<tr><td>Salon de réception</td><td>Cire traditionnelle lustrée</td></tr>
</tbody></table>
""",
  faq=[4, 0],
 ),
 dict(
  slug="parquet-point-de-hongrie", name="Rénovation de parquet point de Hongrie", short="Point de Hongrie",
  img="hero-point-de-hongrie", icon="chevron",
  title="Rénovation parquet point de Hongrie à Paris — ponçage & restauration | SGE",
  desc="Spécialiste de la rénovation de parquet point de Hongrie à Paris : ponçage, remplacement de lames coupées à 45°, vitrification, huile ou cire. Devis gratuit.",
  h1="Rénovation de parquet point de Hongrie",
  lead="Emblème des appartements haussmanniens, le point de Hongrie se reconnaît à ses lames coupées en biseau qui dessinent des chevrons parfaits. Sa rénovation exige précision et respect du motif.",
  tldr="Le point de Hongrie est un parquet à lames coupées à 45° ou 60° formant des chevrons. SGE le ponce en diagonale du motif pour éviter les marques, remplace les lames abîmées par des pièces taillées sur mesure et applique la finition de votre choix, dès 70 €/m².",
  body="""
<h2>Reconnaître un parquet point de Hongrie</h2>
<p>Dans le point de Hongrie, les extrémités des lames sont coupées en biais (le plus souvent à 45° ou 60°) et se rejoignent bout à bout pour former une ligne continue de chevrons. On le confond souvent avec le <a href="../parquet-baton-rompu/">bâton rompu</a>, dont les lames sont coupées droites et s'emboîtent en quinconce. Notre <a href="../guides/point-de-hongrie-ou-baton-rompu/">guide comparatif</a> détaille les différences.</p>
<h2>Les défis du ponçage d'un point de Hongrie</h2>
<p>Le fil du bois change de direction à chaque bande. Une ponceuse menée dans le mauvais sens arrache les fibres d'une bande sur deux. Nous ponçons en diagonale, à vitesse et pression maîtrisées, puis finissons à la monobrosse pour un rendu parfaitement uniforme, sans marque de transversale.</p>
<h2>Remplacement de lames sur mesure</h2>
<p>Lames tachées par l'eau, fendues, vermoulues ou disparues lors d'un ancien passage de canalisation : nous taillons des pièces de remplacement à l'angle exact du motif, dans du chêne de récupération ou du chêne neuf à la même teinte, et les intégrons sans rupture visible.</p>
<h2>Finitions conseillées</h2>
<p>Pour sublimer les chevrons : <a href="../vitrification-parquet/">vitrification extra-mat</a> « bois brut », huile naturelle ou <a href="../huilage-cirage-parquet/">cire traditionnelle</a>. Une légère teinte peut harmoniser des lames anciennes et neuves.</p>
""",
  faq=[0, 7, 3],
 ),
 dict(
  slug="parquet-baton-rompu", name="Rénovation de parquet bâton rompu", short="Bâton rompu",
  img="baton-rompu", icon="herringbone",
  title="Ponçage et rénovation de parquet bâton rompu à Paris | SGE",
  desc="Rénovation de parquet en bâton rompu (chevron droit) à Paris : ponçage aspiré, réparation, recalage des lames, vitrification, huile ou cire. Dès 70 €/m².",
  h1="Rénovation de parquet bâton rompu",
  lead="Le bâton rompu, aussi appelé « chevron droit » ou « herringbone », habille de nombreux appartements parisiens et immeubles des années 1900 à 1930. Nous lui redonnons son éclat d'origine.",
  tldr="Le bâton rompu est un parquet à lames rectangulaires posées perpendiculairement en quinconce. SGE le ponce, refixe les lames qui bougent, rebouche les joints et applique une finition durable, à partir de 70 €/m².",
  body="""
<h2>Spécificités du bâton rompu</h2>
<p>Ses lames rectangulaires, coupées à angle droit, s'emboîtent alternativement pour dessiner un zigzag. Ce motif, plus fréquent que le point de Hongrie dans les immeubles post-haussmanniens et Art déco, présente souvent des lames décollées ou des joints ouverts aux points de passage.</p>
<h2>Notre intervention</h2>
<ul class="checks">
<li>Repérage et refixation des lames qui sonnent creux ou grincent ;</li>
<li>Ponçage en diagonale du motif avec trois grains successifs ;</li>
<li>Rebouchage des joints à la pâte à bois teintée ou au fil de chêne ;</li>
<li>Finition vitrifiée, huilée ou cirée, avec teinte sur échantillon si souhaité.</li>
</ul>
<figure class="figure"><picture><source srcset="../img/avant-baton-rompu.webp" type="image/webp"><img src="../img/avant-baton-rompu.jpg" alt="Parquet bâton rompu grisé et rayé avant ponçage" width="1200" height="800" loading="lazy"></picture><figcaption>Illustration : bâton rompu grisé avant ponçage.</figcaption></figure>
<h2>Bâton rompu collé ou cloué ?</h2>
<p>Les bâtons rompus anciens sont cloués sur lambourdes ou sur un parquet support ; ceux des années 1950–1970 sont souvent collés au bitume sur dalle. Nous identifions le mode de pose avant le chantier, car il conditionne la réparation des lames et la profondeur de ponçage possible.</p>
""",
  faq=[0, 3, 7],
 ),
 dict(
  slug="parquet-versailles", name="Restauration de parquet Versailles", short="Parquet Versailles",
  img="parquet-versailles", icon="grid",
  title="Restauration de parquet Versailles à Paris — panneaux anciens | SGE",
  desc="Restauration et ponçage de parquets à panneaux Versailles, Chantilly et à compartiments à Paris : réparation de panneaux, ponçage, cire ou huile. Devis gratuit.",
  h1="Restauration de parquet Versailles",
  lead="Le parquet Versailles, composé de panneaux carrés à entrelacs, est le plus noble des parquets anciens. On le retrouve dans les hôtels particuliers et les grands appartements de réception.",
  tldr="Le parquet Versailles est constitué de panneaux carrés (souvent environ 1 m de côté) assemblés à tenons et mortaises en motif d'entrelacs. SGE le restaure panneau par panneau : refixation, remplacement de pièces, ponçage délicat et finition cire ou huile.",
  body="""
<h2>Un parquet d'exception, un traitement d'exception</h2>
<p>Créé pour le château de Versailles à la fin du XVII<sup>e</sup> siècle, ce parquet à panneaux s'est répandu dans les demeures aristocratiques puis dans les appartements bourgeois parisiens. Ses pièces assemblées dans plusieurs directions de fil imposent un ponçage particulièrement délicat.</p>
<h2>Notre méthode de restauration</h2>
<ol class="steps">
<li>Relevé du motif et repérage des panneaux dégradés ;</li>
<li>Démontage si nécessaire, recollage et remplacement des pièces manquantes à l'identique ;</li>
<li>Ponçage à grain fin, finitions manuelles autour des entrelacs ;</li>
<li>Finition cire traditionnelle ou huile naturelle, lustrage.</li>
</ol>
<p>Nous intervenons également sur les parquets Chantilly, Chevreuse, Arenberg et les parquets à compartiments ou à frises d'encadrement.</p>
""",
  faq=[7, 4],
 ),
 dict(
  slug="restauration-parquet-ancien", name="Réparation et restauration de parquet ancien", short="Réparation & restauration",
  img="avant-point-de-hongrie", icon="tools",
  title="Réparation de parquet ancien à Paris — lames, grincements, joints | SGE",
  desc="Réparation de parquet ancien à Paris : remplacement de lames, suppression des grincements, rebouchage des joints, traitement des insectes, dégâts des eaux. Devis gratuit.",
  h1="Réparation et restauration de parquet ancien",
  lead="Grincements, lames qui bougent, joints ouverts, taches noires après un dégât des eaux, traces de cloisons supprimées : nous réparons votre parquet avant de le poncer, pour un résultat homogène.",
  tldr="SGE répare les parquets anciens avant ponçage : remplacement de lames, refixation, suppression des grincements, rebouchage des joints, raccords après suppression de cloison et traitement curatif des insectes xylophages.",
  body="""
<h2>Les réparations les plus fréquentes</h2>
<ul class="checks">
<li><strong>Lames tachées ou noircies</strong> (dégât des eaux, pots de fleurs, urine d'animaux) : remplacement par du chêne ancien.</li>
<li><strong>Raccords après travaux</strong> : suppression de cloison, ouverture de cuisine, passage de gaines — nous recréons le motif en continuité.</li>
<li><strong>Grincements</strong> : refixation des lames sur les lambourdes par vissage ou clouage invisible.</li>
<li><strong>Joints ouverts</strong> : rebouchage au fil de chêne collé ou à la pâte à bois teintée.</li>
<li><strong>Insectes xylophages</strong> : traitement curatif avant finition.</li>
</ul>
<h2>Du bois ancien pour des raccords invisibles</h2>
<p>Un chêne neuf n'a ni la teinte ni la densité d'un chêne centenaire. Nous utilisons dès que possible des lames de récupération issues d'appartements anciens, puis harmonisons la teinte lors de la finition.</p>
<h2>Indemnisation après sinistre</h2>
<p>En cas de dégât des eaux, nous établissons un devis détaillé et des photos utilisables par votre assureur ou votre syndic.</p>
""",
  faq=[7, 3, 6],
 ),
]

# ---------------------------------------------------------------- ZONES
ZONES = [
 dict(slug="paris-8", name="Paris 8e", full="Paris 8e arrondissement", cp="75008",
  intro="Le 8e arrondissement concentre certains des plus beaux immeubles haussmanniens de la capitale : boulevard Haussmann, avenue de Messine, rue de Courcelles, abords du parc Monceau.",
  body="<p>Autour de la plaine Monceau et du quartier de l'Europe, les grands appartements bourgeois conservent souvent leurs parquets d'origine : point de Hongrie dans les salons en enfilade, parquet Versailles dans certaines pièces de réception, bâton rompu dans les chambres. Nous intervenons régulièrement dans des immeubles de prestige où la protection des parties communes et le respect des horaires de la copropriété sont essentiels.</p><p>Quartiers desservis : Faubourg-du-Roule, Madeleine, Europe, Champs-Élysées, plaine Monceau.</p>"),
 dict(slug="paris-16", name="Paris 16e", full="Paris 16e arrondissement", cp="75016",
  intro="Passy, Auteuil, Trocadéro, Chaillot ou Porte Dauphine : le 16e mêle immeubles haussmanniens, post-haussmanniens, Art nouveau et Art déco, chacun avec ses parquets caractéristiques.",
  body="<p>Les immeubles de pierre de taille de l'avenue Victor-Hugo ou de l'avenue Kléber abritent de nombreux points de Hongrie ; les constructions des années 1920–1930 d'Auteuil présentent plus souvent des bâtons rompus et des parquets à l'anglaise en chêne ou en essences plus exotiques. Nous adaptons la méthode de ponçage et la finition à chaque époque.</p><p>Quartiers desservis : Passy, Auteuil, La Muette, Chaillot, Porte Dauphine.</p>"),
 dict(slug="paris-17", name="Paris 17e", full="Paris 17e arrondissement", cp="75017",
  intro="De la plaine Monceau aux Batignolles en passant par les Ternes, le 17e regorge d'appartements anciens aux parquets de chêne en point de Hongrie.",
  body="<p>Avenue de Villiers, avenue de Wagram, rue de Prony ou boulevard Malesherbes : les immeubles de la fin du XIX<sup>e</sup> siècle y ont souvent conservé leurs parquets d'origine, parfois recouverts de moquette ou de linoléum. Nous les révélons, les réparons et leur offrons une seconde vie. Côté Batignolles, nous intervenons aussi dans les immeubles de faubourg plus modestes aux parquets à l'anglaise.</p><p>Quartiers desservis : Ternes, Plaine-Monceau, Batignolles, Épinettes.</p>"),
 dict(slug="paris-7", name="Paris 7e", full="Paris 7e arrondissement", cp="75007",
  intro="Faubourg Saint-Germain, Gros-Caillou, Invalides, Champ-de-Mars : le 7e associe hôtels particuliers du XVIII<sup>e</sup> siècle et immeubles haussmanniens des avenues Bosquet et Rapp.",
  body="<p>Les hôtels particuliers et appartements anciens du 7e possèdent parfois des parquets à panneaux Versailles ou des points de Hongrie très anciens, qui ont déjà connu plusieurs ponçages. Nous mesurons systématiquement l'épaisseur d'usure restante et privilégions un ponçage minimal suivi d'une finition cirée, plus respectueuse de ces bois patrimoniaux.</p><p>Quartiers desservis : Saint-Thomas-d'Aquin, Invalides, École-Militaire, Gros-Caillou.</p>"),
 dict(slug="paris-6", name="Paris 6e", full="Paris 6e arrondissement", cp="75006",
  intro="Saint-Germain-des-Prés, Odéon, Luxembourg, Notre-Dame-des-Champs : le 6e abrite des immeubles des XVII<sup>e</sup>, XVIII<sup>e</sup> et XIX<sup>e</sup> siècles, et une grande variété de parquets anciens.",
  body="<p>Dans les immeubles anciens de la rue de Rennes, du boulevard Saint-Germain ou de la rue d'Assas, on rencontre aussi bien des points de Hongrie haussmanniens que des parquets à l'anglaise en larges lames ou des panneaux Versailles. Les accès souvent étroits et les cages d'escalier anciennes demandent une logistique soignée : matériel compact, protections renforcées, interventions planifiées avec le syndic.</p><p>Quartiers desservis : Monnaie, Odéon, Notre-Dame-des-Champs, Saint-Germain-des-Prés.</p>"),
 dict(slug="paris-9", name="Paris 9e", full="Paris 9e arrondissement", cp="75009",
  intro="Opéra, Chaussée-d'Antin, Saint-Georges, Nouvelle Athènes : le 9e est au cœur du Paris haussmannien et de ses grands appartements parquetés.",
  body="<p>Des immeubles de la Restauration de la Nouvelle Athènes aux immeubles haussmanniens du boulevard Haussmann et de la rue La Fayette, le 9e offre une grande diversité de parquets anciens. Nous rénovons aussi bien les appartements familiaux que les cabinets et bureaux installés dans d'anciens logements bourgeois, avec des interventions possibles le week-end pour ne pas perturber l'activité.</p><p>Quartiers desservis : Saint-Georges, Chaussée-d'Antin, Faubourg-Montmartre, Rochechouart.</p>"),
 dict(slug="neuilly-sur-seine", name="Neuilly-sur-Seine", full="Neuilly-sur-Seine (92200)", cp="92200",
  intro="À Neuilly-sur-Seine, hôtels particuliers, villas et immeubles bourgeois en pierre de taille possèdent souvent de magnifiques parquets anciens en chêne.",
  body="<p>Du boulevard Victor-Hugo à l'île de la Jatte, en passant par le quartier Saint-James, nous restaurons des parquets point de Hongrie, bâton rompu et Versailles dans des maisons et appartements de caractère. Les grandes surfaces et les pièces de réception se prêtent particulièrement aux finitions cirées et huilées, qui mettent en valeur la profondeur du chêne.</p><p>Nous intervenons également à Levallois-Perret, Courbevoie et Puteaux.</p>"),
 dict(slug="boulogne-billancourt", name="Boulogne-Billancourt", full="Boulogne-Billancourt (92100)", cp="92100",
  intro="Boulogne-Billancourt est réputée pour son patrimoine des années 1920–1930 : immeubles Art déco, villas d'architectes, mais aussi immeubles bourgeois du début du XX<sup>e</sup> siècle.",
  body="<p>Dans les quartiers Parchamp-Albert-Kahn, Rhin-et-Danube ou Silly-Gallieni, les parquets en bâton rompu et à l'anglaise sont majoritaires, parfois en essences rares. Nous les ponçons avec soin, réparons les lames décollées et proposons des finitions modernes extra-mates ou des teintes plus soutenues pour les intérieurs contemporains.</p><p>Nous intervenons également à Issy-les-Moulineaux et Saint-Cloud.</p>"),
 dict(slug="levallois-perret", name="Levallois-Perret", full="Levallois-Perret (92300)", cp="92300",
  intro="Entre immeubles anciens rénovés et appartements familiaux, Levallois-Perret compte de nombreux parquets en chêne massif à remettre en valeur.",
  body="<p>Nous rénovons à Levallois des parquets anciens en point de Hongrie et en bâton rompu, souvent lors d'une rénovation complète d'appartement après achat. Notre planning s'adapte à celui des autres corps de métier : le ponçage et la finition interviennent idéalement en dernier, après la peinture.</p><p>Nous intervenons aussi à Clichy, Neuilly-sur-Seine et dans le 17e arrondissement voisin.</p>"),
 dict(slug="versailles", name="Versailles", full="Versailles (78000)", cp="78000",
  intro="Berceau du célèbre parquet à panneaux qui porte son nom, Versailles compte de nombreux hôtels particuliers et appartements anciens dans les quartiers Notre-Dame et Saint-Louis.",
  body="<p>Nous restaurons à Versailles des parquets Versailles authentiques, des points de Hongrie et des parquets à l'anglaise en chêne ancien. Ces bois souvent très anciens ont déjà connu plusieurs ponçages : nous privilégions des interventions douces et des finitions traditionnelles à la cire qui respectent leur patine.</p><p>Nous intervenons aussi au Chesnay-Rocquencourt et à Viroflay.</p>"),
 dict(slug="saint-germain-en-laye", name="Saint-Germain-en-Laye", full="Saint-Germain-en-Laye (78100)", cp="78100",
  intro="Le centre historique de Saint-Germain-en-Laye et ses demeures de caractère abritent des parquets anciens d'une grande qualité.",
  body="<p>Maisons bourgeoises, hôtels particuliers du centre-ville et appartements anciens : nous y rénovons parquets en chêne massif, escaliers et paliers. Les grandes maisons familiales permettent souvent de travailler par zones pour limiter la gêne au quotidien.</p><p>Nous intervenons aussi au Pecq, à Chatou et au Vésinet.</p>"),
]

OTHER_AREAS = ["Paris 1er", "Paris 2e", "Paris 3e", "Paris 4e", "Paris 5e", "Paris 10e", "Paris 11e", "Paris 12e", "Paris 14e", "Paris 15e", "Paris 18e", "Saint-Cloud", "Issy-les-Moulineaux", "Vincennes", "Saint-Mandé", "Le Vésinet", "Chatou", "Rueil-Malmaison", "Suresnes", "Courbevoie", "Puteaux", "Clichy"]

# ---------------------------------------------------------------- GUIDES
GUIDES = [
 dict(slug="prix-poncage-parquet-paris", img="apres-point-de-hongrie",
  title="Prix du ponçage de parquet à Paris en 2026 : tarifs au m² détaillés",
  h1="Prix du ponçage de parquet à Paris en 2026",
  desc="Combien coûte le ponçage d'un parquet ancien à Paris en 2026 ? Tarifs au m², options, exemples chiffrés pour 30, 50 et 80 m², et conseils pour comparer les devis.",
  tldr="En 2026 à Paris, un ponçage-vitrification standard se négocie souvent entre 35 et 65 €/m². Pour un parquet ancien (point de Hongrie, bâton rompu, Versailles) traité par un spécialiste — ponçage 3 passes, réparations, vitrificateur bi-composant ou finition naturelle — comptez à partir de 70 €/m², le tarif d'entrée de SGE.",
  body="""
<h2>Ce qui compose le prix d'un ponçage</h2>
<ul class="checks">
<li><strong>Le ponçage</strong> lui-même (3 passes, bordures, angles) ;</li>
<li><strong>La finition</strong> : vitrificateur, huile ou cire, et le nombre de couches ;</li>
<li><strong>Les réparations</strong> : joints, lames à remplacer, refixation ;</li>
<li><strong>Les contraintes du chantier</strong> : étage sans ascenseur, stationnement, horaires de copropriété ;</li>
<li><strong>La surface</strong> : les petites surfaces font l'objet d'un forfait minimum.</li>
</ul>
<h2>Tarifs indicatifs SGE</h2>
{TARIF_TABLE}
<h2>Exemples chiffrés</h2>
<table class="table"><thead><tr><th>Surface</th><th>Ponçage + vitrification (dès 70 €/m²)</th><th>Avec teinte et joints (dès 90 €/m²)</th></tr></thead><tbody>
<tr><td>30 m² (studio, grande pièce)</td><td>à partir de 2 100 €</td><td>à partir de 2 700 €</td></tr>
<tr><td>50 m² (2–3 pièces)</td><td>à partir de 3 500 €</td><td>à partir de 4 500 €</td></tr>
<tr><td>80 m² (appartement familial)</td><td>à partir de 5 600 €</td><td>à partir de 7 200 €</td></tr>
</tbody></table>
<p class="note">Montants HT indicatifs. Le prix exact est fixé après diagnostic sur place ou sur photos.</p>
<h2>Pourquoi des écarts de prix entre devis ?</h2>
<p>Un devis à 25 ou 30 €/m² correspond rarement à la même prestation : ponçage en deux passes seulement, vitrificateur mono-composant, bordures non finies à la main, aucune réparation incluse. Sur un parquet haussmannien, ces économies se voient : marques de disque, joints noirs, film qui s'use en un ou deux ans dans les passages. Comparez les devis ligne par ligne : nombre de passes, produit exact, nombre de couches, réparations incluses, protection du chantier.</p>
<h2>TVA réduite</h2>
<p>Pour un logement achevé depuis plus de deux ans, les travaux de rénovation de parquet bénéficient généralement d'une TVA à 10 %, sous réserve de l'attestation à fournir.</p>
<p><a class="btn" href="../../devis/">Obtenir mon devis gratuit</a></p>
""",
  faq=[0, 1]),
 dict(slug="point-de-hongrie-ou-baton-rompu", img="baton-rompu",
  title="Point de Hongrie ou bâton rompu : comment les reconnaître ?",
  h1="Point de Hongrie ou bâton rompu : les différences",
  desc="Point de Hongrie ou bâton rompu ? Coupe des lames, histoire, rendu, prix et rénovation : le guide pour reconnaître et entretenir les parquets à chevrons des appartements parisiens.",
  tldr="Le point de Hongrie a des lames coupées en biais (45° ou 60°) qui forment une ligne de chevrons continue ; le bâton rompu a des lames coupées droites qui s'imbriquent en quinconce pour former un zigzag. Les deux se poncent en diagonale du motif.",
  body="""
<h2>La coupe des lames, le critère décisif</h2>
<table class="table"><thead><tr><th></th><th>Point de Hongrie</th><th>Bâton rompu</th></tr></thead><tbody>
<tr><td>Coupe des extrémités</td><td>En biais (45° ou 60°)</td><td>Droite (90°)</td></tr>
<tr><td>Dessin</td><td>Pointes alignées, chevrons continus</td><td>Zigzag en escalier</td></tr>
<tr><td>Époque typique à Paris</td><td>Immeubles haussmanniens (1850–1900)</td><td>Toutes époques, très fréquent 1900–1960</td></tr>
<tr><td>Coût de pose neuve</td><td>Plus élevé (coupes, chutes)</td><td>Un peu moins élevé</td></tr>
<tr><td>Rénovation</td><td>Ponçage diagonal, lames de remplacement à l'angle exact</td><td>Ponçage diagonal, refixation fréquente</td></tr>
</tbody></table>
<figure class="figure"><picture><source srcset="../../img/hero-point-de-hongrie.webp" type="image/webp"><img src="../../img/hero-point-de-hongrie.jpg" alt="Parquet point de Hongrie avec chevrons continus" width="1600" height="1000" loading="lazy"></picture><figcaption>Point de Hongrie : les lames se rejoignent en pointe.</figcaption></figure>
<figure class="figure"><picture><source srcset="../../img/baton-rompu.webp" type="image/webp"><img src="../../img/baton-rompu.jpg" alt="Parquet bâton rompu avec lames en quinconce" width="1200" height="800" loading="lazy"></picture><figcaption>Bâton rompu : les lames s'imbriquent en quinconce.</figcaption></figure>
<h2>Les rénover sans les abîmer</h2>
<p>Dans les deux cas, le fil du bois change de direction d'une lame à l'autre : on ponce en diagonale du motif puis on termine à la monobrosse. Découvrez nos services <a href="../../parquet-point-de-hongrie/">point de Hongrie</a> et <a href="../../parquet-baton-rompu/">bâton rompu</a>.</p>
""",
  faq=[3]),
 dict(slug="vitrifier-ou-huiler-parquet-ancien", img="vitrification-mat",
  title="Vitrifier ou huiler un parquet ancien ? Comparatif complet",
  h1="Vitrifier, huiler ou cirer un parquet ancien ?",
  desc="Vitrificateur, huile ou cire : résistance, aspect, entretien, prix et durée de vie. Le comparatif d'un spécialiste du parquet ancien pour choisir la bonne finition.",
  tldr="Vitrifier = protection maximale et entretien minimal ; huiler = aspect naturel et réparations locales faciles ; cirer = patine traditionnelle mais entretien régulier. Pour un séjour parisien avec enfants, la vitrification extra-mat est le meilleur compromis.",
  body="""
<h2>Tableau comparatif</h2>
<table class="table"><thead><tr><th></th><th>Vitrification</th><th>Huile</th><th>Cire</th></tr></thead><tbody>
<tr><td>Résistance à l'usure</td><td>★★★</td><td>★★</td><td>★</td></tr>
<tr><td>Aspect naturel</td><td>★★ (extra-mat : ★★★)</td><td>★★★</td><td>★★★</td></tr>
<tr><td>Réparation locale</td><td>Difficile</td><td>Facile</td><td>Facile</td></tr>
<tr><td>Entretien</td><td>Très simple</td><td>Ravivage tous les 1–2 ans</td><td>Recirage régulier</td></tr>
<tr><td>Durée avant rénovation</td><td>8–12 ans</td><td>Illimitée avec entretien</td><td>Illimitée avec entretien</td></tr>
<tr><td>Tarif SGE (avec ponçage)</td><td>dès 70 €/m²</td><td>dès 75 €/m²</td><td>dès 85 €/m²</td></tr>
</tbody></table>
<h2>Nos recommandations</h2>
<p>Vitrification pour les pièces très passantes et les familles ; huile pour qui aime le contact du bois et accepte un entretien léger ; cire pour les salons de réception et les parquets patrimoniaux. Il est tout à fait possible de combiner plusieurs finitions dans un même appartement.</p>
<p>Voir aussi : <a href="../../vitrification-parquet/">vitrification de parquet</a> · <a href="../../huilage-cirage-parquet/">huilage et cirage</a>.</p>
""",
  faq=[4]),
 dict(slug="combien-de-fois-poncer-parquet", img="parquet-anglaise",
  title="Combien de fois peut-on poncer un parquet ancien ?",
  h1="Combien de fois peut-on poncer un parquet ancien ?",
  desc="Couche d'usure, épaisseur, signes d'un parquet trop poncé : tout savoir sur le nombre de ponçages possibles d'un parquet massif ancien et comment le préserver.",
  tldr="Un parquet massif ancien de 23 mm possède en général 6 à 10 mm de bois au-dessus de la languette. Un ponçage professionnel retire environ 0,5 à 1 mm : le parquet peut donc être poncé de nombreuses fois s'il est confié à un spécialiste.",
  body="""
<h2>La couche d'usure, capital du parquet</h2>
<p>La couche d'usure est l'épaisseur de bois située au-dessus de la languette. Tant qu'elle est suffisante, le parquet peut être poncé. Au-delà, on voit apparaître les têtes de clous et les languettes : il est trop tard pour un ponçage classique.</p>
<h2>Comment nous la préservons</h2>
<ul class="checks">
<li>Mesure de l'épaisseur disponible (au droit d'une plinthe ou d'une grille de ventilation) ;</li>
<li>Choix du premier grain en fonction de l'état réel : inutile de partir trop gros sur un parquet simplement terni ;</li>
<li>Ponçage diagonal régulier, sans creuser les passages ;</li>
<li>Proposition d'une simple <strong>rénovation sans ponçage</strong> (égrenage + nouvelle couche) quand le vernis n'est qu'usé en surface.</li>
</ul>
<h2>Tous les combien poncer ?</h2>
<p>Une vitrification de qualité dure 8 à 12 ans dans un séjour. Avec une huile ou une cire bien entretenue, le ponçage n'est nécessaire qu'en cas de dégradation importante.</p>
""",
  faq=[3]),
 dict(slug="preparer-logement-poncage-parquet", img="parquet-versailles",
  title="Préparer son logement avant un ponçage de parquet : la check-list",
  h1="Préparer son logement avant un ponçage de parquet",
  desc="Meubles, plinthes, copropriété, animaux, temps de séchage : la check-list pour préparer un ponçage de parquet et réinstaller son appartement au bon moment.",
  tldr="Avant un ponçage : vider les pièces, prévenir la copropriété, prévoir un accès électrique et un point d'eau, éloigner les animaux. Après : marcher en chaussettes 12–24 h après la dernière couche, meubles avec patins à 48–72 h, tapis à 8–10 jours.",
  body="""
<h2>Avant le chantier</h2>
<ol class="steps">
<li>Videz les pièces concernées (meubles, tapis, rideaux longs) ;</li>
<li>Prévenez le syndic ou le gardien et vérifiez les horaires autorisés ;</li>
<li>Faites réaliser la peinture et les travaux poussiéreux <em>avant</em> le ponçage ;</li>
<li>Prévoyez un accès à l'électricité et à un point d'eau ;</li>
<li>Organisez la garde des animaux et, idéalement, un hébergement pendant la finition.</li>
</ol>
<h2>Après le chantier</h2>
<table class="table"><thead><tr><th>Délai après la dernière couche</th><th>Ce qui est possible</th></tr></thead><tbody>
<tr><td>12 à 24 h</td><td>Marcher en chaussettes</td></tr>
<tr><td>48 à 72 h</td><td>Réinstaller les meubles avec patins feutre</td></tr>
<tr><td>8 à 10 jours</td><td>Reposer les tapis, premier lavage</td></tr>
</tbody></table>
""",
  faq=[1, 5, 6]),
]
