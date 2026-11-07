---
num: 1609
nom: "Tauri vs PWA : app desktop légère depuis le web (2027)"
emoji: "🖥️"
domaine: "Développement"
signal: "Choisir en 2027 entre Tauri (app desktop native légère embarquant le webview système + backend Rust, ~600 kB contre 100+ Mo pour Electron) et PWA (installable depuis le navigateur, offline, notifications). Utilise selon le besoin (accès système fort → Tauri, distribution web → PWA). N'utilise pas Electron si la taille compte."
mot_cle: "tauri vs PWA vs electron app desktop légère 2027"
nom_court: "Tauri/PWA"
branche: "D1"
synonymes: ["app desktop 600 kB avec tauri (pas electron)", "PWA installable offline notifications push", "tauri backend rust webview système"]
cross_refs: [1608, 607, 545]
tags: ["2027"]
depends_on: [607]
---

## 1609. 🖥️ Tauri vs PWA : app desktop légère depuis le web (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Choisir en 2027 entre Tauri (desktop natif léger : webview système + backend Rust, ~600 kB) et PWA (installable navigateur, offline) selon le besoin d'accès système, avec comparatif Electron (lourd).

**Quand l'utiliser (triggers)** :
- Notre app desktop Electron fait 150 Mo, alléger
- tauri 600 kB vs electron 150 Mo
- PWA installable offline vs app native

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es dev desktop léger. Tu compares : Tauri (Rust + webview OS, accès fichiers/notifs natif via commandes signées, taille ~600 kB), PWA (manifest + service worker, store optionnel), Electron (lourd mais mature). Règle : accès système fort → Tauri ; distribution web simple → PWA. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'app web existante (front)
- Le besoin d'accès système (fichiers, notifs, barre menu)
- La cible (Windows/Mac/Linux, store ?)

**Méthode** :
1. PWA d'abord (rapide) : manifest.webmanifest (icônes, nom, theme), service worker (cache offline, cache-first), install prompt, notifs push (FCM/APNs).
2. Si besoin système : Tauri — npm create tauri, front dans src-tauri, commandes Rust signées (tauri.conf.json allowlist), build ~600 kB.
3. Tester : offline, install, notif, accès fichier (Tauri dialog).
4. Distribuer : store (App Store/Google Play via Tauri mobile) ou téléchargement direct.

**Sorties attendues** :
- La PWA installable (offline, notifs) ou l'app Tauri (~600 kB)
- Le comparatif Tauri/PWA/Electron avec tailles mesurées
- Le store ou le téléchargement configuré

**Exemple de prompt** :
> « Notre app desktop Electron fait 150 Mo et démarre lentement : refais-la en Tauri (Rust + webview système, ~600 kB, accès fichiers/notifs natifs) — ou en PWA si pas besoin système. »

**Cas d'usage** : Apps desktop légères, outils internes, PWA grand public. S'articule avec skills 1608 (Wasm), 607 (publication mobile) et 545 (site statique).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
