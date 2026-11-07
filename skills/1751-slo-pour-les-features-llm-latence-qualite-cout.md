---
num: 1751
date_ajout: "2026-11"
nom: "SLO pour les features LLM : latence, qualité, coût"
emoji: "🎯"
domaine: "Data & IA"
signal: "Définir des SLO en 2027 pour une feature IA (pas que la dispo 351) : latence p99 du streaming (TTFT sous 1 s 1439, fin sous 10 s), taux d'erreur 5xx, qualité (score eval 1630, hallucinations 1155 sous seuil), coût par requête (1491), taux d'escalade HITL (1636). Budget d'erreur : SLO 99,5 % sur 28 j = 3,6 h de panne permise/mois. N'utilise pas sans monitoring (1750)."
mot_cle: "SLO feature LLM 2027 latence p99 TTFT qualité hallucinations coût requête escalade HITL budget erreur 99,5% 3,6h/mois"
nom_court: "SLO LLM"
branche: "D14"
synonymes: ["SLO d'une feature IA : TTFT sous 1 s, latence fin sous 10 s (streaming 1439)", "budget d'erreur : SLO 99,5 % sur 28 j = 3,6 h de panne permise par mois", "SLO qualité : score eval 1630 + hallucinations 1155 sous seuil + coût/requête 1491"]
cross_refs: [351, 1630, 1491]
tags: ["2027"]
depends_on: [351]
---

## 1751. 🎯 SLO pour les features LLM : latence, qualité, coût (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Définir des SLO en 2027 pour une feature IA : latence (TTFT < 1 s, fin < 10 s en streaming 1439), erreurs, qualité (score eval 1630, hallucinations 1155), coût/requête (1491), escalade HITL (1636) — avec budget d'erreur (99,5 % = 3,6 h/mois).

**Quand l'utiliser (triggers)** :
- SLO 99,5 % sur 28 jours = 3,6 h de panne permise par mois (calcul)
- notre chatbot : TTFT sous 1 s, p99 sous 10 s, hallucinations sous 1 %
- coût par requête SLO : moins de 0,02 € (1491)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es SRE feature IA. Tu définis les SLI (latence TTFT/p99 1439, erreurs, qualité eval 1630, coût 1491, escalade 1636), les SLO (99,5 %/99,9 %), le budget d'erreur (formule 28 j), les alertes burn rate (1417), et le gel des features risky quand le budget est brûlé. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La feature IA en prod (1630)
- Les métriques (1750 OTel GenAI)
- Les seuils métier

**Méthode** :
1. SLI latence : TTFT (time to first token 1439) p95 < 500 ms, fin p99 < 10 s (streaming).
2. SLI qualité : score eval hebdo (1630) > 90 %, hallucinations détectées (1155) < 1 % des réponses.
3. SLI coût : coût/requête (1491) < seuil (ex. 0,02 €) — alerte si dépassé.
4. SLI dispo : erreurs 5xx < 0,5 %.
5. SLO global : 99,5 % sur 28 j → budget 3,6 h/mois de 'mauvais' autorisé.
6. Alertes burn rate (1417) : si on brûle le budget vite (ex. > 50 % en 1 semaine), alerte urgente + gel des changements risqués (1418 canary ralenti).
7. Revue mensuelle des SLO avec le métier (ajuster les seuils).

**Sorties attendues** :
- Les SLI/SLO de la feature IA (latence, qualité, coût, dispo) + budget d'erreur calculé
- Les alertes burn rate (1417) + le gel de features quand le budget brûle
- La revue mensuelle avec seuils ajustés

**Exemple de prompt** :
> « Notre chatbot a des SLO flous : définis 2027 — TTFT p95 < 500 ms, fin p99 < 10 s (streaming 1439), erreurs < 0,5 %, qualité eval 1630 > 90 %, hallucinations 1155 < 1 %, coût/requête 1491 < 0,02 € ; SLO 99,5 %/28 j = 3,6 h de budget, alertes burn rate (1417). »

**Cas d'usage** : SLO des features IA en prod. S'articule avec skills 351 (SLI/SLO), 1630 (evals), 1491 (coût), 1417 (alertes), 1439 (streaming).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
