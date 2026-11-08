---
num: 1711
date_ajout: "2026-11"
nom: "Scorecards : niveaux de maturité des services"
emoji: "🎯"
domaine: "Développement"
signal: "Mettre des scorecards en 2027 (Port/Cortex natifs, ou Backstage plugin) : chaque service noté bronze/argent/or sur des critères (observabilité OTel 1680, sécurité 1646, SLO 351, CI 1413, owner renseigné, doc 1406), avec plan d'amélioration. Sert à piloter la dette et la conformité sans revue manuelle de chaque service. N'utilise pas pour noter des personnes (jamais)."
mot_cle: "scorecards services 2027 bronze argent or maturité observabilité sécurité SLO CI owner doc Port Cortex"
nom_court: "Scorecards"
branche: "D16"
synonymes: ["scorecard par service : bronze/argent/or (observabilité, sécurité, SLO)", "Port/Cortex scorecards automatiques 2027", "jamais de scorecard sur des personnes, uniquement des services"]
cross_refs: [1710, 1702, 351]
tags: ["2027"]
depends_on: [1702]
---

## 1711. 🎯 Scorecards : niveaux de maturité des services (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Noter chaque service en 2027 (bronze/argent/or) via des scorecards (Port/Cortex natifs ou plugin Backstage) sur : observabilité (OTel 1680), sécurité (1646), SLO (351), CI (1413), owner + doc (1406) — pour piloter la dette sans revue manuelle, jamais sur des personnes.

**Quand l'utiliser (triggers)** :
- quel service n'a pas de SLO ni de doc ? (scorecard)
- bronze/argent/or automatique sur 200 services (Port)
- piloter la dette technique avec les scorecards, pas des audits manuels

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es platform engineer gouvernance. Tu définis les critères par niveau (bronze = owner+doc, argent = + CI tests + SLO, or = + OTel complet + sécurité 1646 + runbook 199), les seuils automatiques (API k8s/CI), et le plan d'amélioration par service. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le catalogue de services (1702)
- Les critères par niveau
- Les seuils automatiques (APIs)

**Méthode** :
1. Définir les niveaux : bronze (owner renseigné, doc 1406, repo propre), argent (+ CI tests 67, SLO 351, alertes 1417), or (+ OTel traces 1680, SAST 1646, runbook 199, PRA testé 1454).
2. Automatiser : scorecards calculés depuis les APIs (k8s labels, CI, Grafana) — pas de saisie manuelle.
3. Dashboard par équipe (qui a combien de bronze), objectif : 0 bronze à 6 mois.
4. Plan d'amélioration par service en dette (bronze/argent) avec owner et échéance.
5. Jamais de classement de personnes — uniquement des services (règle absolue).

**Sorties attendues** :
- Les scorecards auto (bronze/argent/or) sur tous les services
- Le dashboard par équipe + objectif 0 bronze à 6 mois
- Les plans d'amélioration en dette avec owners et échéances

**Exemple de prompt** :
> « 200 services, personne ne sait lesquels ont un SLO ou de la doc : déploie des scorecards auto (Port/Cortex ou plugin Backstage) bronze/argent/or (owner/doc/CI/SLO/OTel/sécurité 1646), dashboard par équipe, objectif 0 bronze à 6 mois, jamais sur des personnes. »

**Cas d'usage** : Gouvernance plateforme. S'articule avec skills 1710 (Port/Cortex), 1702 (Backstage), 351 (SLO) et 1646 (sécurité).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
