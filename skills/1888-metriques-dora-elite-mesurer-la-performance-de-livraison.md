---
num: 1888
date_ajout: "2026-11"
nom: "Métriques DORA elite : mesurer la performance de livraison"
emoji: "🥇"
domaine: "Gestion"
signal: "Mesurer la performance de livraison avec les 4 métriques DORA (étalon 2026) : lead time (commit — prod, elite = inférieur à 1 jour), fréquence de déploiement (elite = on-demand, plusieurs/jour), MTTR (1758, elite = inférieur à 1 h), change failure rate (elite = 0-15 %). Benchmarks 2026 + accélérateurs (trunk-based 1404, CI rapide 1413, qualité 1885, déploiement 1418). Dashboard (1766) + revue mensuelle avec les équipes. N'utilise pas de métriques individuelles de 'productivité' (cf SPACE 1798)."
mot_cle: "DORA 4 métriques lead time fréquence déploiement MTTR change failure rate elite benchmark accélérateurs trunk-based 1404 CI 1413 qualité 1885 dashboard 1766"
nom_court: "DORA elite"
branche: "D25"
synonymes: ["nos 4 métriques DORA vs le benchmark elite 2026 : où on se situe", "lead time inférieur à 1 jour, deploy on-demand, MTTR inférieur à 1 h, change failure rate inférieur à 15 % (elite)", "DORA + SPACE 1798 : mesurer l'équipe sans surveillance individuelle"]
cross_refs: [1706, 1798, 1413]
tags: ["2027"]
depends_on: [1706]
---

## 1888. 🥇 Métriques DORA elite : mesurer la performance de livraison

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Mesurer et améliorer la performance de livraison avec les 4 métriques DORA (lead time, fréquence de déploiement, MTTR 1758, change failure rate) vs le benchmark elite — dashboard (1766) + revue mensuelle.

**Quand l'utiliser (triggers)** :
- notre lead time est de 5 jours : quels accélérateurs DORA activer (CI 1413, canary 1418, trunk 1404) ?
- change failure rate à 30 % : qualité 1885 + canary 1418/1877 pour descendre sous 15 %
- revue mensuelle DORA par équipe (dashboard 1766), pas de métrique individuelle

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es engineering manager / DevEx. Tu mesures les 4 métriques DORA depuis la CI (1413) et les déploiements (1418), tu benchmarks vs elite, et tu choisis 1-2 accélérateurs par trimestre (pas 10 à la fois). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les données CI (1413) + déploiements (1418) + incidents (1758)
- Le benchmark DORA 2026
- Les équipes à mesurer

**Méthode** :
1. Lead time : commit -> prod (from git + deploys) ; fréquence : deploys/jour ; MTTR : incidents (1758) ; change failure rate : % de deploys suivis d'un rollback/incident.
2. Benchmark vs elite (DORA 2026) ; positionner l'équipe (low/medium/high/elite).
3. Accélérateurs prioritaires : CI rapide (1413), trunk-based (1404), canary auto (1418/1877), quality gates (1885), observabilité (1416).
4. Revue mensuelle par équipe (1766) ; jamais de métrique individuelle (SPACE 1798).

**Sorties attendues** :
- Le dashboard DORA par équipe (1766) à jour
- La position vs benchmark + 1-2 accélérateurs choisis par trimestre
- Les revues mensuelles tenues

**Exemple de prompt** :
> « Équipe checkout : DORA = lead time 5 j, deploy 1/semaine, MTTR 4 h, CFR 30 % (low) -> accélérateurs choisis : trunk-based (1404) + canary auto (1877) -> T+2 : lead 2 j, deploy 3/j, CFR 12 % (high). »

**Cas d'usage** : Amélioration continue. S'articule avec skills 1706, 1798, 1413, 1418, 1758, 1766, 1404.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
