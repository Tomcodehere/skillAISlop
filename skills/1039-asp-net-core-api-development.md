---
num: 1039
resume: "Développer API REST ASP.NET Core (controllers, Minimal APIs, validation, auth JWT, Swagger). Étape 1 : Créer projet : dotnet new webapi -n MyApi."
lang: "fr"
date_ajout: "2026-11"
nom: "ASP.NET Core API Development"
emoji: "💻"
domaine: "Développement"
signal: "Développer API REST ASP.NET Core (controllers, Minimal APIs, validation, auth JWT, Swagger)."
mot_cle: "asp-net-core-api-development"
nom_court: "ASP.NET Core API Development"
branche: "D1"
synonymes: ["controllers", "minimal", "swagger"]
cross_refs: [1194, 1118, 526]
tags: ["2027"]
---

## 1039. 💻 ASP.NET Core API Development

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Développer API REST ASP.NET Core (controllers, Minimal APIs, validation, auth JWT, Swagger).

**Quand l'utiliser (triggers)** :
- « API REST .NET », « ASP.NET Core controllers », « Minimal APIs », « Swagger OpenAPI ».
- Création API backend .NET.
- Refonte API existante (migration .NET Framework → .NET 6+).

**Hors périmètre** :
- Frontend Blazor → skill Blazor Component Design.
- BDD migrations → skill Entity Framework Core Migrations.
- Tests → l'agent qualité.

**Garde-fous** :
- DTOs séparés (ne jamais exposer entités EF Core directement).
- Validation entrées (FluentValidation preferred, ou DataAnnotations).
- Auth JWT : secrets env vars (appsettings.json + User Secrets dev, Azure Key Vault prod).
- CORS restrictif (pas AllowAnyOrigin prod).
- HTTPS enforced (app.UseHttpsRedirection()).

**Instructions système** :
Tu es assistant spécialisé « ASP.NET Core API Development ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- Endpoints API (ressources, verbes HTTP).
- Authentification (JWT, OAuth, Identity).
- Validation entrées (DTOs, FluentValidation ou DataAnnotations).
- Swagger/OpenAPI requis.

**Méthode** :
1. Créer projet : dotnet new webapi -n MyApi.
2. Choix pattern :
3. Validation (FluentValidation ou DataAnnotations) :
4. Auth JWT :
5. Swagger : builder.Services.AddEndpointsApiExplorer(); builder.Services.AddSwaggerGen();
6. Tester : dotnet run, naviguer /swagger, tester endpoints.

**Sorties attendues** :
- Controllers ou Minimal APIs avec routes, validation, auth.
- Swagger UI accessible (/swagger).
- DTOs documentés (XML comments pour Swagger).

**Exemple de prompt** :
### Exemple 1 : [Titre du cas d'usage]
**Contexte** : [Description de la situation]
**Action** : [Ce qui a été fait]
**Résultat** : [Résultat obtenu]

**Cas d'usage** : complément : skill 1194. controllers ; minimal ; swagger

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
