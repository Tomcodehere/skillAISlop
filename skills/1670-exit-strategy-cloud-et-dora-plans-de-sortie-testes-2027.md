---
num: 1670
date_ajout: "2026-11"
nom: "Exit strategy cloud et DORA : plans de sortie testes (2027)"
emoji: "🚪"
domaine: "Data"
signal: "Rédiger et tester une exit strategy cloud en 2027 (obligation DORA pour la finance : plans de sortie 'suffisamment testés' pour les services ICT critiques) : inventaire des dépendances (vendor lock-in), export des données en format ouvert (1663), contrat avec clauses de sortie (Data Act 1671), test de restauration chez un autre fournisseur, runbook, exercice annuel (1454). Utilise pour tout contrat cloud critique. N'utilise pas pour du SaaS bureautique mineur."
mot_cle: "exit strategy cloud 2027 DORA plan de sortie testé vendor lock-in export ouvert runbook exercice annuel"
nom_court: "Exit cloud"
branche: "D15"
synonymes: ["DORA : mon plan de sortie cloud doit être testé, pas juste écrit", "sortir d'AWS : quoi exporter, où, comment restaurer", "runbook de migration cloud avec RTO/RPO"]
cross_refs: [1649, 1671, 1688]
tags: ["2027"]
depends_on: [1671]
---

## 1670. 🚪 Exit strategy cloud et DORA : plans de sortie testes (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Rédiger et TESTER une exit strategy cloud en 2027 (DORA : plans de sortie suffisamment testés pour l'ICT critique) : inventaire du lock-in, export en format ouvert (1663), clauses de sortie (Data Act 1671), restauration testée chez un autre fournisseur, runbook + exercice annuel (1454).

**Quand l'utiliser (triggers)** :
- DORA nous demande un plan de sortie 'suffisamment testé' pour AWS
- quels services nous verrouillent vraiment (lock-in) ?
- tester la restauration chez un 2e fournisseur (OVH 1688)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte résilience cloud. Tu fais : inventaire des services cloud et leur lock-in (managed DB, IAM, services propriétaires), plan de sortie par criticité (RTO/RPO), export régulier en format ouvert (1663), test de restauration annuel (1454), clauses contractuelles (1671). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les services cloud utilisés et leur criticité (DORA 1649)
- Le fournisseur de secours (cloud UE 1688, on-prem)
- Les RTO/RPO par service

**Méthode** :
1. Inventorier : services utilisés, données, dépendances propriétaires (ex. DynamoDB, IAM), volume.
2. Classer par criticité (DORA) : critiques → exit testé obligatoire, autres → documenté.
3. Export régulier : données en Parquet/Iceberg (1663) sur stockage indépendant, test de lecture.
4. Test annuel : restaurer un service critique chez le 2e fournisseur, mesurer le RTO réel (1454).
5. Contrat : clause de sortie + Data Act (1671) + SLA de coopération du fournisseur (30 j).
6. Runbook (199) + exercice tabletop annuel (1454) + revue post-exercice.

**Sorties attendues** :
- L'inventaire du lock-in par service cloud
- Le test de restauration annuel réussi (RTO mesuré) chez le 2e fournisseur
- Le runbook + contrat avec clause de sortie (1671)

**Exemple de prompt** :
> « DORA exige un plan de sortie testé pour notre CRM sur AWS : inventaire du lock-in (DynamoDB, Cognito), export Parquet/Iceberg (1663) régulier, restauration testée chez OVH (1688) avec RTO mesuré, runbook + clause Data Act (1671) + exercice annuel (1454). »

**Cas d'usage** : Finance (DORA), toute charge critique cloud. S'articule avec skills 1649 (NIS2/DORA), 1671 (Data Act), 1688 (cloud UE) et 1454 (tabletop).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
