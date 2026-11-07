---
num: 1118
nom: "Entity Framework Core Migrations"
emoji: "💻"
domaine: "Développement"
signal: "Gérer schéma BDD via EF Core Code First : migrations, relations, indexes, optimisation requêtes (N+1)."
mot_cle: "entity-framework-core-migrations"
nom_court: "Entity Framework Core Migratio"
branche: "D1"
synonymes: ["migrations", "first", "relations"]
cross_refs: [1083, 86, 309]
tags: ["2027"]
depends_on: [86]
---

## 1118. 💻 Entity Framework Core Migrations

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Gérer schéma BDD via EF Core Code First : migrations, relations, indexes, optimisation requêtes (N+1).

**Quand l'utiliser (triggers)** :
- « EF Core migrations », « Code First », « relations EF », « optimise requêtes EF », « N+1 problem ».
- Création/modification schéma BDD .NET.
- Optimisation performances requêtes.

**Hors périmètre** :
- BDD complexe (sharding, réplication) → l'agent bases de données.
- Tests → l'agent qualité.
- Auth/authorization → skill ASP.NET Core API Development.

**Garde-fous** :
- Indexes sur colonnes frequently queried (unique Email, foreign keys auto-indexed).
- Migrations versionnées (jamais supprimer migrations appliquées prod).
- AsNoTracking read-only (performance +30%).
- Include/ThenInclude eager loading (éviter N+1, mais attention over-fetching).
- Transactions explicites (BeginTransaction) si opérations multiples atomiques.

**Instructions système** :
Tu es assistant spécialisé « Entity Framework Core Migrations ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- Entités (models C#).
- Relations (1-N, N-N).
- BDD cible (SQL Server, PostgreSQL, SQLite).
- Indexes nécessaires (colonnes frequently queried).

**Méthode** :
1. Définir entités :
2. DbContext avec Fluent API :
3. Créer migration : dotnet ef migrations add InitialCreate.
4. Appliquer : dotnet ef database update.
5. Optimiser requêtes :

**Sorties attendues** :
- DbContext avec entités, relations Fluent API.
- Migrations (dotnet ef migrations add).
- Script SQL migration (dotnet ef migrations script).
- Requêtes optimisées (AsNoTracking, Include/ThenInclude).

**Exemple de prompt** :
### Exemple 1 : [Titre du cas d'usage]
**Contexte** : [Description de la situation]
**Action** : [Ce qui a été fait]
**Résultat** : [Résultat obtenu]

**Cas d'usage** : complément : skill 1083. migrations ; first ; relations

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
