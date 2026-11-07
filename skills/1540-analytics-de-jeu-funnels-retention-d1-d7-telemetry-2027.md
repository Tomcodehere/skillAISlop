---
num: 1540
date_ajout: "2026-11"
nom: "Analytics de jeu : funnels, rétention D1/D7, telemetry (2027)"
emoji: "📊"
domaine: "Game Dev"
signal: "Mettre en place la télémétrie d'un jeu en 2027 (RGPD-compliant 1587) : événements custom (level_start, boss_kill, purchase) envoyés à Unity Analytics/GameAnalytics/custom, funnels (tutoriel étape 3 → 4), rétention D1/D7/D30, dashboards, décisions data-driven. Utilise dès le soft launch. N'utilise pas pour espionner (consentement requis)."
mot_cle: "analytics jeu télémétrie funnels rétention D1 D7 D30 événements custom"
nom_court: "Analytics jeu"
branche: "D22"
synonymes: ["funnel tutoriel étape par étape", "rétention D1 D7 D30 dashboard", "envoyer événements custom à Unity Analytics", "mesurer ARPU rétention D7 p-value ship kill"]
cross_refs: [1541, 110, 1587]
tags: ["2027"]
depends_on: [110]
---

## 1540. 📊 Analytics de jeu : funnels, rétention D1/D7, telemetry (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Mettre en place la télémétrie d'un jeu en 2027 (avec consentement RGPD) : événements custom (level_start, boss_kill, achat), funnels de tutoriel (1572), rétention D1/D7/D30, dashboards, pour décider data-driven (1481).

**Quand l'utiliser (triggers)** :
- Combien de joueurs atteignent le niveau 3 ? (funnel)
- Rétention D1/D7/D30 sur le dashboard
- Envoyer un événement custom à chaque kill de boss

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es game analyst. Tu définis les événements nommés (snake_case, params max 10), le consentement (opt-in, 1587), l'envoi (Unity Analytics/GameAnalytics/batch custom), et les dashboards : funnels, rétention cohortes, revenus. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les événements clés du jeu (tutoriel, niveaux, achats, crashes)
- La plateforme d'analytics (Unity Analytics, GameAnalytics, Segment custom)
- Le consentement RGPD (1587)

**Méthode** :
1. Lister les événements critiques : tutorial_step(n), level_start/end, boss_kill, purchase, crash, session_start.
2. Implémenter analytics.logEvent(nom, params) avec batch (toutes les 30 s ou 20 events) + consentement opt-in (écran de choix).
3. Funnels : séquence d'étapes (tutoriel 1→5) → taux de passage par étape (où on perd les joueurs ?).
4. Rétention : cohortes D1/D7/D30 (qui revient ?), dashboard courbe.
5. Dashboards : rétention, funnels, revenus ARPPU, crash-free rate (objectif > 99 %).

**Sorties attendues** :
- La télémétrie déployée (events + consentement)
- Les funnels de tutoriel et la rétention D1/D7/D30
- Le dashboard avec décisions data-driven

**Exemple de prompt** :
> « On ne sait pas où on perd les joueurs : mets la télémétrie (events tutorial_step/level_end/purchase + consentement), funnels de tutoriel, rétention D1/D7/D30, dashboard Unity Analytics. »

**Cas d'usage** : Soft launch, live ops (1542), équilibrage (1529). S'articule avec skills 1541 (A/B in-game), 110 (A/B) et 1587 (RGPD).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
