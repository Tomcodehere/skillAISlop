---
num: 1757
resume: "Alerter intelligemment en 2027 avec le burn rate (Google SRE) : calculer la consommation du budget d'erreur (SLO 351) — burn 14x/1 h = page urgente, 6x/6 h = ticket, 1x/3 j = info — pour éviter la fatigue (1417). Étape 1 : SLO ex. 99,9 % sur 30 j → budget d'erreur = 43 min/mois de 'mauvais' (erreurs 5xx ou latence haute)."
lang: "fr"
date_ajout: "2026-11"
nom: "SLO burn rate : alertes intelligentes sur le budget d'erreur"
emoji: "⏱️"
domaine: "Data"
signal: "Alerter intelligemment en 2027 avec le burn rate (Google SRE) : au lieu d'alerter sur chaque pic, calculer le taux de consommation du budget d'erreur (SLO 351/1751) — burn rate 14x sur 1 h = alerte page urgente (budget brûlé en 2 j), 6x sur 6 h = alerte ticket, 1x sur 3 j = info. Évite la fatigue (1417). N'utilise pas pour remplacer les alertes de panne totale."
mot_cle: "burn rate SLO 2027 alertes intelligentes budget erreur 14x 1h page urgente 6x 6h ticket 1x 3j info anti fatigue 1417"
nom_court: "Burn rate"
branche: "D17"
synonymes: ["burn rate 14x sur 1h = alerte urgente (le budget brûle en 2 jours)", "6x sur 6h = ticket, 1x sur 3j = info (Google SRE 2027)", "moins d'alertes, plus pertinentes (anti fatigue 1417)"]
cross_refs: [351, 1417, 1751]
tags: ["2027"]
depends_on: [351]
---

## 1757. ⏱️ SLO burn rate : alertes intelligentes sur le budget d'erreur (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Alerter intelligemment en 2027 avec le burn rate (Google SRE) : calculer la consommation du budget d'erreur (SLO 351) — burn 14x/1 h = page urgente, 6x/6 h = ticket, 1x/3 j = info — pour éviter la fatigue (1417).

**Quand l'utiliser (triggers)** :
- on est pagés pour un pic de 5 min qui n'a rien consommé
- burn rate 14x sur 1h : le budget d'erreur sera vide en 2 jours → page
- 6x sur 6h = ticket, 1x sur 3j = juste une info (pas de page)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es SRE alerting. Tu définis le SLO (99,9 % = 43 min/mois de budget 351), tu calcules le burn rate multi-fenêtres (1 h/6 h/3 j), et tu routes : 14x/1h → PagerDuty urgent, 6x/6h → ticket, 1x/3j → log/info (1417). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le SLO (351/1751) et son budget
- Les métriques de conformité (1416)
- Les canaux d'alerte (1417)

**Méthode** :
1. SLO ex. 99,9 % sur 30 j → budget d'erreur = 43 min/mois de 'mauvais' (erreurs 5xx ou latence haute).
2. Burn rate = (taux d'erreur réel / taux d'erreur autorisé) ; fenêtres courtes (1 h) et longues (3 j).
3. Seuils : burn 14x sur 1 h → urgent (budget consommé en ~2 j) ; 6x sur 6 h → ticket ; 1x sur 3 j → info.
4. Implémenter : Prometheus recording rules (ratio erreurs/requêtes vs SLO) + Alertmanager routing (1417) avec 3 niveaux.
5. Jamais d'alerte sur un pic isolé sans burn rate (anti-fatigue 1417).
6. Revue mensuelle : ajuster les seuils selon les faux positifs.

**Sorties attendues** :
- Les règles burn rate multi-fenêtres (14x/1h, 6x/6h, 1x/3j) déployées
- Le routage Alertmanager (1417) : urgent/ticket/info selon le burn
- Le suivi : nb d'alertes avant/après (objectif -70 % de bruit, 0 incident manqué)

**Exemple de prompt** :
> « On est pagés pour des pics de 5 min qui ne consomment rien : passe aux alertes burn rate 2027 (SLO 99,9 % = 43 min/mois 351) — burn 14x/1 h = urgent, 6x/6 h = ticket, 1x/3 j = info (1417) ; -70 % de bruit, 0 incident manqué. »

**Cas d'usage** : Alerting SRE moderne. S'articule avec skills 351 (SLO), 1751 (SLO LLM), 1417 (alerting), 1416 (Prometheus/Grafana).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
