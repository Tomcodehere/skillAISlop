---
num: 1614
resume: "Migrer un projet Webpack legacy vers Vite en 2027 sans régression : mapping loaders→plugins, alias/env/proxy dev, assets, polyfills, et preuve que le build prod est équivalent (taille, perfs, tests). Étape 1 : Inventorier webpack.config : entry, loaders, plugins, alias, define, devServer.proxy, output."
lang: "fr"
date_ajout: "2026-11"
nom: "Migration Webpack vers Vite : guide pratique"
emoji: "🔄"
domaine: "Développement"
signal: "Migrer un projet Webpack legacy vers Vite en 2027 : mapping des loaders → plugins Vite, config vite.config (alias, define/env, proxy dev), gestion des assets (public/), polyfills, et vérification que le build prod est identique (taille, perfs). Utilise quand Webpack ralentit le dev/CI. N'utilise pas si le projet marche bien (ne pas toucher)."
mot_cle: "migrer webpack vers vite guide loaders plugins alias env proxy"
nom_court: "Webpack→Vite"
branche: "D1"
synonymes: ["migrer mon projet webpack legacy vers vite", "loaders webpack vers plugins vite équivalent", "vite proxy dev server remplace webpack-dev-server"]
cross_refs: [1600, 1413, 545]
tags: ["2027"]
depends_on: [1600]
---

## 1614. 🔄 Migration Webpack vers Vite : guide pratique (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Migrer un projet Webpack legacy vers Vite en 2027 sans régression : mapping loaders→plugins, alias/env/proxy dev, assets, polyfills, et preuve que le build prod est équivalent (taille, perfs, tests).

**Quand l'utiliser (triggers)** :
- Notre vieux projet Webpack met 30 s à démarrer en dev
- mapping loaders webpack (babel, sass) vers vite
- vite.config alias define env proxy dev 2027

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es dev migration. Tu fais le mapping : babel-loader→@vitejs/plugin-react (ou esbuild), css-loader/style-loader→CSS natif Vite, file-loader→assets, DefinePlugin→define, devServer.proxy→server.proxy, et tu valides par les tests + la taille du bundle. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le projet Webpack (webpack.config.js, loaders, plugins)
- Les tests (unitaires + e2e 252)
- La taille/perf du build actuel (baseline)

**Méthode** :
1. Inventorier webpack.config : entry, loaders, plugins, alias, define, devServer.proxy, output.
2. Créer vite.config.ts : plugins équivalents (react/swc, legacy si besoin), resolve.alias, define, server.proxy, build.outDir.
3. Assets : déplacer dans public/ ce qui était file-loader/copy-webpack-plugin ; imports d'images → Vite gère nativement.
4. En dev : lancer vite, vérifier proxy API, HMR, variables d'env (VITE_ prefix).
5. Valider : tests passent, build prod taille équivalente ou meilleure, perfs dev (cold start mesuré).

**Sorties attendues** :
- Le projet migré sur Vite (dev rapide, build propre)
- Le mapping loaders→plugins documenté
- La preuve : tests verts + build prod équivalent

**Exemple de prompt** :
> « Notre projet legacy Webpack met 30 s à démarrer en dev : migre vers Vite (mapping des loaders, alias/env/proxy, public/), tests verts + build prod équivalent mesuré. »

**Cas d'usage** : Legacy front, monorepos. S'articule avec skills 1600 (Rolldown), 1413 (CI) et 545 (statique).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
