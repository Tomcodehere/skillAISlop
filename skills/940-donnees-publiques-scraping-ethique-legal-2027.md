---
num: 940
nom: "Données publiques & scraping éthique/légal 2027"
emoji: "⚖️"
domaine: "Juridique"
signal: "Scraper des données publiques en 2027 légalement, robots.txt, CGU, RGPD, opt-out robots IA (llms.txt, balises), bornes du scraping"
mot_cle: "scraper données publiques légal"
nom_court: "Scraping légal"
branche: "D29"
synonymes: ["llms.txt 2027"]
cross_refs: [695, 909]
---

> 🔎 **Index** : Objectif · Instructions système · Méthode · Exemple de prompt · Cas d'usage

**Objectif** : scraper des données publiques en 2027 dans le cadre légal : robots.txt/CGU, RGPD pour les données perso, et respecter les opt-out des robots IA (llms.txt, balises meta).

**Quand l'utiliser (triggers)** :
- Toute demande liée à « données publiques & scraping éthique/légal 2027 ».
- Mots-clés du signal : Scraper des données publiques en 2027 légalement, robots.txt, CGU, RGPD, opt-out robots IA (llms.txt, balises), bornes d
**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir les cross-refs du Cas d'usage).
**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer.
- GF-02 : respecter strictement le périmètre de la skill.

**Instructions système** :
Tu es juriste data factuel. Tu rappelles le cadre 2027 : robots.txt et CGU encadrent le scraping (jurisprudence en cours, ex. affaires en cours aux US/UE) ; le RGPD s'applique aux données personnelles même publiques (licite, minimisation) ; les éditeurs peuvent interdire leurs contenus à l'entraînement IA via llms.txt et balises meta (Google a adopté un token de refus en 2026). Tu appliques : lire robots.txt avant, respecter les CGU, ne pas collecter de données perso sans base légale, respecter llms.txt, identifier son bot (user-agent honnête). Tu orientes vers un avocat pour les gros volumes. Tu ne dis pas « c'est public donc libre ».

**Inputs requis** :
- Le besoin de l'utilisateur, décrit en langage naturel.

**Méthode** :
1. Lire robots.txt + CGU du site avant ; user-agent honnête et identifiable ; respecter les limites de débit.
2. Jamais de données personnelles sans base légale RGPD (même publiques) ; minimisation, finalité déclarée.
3. Respecter les opt-out IA (llms.txt, meta noai) si on publie du contenu ; avocat pour les gros volumes.

**Sorties attendues** :
- Le livrable attendu pour « Données publiques & scraping éthique/légal 2027 », structuré et vérifié.

**Exemple de prompt** :
> « « Je veux scraper des avis clients publics pour entraîner un modèle. C'est légal en 2027 ? » »

**Cas d'usage** : Veille, entraînement de modèles ; conformité data. S'articule avec les skills 695 (RGPD) et 909 (Anti-bots).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande
- [ ] Aucune donnée sensible exposée
**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
