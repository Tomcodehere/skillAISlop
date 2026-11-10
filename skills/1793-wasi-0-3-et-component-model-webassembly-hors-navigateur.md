---
num: 1793
resume: "Adopter WebAssembly hors navigateur en 2027 : compiler en wasm32-wasip2 (WASI 0.3 async, WASI 1.0 ABI stable), composer des composants multi-langages via le Component Model (WIT), exécuter sur Wasmtime/WasmEdge/wazero pour edge, serverless, plugins, IoT. Étape 1 : Compiler : cargo build --target wasm32-wasip2 --release (WASI 0.3, async natif)."
lang: "fr"
date_ajout: "2026-11"
nom: "WASI 0.3 et Component Model : WebAssembly hors navigateur"
emoji: "🧩"
domaine: "Développement"
signal: "En 2027, WebAssembly sort définitivement du navigateur : WASI 0.2 stable, WASI 0.3 (fév. 2026) ajoute l'async natif (futures/streams), WASI 1.0 (fin 2026/début 2027) fige l'ABI long terme. Le Component Model (WIT) permet de composer des modules écrits en plusieurs langages (Rust, Go, C, Python) avec des appels de fonctions, pas du réseau. Cible : wasm32-wasip2 (cargo build --target wasm32-wasip2). Runtimes : Wasmtime (référence, Bytecode Alliance), WasmEdge (edge/IoT), wazero (Go, no CGO), Wasmer. Utilise pour edge, serverless, plugins, IoT."
mot_cle: "WASI 0.3 WASI 1.0 Component Model WIT wasm32-wasip2 Wasmtime WasmEdge wazero hors navigateur 2027"
nom_court: "WASI & Wasm serveur"
branche: "D1"
synonymes: ["cargo build --target wasm32-wasip2 pour compiler en WASI 0.3", "Component Model WIT : composer des modules Rust+Go+Python en un binaire", "WASI 1.0 fige l'ABI long terme fin 2026 debut 2027"]
cross_refs: [1794, 1797, 1770]
tags: ["2027"]
depends_on: [1608]
---

## 1793. 🧩 WASI 0.3 et Component Model : WebAssembly hors navigateur (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Adopter WebAssembly hors navigateur en 2027 : compiler en wasm32-wasip2 (WASI 0.3 async, WASI 1.0 ABI stable), composer des composants multi-langages via le Component Model (WIT), exécuter sur Wasmtime/WasmEdge/wazero pour edge, serverless, plugins, IoT.

**Quand l'utiliser (triggers)** :
- mon plugin doit tourner dans n'importe quel langage : Wasm Component
- WASI 1.0 est sorti, l'ABI est stable pour la prod
- Wasmtime vs WasmEdge vs wazero : lequel choisir ?

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es développeur plateforme / cloud. Tu cibles wasm32-wasip2, tu choisis le runtime selon le cas (Wasmtime référence, WasmEdge edge/IoT léger, wazero embarqué en Go), et tu composes des composants WIT multi-langages quand un plugin doit être polyglotte. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le code source (Rust/Go/C/Python compilable Wasm)
- Le cas d'usage : edge, serverless, plugin, IoT
- Le runtime choisi

**Méthode** :
1. Compiler : cargo build --target wasm32-wasip2 --release (WASI 0.3, async natif).
2. Pour un plugin polyglotte : definir l'interface en WIT, implementer en 2 langages, composer avec wit-component.
3. Choisir le runtime : Wasmtime (perf, Component Model complet), WasmEdge (edge/IoT, empreinte faible), wazero (embarque dans une appli Go, sans CGO).
4. Deployer : edge (1797), serverless, ou plugin embarque (1794).

**Sorties attendues** :
- Le binaire .wasm wasip2 compile
- Les composants WIT composes (si plugin polyglotte)
- Le choix de runtime documente avec criteres

**Exemple de prompt** :
> « Plugin de filtre image polyglotte 2027 : interface WIT (image -> image), cœur en Rust (perf) + filtre sepia en Python (compilé Wasm), composes en un composant, exécuté par Wasmtime dans l'app hôte. »

**Cas d'usage** : Wasm serveur/edge/plugin. S'articule avec skills 1794 (sandbox), 1797 (edge), 1770 (Rust).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
