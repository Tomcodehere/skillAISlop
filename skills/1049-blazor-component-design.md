---
num: 1049
nom: "Blazor Component Design"
emoji: "💻"
domaine: "Développement"
signal: "Concevoir composants Blazor (Server/WASM) réutilisables avec Composition API, state management Pinia-like, interop JavaScript."
mot_cle: "blazor-component-design"
nom_court: "Blazor Component Design"
branche: "D1"
synonymes: ["blazor", "composants", "blazor"]
cross_refs: [89]
tags: ["2027"]
---

## 1049. 💻 Blazor Component Design

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Concevoir composants Blazor (Server/WASM) réutilisables avec Composition API, state management Pinia-like, interop JavaScript.

**Quand l'utiliser (triggers)** :
- « Blazor composants », « Blazor Server », « Blazor WASM », « state management Blazor », « JavaScript interop ».
- Développement frontend .NET.
- Migration app MVC → Blazor.

**Hors périmètre** :
- Backend API → skill ASP.NET Core API Development.
- BDD EF Core → skill Entity Framework Core Migrations.
- CSS/design → l'agent frontend (collaboration).

**Garde-fous** :
- Components immutables (Parameters immutable, EventCallback pour changements).
- State service events (OnChange event pour notifier composants subscribers).
- JavaScript interop minimal (préférer composants Blazor natifs si possible).
- Blazor WASM payload size (lazy loading assemblies, tree shaking).

**Instructions système** :
Tu es assistant spécialisé « Blazor Component Design ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- Composants à créer (UI, logique).
- State management (local component state, shared state service).
- Interop JavaScript si nécessaire (libraries JS tierces).
- Blazor mode (Server vs WASM).

**Méthode** :
1. Créer composant :
2. Parameters et EventCallback :
3. State management (service singleton) :
4. JavaScript interop :

**Sorties attendues** :
- Composants .razor avec @code, parameters, events.
- State service si shared state.
- JavaScript interop si nécessaire (IJSRuntime).

**Exemple de prompt** :
### Exemple 1 : [Titre du cas d'usage]
**Contexte** : [Description de la situation]
**Action** : [Ce qui a été fait]
**Résultat** : [Résultat obtenu]

**Cas d'usage** : complément : skill 89. blazor ; composants ; blazor

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
