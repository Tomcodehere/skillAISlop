---
num: 1604
nom: "TanStack Start + tRPC : full-stack type-safe (2027)"
emoji: "🔐"
domaine: "Développement"
signal: "Construire une app full-stack type-safe en 2027 avec TanStack Start (React, routing serveur) + tRPC (API typée de bout en bout, sans schéma OpenAPI à maintenir) : types partagés client/serveur, validation zod. Alternative à Next.js + REST. Utilise pour une app métier interne moderne. N'utilise pas pour un site content-first (voir 1603)."
mot_cle: "tanstack start trpc full-stack type-safe zod 2027"
nom_court: "TanStack+tRPC"
branche: "D1"
synonymes: ["API type-safe de bout en bout (tRPC)", "tanstack start react full-stack 2027", "trpc vs REST vs GraphQL choisir"]
cross_refs: [526, 87, 1249]
tags: ["2027"]
depends_on: [526]
---

## 1604. 🔐 TanStack Start + tRPC : full-stack type-safe (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Construire une app full-stack type-safe en 2027 avec TanStack Start + tRPC : procédures typées appelées comme des fonctions (pas d'URL/JSON à parser), validation zod partagée, autocomplétion de bout en bout.

**Quand l'utiliser (triggers)** :
- Notre API REST a des bugs de contrat client/serveur
- tRPC : appeler l'API comme une fonction typée
- tanstack start vs next.js en 2027

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es dev full-stack. Tu montres : router tRPC (procédures avec input zod), client tRPC (hooks typés, trpc.user.list.useQuery()), TanStack Start pour le routing/SSR, une mutation avec invalidation de cache. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le projet React (TanStack Start)
- Les entités métier (user, commande...) et leurs règles (zod)
- La base de données (Prisma/Drizzle)

**Méthode** :
1. Initialiser TanStack Start, installer @trpc/server + @trpc/client + @tanstack/react-query.
2. Définir les schémas zod (CreateUserSchema), le router tRPC (procedures avec .input().mutation/query).
3. Côté client : createTRPCReact, utiliser les hooks typés (plus d'URL à taper, plus de cast).
4. Mutations : await trpc.user.create.mutate(), puis queryClient.invalidateQueries pour rafraîchir.
5. Déployer (SSR ou statique + edge 1612), tester les contrats (types à la compilation).

**Sorties attendues** :
- L'app TanStack Start + tRPC fonctionnelle
- Les contrats typés de bout en bout (erreur de contrat = erreur de compilation)
- Le comparatif tRPC vs REST vs GraphQL documenté

**Exemple de prompt** :
> « Notre app interne a des bugs de contrat API (champs renommés, types cassés) : migre en TanStack Start + tRPC (procédures typées, zod, invalidation auto) — plus d'erreur de contrat possible. »

**Cas d'usage** : Apps métier internes, dashboards, outils SaaS. S'articule avec skills 526 (API REST/GraphQL), 87 (OpenAPI) et 1249 (React).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
