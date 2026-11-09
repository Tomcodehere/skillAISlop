---
num: 1706
resume: "Mesurer la performance de livraison en 2027 avec les 4 métriques DORA (lead time, deploy frequency, MTTR, change failure rate), collectées automatiquement (CI 1413 + incidents 256), au niveau équipe uniquement — jamais individuel. Étape 1 : Lead time : timestamp commit → déploiement prod (CI 1413), médiane par équipe/semaine."
date_ajout: "2026-11"
nom: "Métriques DORA : mesurer la performance de livraison"
emoji: "📊"
domaine: "Développement"
signal: "Mesurer la performance de livraison avec les 4 métriques DORA en 2027 : lead time for changes (commit→prod), deploy frequency, MTTR (mean time to recovery), change failure rate (% de déploiements avec incident). Les IDP matures atteignent : lead time sous 4 h, déploiements quotidiens, MTTR sous 1 h, failure rate sous 5 %. Utilise pour justifier/piloter la plateforme (1700). N'utilise pas pour évaluer des individus (jamais)."
mot_cle: "métriques DORA 2027 lead time deploy frequency MTTR change failure rate mesurer livraison"
nom_court: "DORA"
branche: "D16"
synonymes: ["lead time commit→prod sous 4 h en 2027 (DORA)", "change failure rate sous 5 % mesuré", "DORA jamais pour évaluer des individus (équipe uniquement)"]
cross_refs: [1700, 36, 344]
tags: ["2027"]
depends_on: [1700]
---

## 1706. 📊 Métriques DORA : mesurer la performance de livraison (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Mesurer la performance de livraison en 2027 avec les 4 métriques DORA (lead time, deploy frequency, MTTR, change failure rate), collectées automatiquement (CI 1413 + incidents 256), au niveau équipe uniquement — jamais individuel.

**Quand l'utiliser (triggers)** :
- combien de temps entre un commit et la prod chez nous ? (lead time DORA)
- on déploie 1x/semaine, objectif quotidien (deploy frequency)
- notre MTTR est de 3 h, objectif sous 1 h (DORA)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es platform engineer metrics. Tu définis les 4 métriques DORA, tu les collectes automatiquement (CI pour lead time/frequency, incidents pour MTTR/failure rate), dashboard par équipe (1698), et tu t'interdis formellement l'usage individuel (c'est un signal d'équipe, pas de performance perso). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La CI (1413) et le suivi des déploiements
- Le suivi des incidents (256)
- Les équipes à mesurer

**Méthode** :
1. Lead time : timestamp commit → déploiement prod (CI 1413), médiane par équipe/semaine.
2. Deploy frequency : nb de déploiements prod/semaine (elite = on demand, plusieurs/jour).
3. MTTR : durée incident (détection 1417 → résolution), médiane.
4. Change failure rate : % de déploiements suivis d'un incident (rollback 1418 ou hotfix) dans les 7 j.
5. Dashboard DORA par équipe (Grafana 1416), revue trimestrielle, jamais individuel.
6. Améliorer : golden paths (1701) réduisent lead time et failure rate (tests auto, canary 1418).

**Sorties attendues** :
- Le dashboard DORA (4 métriques par équipe, auto-collectées)
- Les seuils atteints (ex. lead time sous 4 h, failure rate sous 5 %)
- La règle 'jamais individuel' documentée dans le règlement

**Exemple de prompt** :
> « On veut savoir si notre plateforme (1700) marche : mets les 4 métriques DORA auto (CI 1413 + incidents 256), dashboard par équipe, objectif lead time sous 4 h et failure rate sous 5 % — jamais d'usage individuel. »

**Cas d'usage** : Pilotage plateforme/équipe. S'articule avec skills 1700 (IDP), 36 (KPI), 344 (définitions métriques) et 1698 (analytics).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
