---
num: 1618
nom: "Core Web Vitals 2027 : INP, LCP, CLS et RUM (2027)"
emoji: "📊"
domaine: "Développement"
signal: "Optimiser les Core Web Vitals en 2027 avec du RUM (Real User Monitoring, données réelles des utilisateurs, pas que labo) : LCP (chargement, objectif sous 2,5 s), INP (interactivité, remplace FID depuis 2024, objectif sous 200 ms), CLS (stabilité, sous 0,1). Utilise quand le SEO/conversion dépend de la vitesse. N'utilise pas sans mesurer le RUM d'abord."
mot_cle: "core web vitals 2027 LCP INP CLS RUM real user monitoring CrUX"
nom_court: "CWV 2027"
branche: "D16"
synonymes: ["INP interaction to next paint sous 200 ms", "LCP sous 2,5 s chargement plus grand élément", "RUM données réelles utilisateurs vs labo Lighthouse"]
cross_refs: [253, 1552, 1603]
tags: ["2027"]
depends_on: [253]
---

## 1618. 📊 Core Web Vitals 2027 : INP, LCP, CLS et RUM (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Atteindre les Core Web Vitals 2027 mesurés en RUM (données réelles) : LCP < 2,5 s, INP < 200 ms, CLS < 0,1 — avec un plan d'action par métrique (images, JS, layout).

**Quand l'utiliser (triggers)** :
- notre SEO baisse, les CWV sont dans le rouge
- INP mauvais à cause des gros handlers JS
- mesurer le vrai impact utilisateur (RUM CrUX) pas que Lighthouse

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es dev performance web. Tu définis : LCP (optimiser l'image héros : preload, formats AVIF/WebP, CDN), INP (découper les tâches longues > 50 ms, yield au main thread, utiliser startTransition), CLS (dimensions réservées aux images/ads/iframes, font-display swap). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le site et ses métriques RUM actuelles (CrUX, Analytics 1540)
- Les pages les plus vues
- Les 3 métriques cibles (LCP/INP/CLS)

**Méthode** :
1. Mesurer en RUM (CrUX API ou analytics 1540 avec web-vitals lib) : p75 par page, identifier les pires pages.
2. LCP : preload l'image héros, AVIF/WebP, CDN, compression, lazy le reste.
3. INP : profiler (1552), découper les handlers (scheduler.yield, startTransition React), réduire le JS tiers (partytown).
4. CLS : width/height sur images/vidéos, réservation d'espace pour ads, font-display: swap.
5. Re-mesurer à 1 semaine et 1 mois (RUM), itérer jusqu'aux seuils p75.

**Sorties attendues** :
- Les 3 CWV au vert en p75 RUM (avant/après)
- Le plan d'action par métrique documenté
- Le monitoring RUM continu en place

**Exemple de prompt** :
> « Notre e-commerce a un INP à 450 ms (handlers JS longs) et LCP 4 s (images lourdes) : mesure en RUM (CrUX), preload héros AVIF, découpe les handlers (yield), réserve les espaces ads → CWV au vert p75. »

**Cas d'usage** : SEO, conversion, tout site public. S'articule avec skills 253 (perf web), 1552 (profilage) et 1603 (Astro rapide).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
