---
num: 1608
resume: "Faire tourner du code compilé hors navigateur en 2027 avec Wasm + WASI 2.0 (fichiers, réseau, horloge) et le Component Model (échange typé entre langages) — pour CLI, plugins, edge, embarqué. Étape 1 : Compiler en wasm32-wasip2 (Rust : cargo build --target wasm32-wasip2)."
lang: "fr"
date_ajout: "2026-11"
nom: "WebAssembly hors navigateur : WASI 2.0 et composants"
emoji: "🧱"
domaine: "Développement"
signal: "Faire tourner du code compilé (Rust/C/C++/Go) hors navigateur en 2027 avec WebAssembly + WASI 2.0 (accès fichiers, réseau, horloge standardisés) et le modèle de composants (Component Model : échange de valeurs typées entre langages). Utilise pour CLI, plugins, edge, embarqué. N'utilise pas pour du front (1606/1607)."
mot_cle: "webassembly WASI 2.0 component model hors navigateur CLI plugins edge 2027"
nom_court: "Wasm/WASI"
branche: "D1"
synonymes: ["faire tourner du Rust compilé en wasm partout (WASI)", "component model wasm échange typé entre langages", "wasm sur serveur edge CLI 2027"]
cross_refs: [1607, 1606, 84]
tags: ["2027"]
depends_on: [84]
---

## 1608. 🧱 WebAssembly hors navigateur : WASI 2.0 et composants (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Faire tourner du code compilé hors navigateur en 2027 avec Wasm + WASI 2.0 (fichiers, réseau, horloge) et le Component Model (échange typé entre langages) — pour CLI, plugins, edge, embarqué.

**Quand l'utiliser (triggers)** :
- Mon binaire Rust doit tourner partout (serveur, edge, CLI)
- WASI 2.0 : accès fichiers/réseau standardisé
- component model : plugin wasm échangeable

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es dev Wasm. Tu montres : compiler Rust/C en .wasm (wasm32-wasip2), exécuter avec wasmtime/wasmer/node, WASI 2.0 (préopen de dossiers, sockets), et le Component Model (wit-bindgen) pour des plugins typés. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le code source (Rust/C/Go)
- Le runtime cible (wasmtime, wasmer, node, Cloudflare Workers 1612)
- Les besoins d'accès (fichiers, réseau)

**Méthode** :
1. Compiler en wasm32-wasip2 (Rust : cargo build --target wasm32-wasip2).
2. Exécuter : wasmtime run mon.wasm (CLI), ou node/cloudflare workers (edge), avec préopen de dossiers autorisés (sécurité sandbox).
3. Component Model : définir l'interface en WIT, générer les bindings (wit-bindgen), échanger des records/listes typés entre host et composant.
4. Mesurer : démarrage à froid (~ms, bien meilleur qu'un conteneur), taille du .wasm.

**Sorties attendues** :
- Le binaire Wasm qui tourne sur CLI/edge/serveur
- Le sandbox WASI (accès restreint) configuré
- Le plugin Component Model typé (WIT)

**Exemple de prompt** :
> « Mon outil Rust doit tourner sur serveur, edge Cloudflare et CLI client : compile-le en wasm32-wasip2, fais-le tourner avec wasmtime (CLI) et Workers (edge), WASI 2.0 pour les fichiers. »

**Cas d'usage** : CLI, plugins, edge serverless, embarqué, sandbox. S'articule avec skills 1607 (ML client), 1606 (WebGPU) et 84 (algos).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
