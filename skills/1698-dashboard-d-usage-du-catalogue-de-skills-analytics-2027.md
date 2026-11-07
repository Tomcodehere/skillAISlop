---
num: 1698
nom: "Dashboard d'usage du catalogue de skills (analytics, 2027)"
emoji: "📊"
domaine: "Routage"
signal: "Visualiser l'usage réel du catalogue de skills en 2027 : `routage.py analytics` (SQL sur la table routes) + dashboard (Grafana 1416 ou Metabase 1674) : top skills routées, taux exit 0/1/2, domaines les plus sollicités, misses récurrents (1497), évolution par version (versions). Utilise pour décider quelles skills prioriser/maintenir. N'utilise pas pour espionner des utilisateurs individuels (RGPD 1584 : anonymiser)."
mot_cle: "dashboard usage catalogue skills analytics routes top skills exit 0 1 2 misses récurrents par domaine"
nom_court: "Analytics catalogue"
branche: "D26"
synonymes: ["quelles sont les 20 skills les plus utilisées ? (top popularité 1416)", "taux d'exit 2 du routeur par semaine (misses 1497)", "évolution du routage par version (versions)"]
cross_refs: [1497, 0, 1540]
tags: ["2027"]
depends_on: [1497]
---

## 1698. 📊 Dashboard d'usage du catalogue de skills (analytics, 2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Visualiser l'usage réel du catalogue en 2027 : analytics SQL (table routes) + dashboard (top skills, taux exit 0/1/2, domaines sollicités, misses récurrents 1497, évolution par version) — pour décider quelles skills prioriser, avec données anonymisées (RGPD 1584).

**Quand l'utiliser (triggers)** :
- quelles skills ne servent jamais ? (à archiver/maintenir)
- le taux d'exit 2 monte depuis la vague 18
- quels domaines sont les plus sollicités cette semaine ?

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es conservateur du catalogue. Tu branches analytics (SQL agrégé) + dashboard (Grafana/Metabase 1674) : top 20 skills, répartition par domaine et par voie (mot-clé/fts/vec/synonyme), exit 0/1/2, misses top (1497), tendance hebdo, par version (versions). Données anonymisées (pas de user_id, 1584). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La table routes (logs de routage)
- Le dashboard (Grafana 1416 / Metabase 1674)
- La politique de rétention/anonymisation (1584)

**Méthode** :
1. Collecte : chaque route loggue (demande hashée, code exit, voie, num, date) dans routes — jamais la demande en clair ni le user (1584, hash 1465).
2. Requêtes SQL (analytics) : top skills (COUNT), par domaine, par voie, taux exit 2/semaine, misses fréquents (joint non_routees 1497).
3. Dashboard : 4-6 panneaux (top 20, camembert domaines, courbe exit 2, heatmap heure/jour, évolution par version).
4. Décisions : skills jamais routées 90 j → archiver/maintenir ? ; domaines sous-couverts → nouvelle vague ; exit 2 récurrent → synonyme (1497).
5. Revue mensuelle avec le comité (présentation 14).

**Sorties attendues** :
- Le dashboard d'usage (top skills, domaines, exit 0/1/2, misses, versions)
- Les requêtes analytics SQL prêtes (top, domaines, voies)
- La revue mensuelle avec décisions documentées (archiver/nouvelle vague)

**Exemple de prompt** :
> « Quelles skills servent vraiment ? : dashboard sur la table routes (anonymisée 1584) — top 20 skills, domaines sollicités, taux exit 2 hebdo (misses 1497), évolution par version ; revue mensuelle : archiver les jamais-routées 90 j, nouvelle vague sur les domaines faibles. »

**Cas d'usage** : Gouvernance du catalogue. S'articule avec skills 1497 (misses), 0 (routeur), 1540 (analytics) et 1674 (BI as code).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
