---
num: 1678
date_ajout: "2026-11"
nom: "Data contracts en prod : enforcement auto en CI"
emoji: "📜"
domaine: "Data"
signal: "Faire respecter les data contracts en production en 2027 (complète 1234/1461) : contrat = schéma + sémantique + qualité + SLA signés par producteur et consommateur ; enforcement AUTO en CI (1592) : le producteur ne peut merger si le contrat change sans versionnage (v1→v2 avec période de grâce), monitoring prod (1675), alerte aux deux côtés, dépréciation avec date. Utilise pour les pipelines inter-équipes. N'utilise pas pour une équipe seule."
mot_cle: "data contracts prod 2027 enforcement CI auto versionnage v1 v2 SLA producteur consommateur dépréciation"
nom_court: "Contrats prod"
branche: "D15"
synonymes: ["le producteur change le schéma sans prévenir, la CI bloque", "contrat signé : schéma + qualité + SLA, versionné v1→v2", "dépréciation avec date : 3 mois avant suppression de colonne"]
cross_refs: [1234, 1461, 1675]
tags: ["2027"]
depends_on: [1234]
---

## 1678. 📜 Data contracts en prod : enforcement auto en CI (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Faire respecter les data contracts en prod en 2027 : contrat signé (schéma, sémantique, qualité, SLA), enforcement AUTO en CI (1592) — un changement de schéma bloque le merge sans versionnage v1→v2 + période de grâce, monitoring prod (1675), alerte bilatérale, dépréciation datée.

**Quand l'utiliser (triggers)** :
- le CRM a supprimé une colonne, 3 pipelines cassés, CI aurait dû bloquer
- contrat v1 → v2 avec 3 mois de grâce avant suppression
- SLA : 99,9% de fraîcheur, alerte si dépassé (1417)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es data platform governance. Tu définis le contrat en YAML (schéma JSON 1427, sémantique, règles qualité 1675, SLA, propriétaires), versionné Git, check auto en CI (1592) côté producteur, monitoring prod (1675), dépréciation avec date butoir. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les sources inter-équipes (contrats à protéger)
- Le format de contrat (YAML/JSON)
- La CI (1592) et le monitoring (1675)

**Méthode** :
1. Rédiger le contrat par source critique : schéma (types, nullabilité 1424), sémantique (définition métier 344), qualité (règles 1675), SLA (fraîcheur, dispo), propriétaires producteur/consommateur.
2. CI producteur (1592) : à chaque PR, comparer le schéma proposé au contrat ; changement cassant → blocage sauf versionnage v2 + période de grâce (ex. 3 mois) + notification consommateurs.
3. CI consommateur : idem, test de lecture du contrat en staging.
4. Monitoring prod (1675) : alerte bilatérale si SLA violé (fraîcheur, volume, drift 1461).
5. Dépréciation : colonne marquée deprecated avec date de suppression (ex. +6 mois), communication aux consommateurs.

**Sorties attendues** :
- Les contrats signés (YAML) versionnés, enforcement CI auto (1592)
- Le blocage des changements cassants sans v2 + grâce testé
- Le monitoring SLA prod (1675) + dépréciation datée communiquée

**Exemple de prompt** :
> « Le CRM a supprimé une colonne sans prévenir et 3 pipelines ont cassé : data contracts signés (schéma+qualité+SLA 1675), CI (1592) bloque tout changement cassant sans versionnage v2 + 3 mois de grâce, monitoring prod avec alerte bilatérale (1461). »

**Cas d'usage** : Pipelines inter-équipes en prod. S'articule avec skills 1234 (contrats producteur-consommateur), 1461 (drift), 1675 (qualité) et 1592 (CI).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
