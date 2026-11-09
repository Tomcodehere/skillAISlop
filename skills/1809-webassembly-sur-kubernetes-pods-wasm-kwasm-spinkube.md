---
num: 1809
resume: "Exécuter des workloads WebAssembly comme pods Kubernetes first-class (kwasm ou SpinKube/wasmCloud) : images Wasm légères, cold start ~1 ms, isolation renforcée — pour fonctions edge, plugins, calcul sandboxé dans le cluster. Étape 1 : Installer kwasm (RuntimeClass wasm) ou SpinKube (operator wasmCloud) sur les nœuds dédiés."
lang: "fr"
date_ajout: "2026-11"
nom: "WebAssembly sur Kubernetes : pods Wasm (kwasm, SpinKube)"
emoji: "🧩"
domaine: "Développement"
signal: "Faire tourner des workloads WebAssembly comme des pods Kubernetes first-class avec kwasm (Kubernetes Wasm) ou SpinKube (wasmCloud + Spin) : runtime containerd shim wasm, images Wasm plus petites, isolation plus forte qu'un conteneur, cold start ~1 ms (1794). Cas : fonctions edge dans le cluster, plugins, calcul sandboxé. k8s 1.36+ avec le runtime configuré. N'utilise pas pour des apps nécessitant un OS complet."
mot_cle: "kwasm SpinKube wasmCloud pods WebAssembly kubernetes containerd shim wasm cold start 1 ms"
nom_court: "Wasm sur k8s"
branche: "D16"
synonymes: ["faire tourner un .wasm comme pod k8s (kwasm containerd shim)", "SpinKube Spin operator pour workloads wasmCloud dans k8s", "pod wasm : image 2 Mo cold start 1 ms isolation forte vs conteneur"]
cross_refs: [1793, 1794, 1797]
tags: ["2027"]
depends_on: [1793]
---

## 1809. 🧩 WebAssembly sur Kubernetes : pods Wasm (kwasm, SpinKube)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Exécuter des workloads WebAssembly comme pods Kubernetes first-class (kwasm ou SpinKube/wasmCloud) : images Wasm légères, cold start ~1 ms, isolation renforcée — pour fonctions edge, plugins, calcul sandboxé dans le cluster.

**Quand l'utiliser (triggers)** :
- mon plugin wasm doit tourner dans le cluster k8s comme les autres pods
- kwasm vs SpinKube : lequel choisir
- pod wasm 2 Mo vs image docker 200 Mo : cold start 1 ms

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es ingénieur plateforme. Tu installes le runtime wasm sur les nœuds (containerd shim via kwasm ou SpinKube), tu déploies les pods avec class runtime wasm, et tu appliques les mêmes policies (Kyverno 1705, admission 1808). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les nœuds avec runtime wasm (kwasm/SpinKube)
- Les modules .wasm (compilés wasm32-wasip2, 1793)
- Les capacités (capabilities) du module (1794)

**Méthode** :
1. Installer kwasm (RuntimeClass wasm) ou SpinKube (operator wasmCloud) sur les nœuds dédiés.
2. Compiler le code en wasm32-wasip2 (1793), publier l'artifact OCI (1807).
3. Déployer le pod avec runtimeClassName: wasm + securityContext (capabilities limitées 1794).
4. Vérifier : cold start mesuré (~1 ms), isolation (le module ne voit que ses capabilities), métriques.

**Sorties attendues** :
- Les pods Wasm déployés via kwasm/SpinKube
- Le benchmark cold start wasm vs conteneur
- Les policies appliquées (1705/1808)

**Exemple de prompt** :
> « Fonction de filtre image (plugin .wasm 1,8 Mo) déployée comme pod kwasm dans le cluster : cold start 1 ms, isolé (capabilities : 1 dossier), vs un conteneur Docker de 200 Mo à 500 ms de cold start. »

**Cas d'usage** : Workloads sandboxés légers dans k8s. S'articule avec skills 1793 (WASI), 1794 (sandbox), 1797 (edge), 609, 1705.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
