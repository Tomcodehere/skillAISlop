---
num: 1794
date_ajout: "2026-11"
nom: "Plugins et sandbox en WebAssembly : sécurité par capacités"
emoji: "🧷"
domaine: "Développement"
signal: "Héberger du code non fiable en 2027 = WebAssembly + modèle de sécurité par capacités (capability-based) : le module n'a accès qu'à ce qu'on lui accorde explicitement (wasmtime run --dir=. app.wasm : seul le dossier courant est visible, le reste est refusé par défaut — pas de /etc/passwd, pas de réseau, pas d'env). Cold start ~1 ms (vs ~500 ms un conteneur Docker), empreinte quelques Mo. Cas : plugins, extensions, exécution de code client, fonctions serverless. N'utilise pas pour remplacer un conteneur quand il faut un OS complet."
mot_cle: "sandbox WebAssembly wasmtime --dir capabilites deny-by-default cold start 1 ms vs 500 ms conteneur plugin 2027"
nom_court: "Sandbox Wasm"
branche: "D12"
synonymes: ["wasmtime run --dir=. ./app.wasm : seul le dossier courant est accessible", "deny-by-default : pas d'acces reseau/dossiers/env sans --tcplisten/--env explicites", "cold start 1 ms Wasm vs 500 ms Docker pour les fonctions serverless/edge"]
cross_refs: [1793, 1797, 1721]
tags: ["2027"]
depends_on: [1793]
---

## 1794. 🧷 Plugins et sandbox en WebAssembly : sécurité par capacités (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Exécuter du code non fiable en sandbox WebAssembly en 2027 avec le modèle par capacités (deny-by-default : wasmtime --dir=. n'ouvre que le dossier courant), cold start ~1 ms, pour plugins, extensions et fonctions edge.

**Quand l'utiliser (triggers)** :
- heberger un plugin tiers dans mon appli sans risque
- wasmtime run --dir=/data --dir=/output app.wasm : rien d'autre n'est visible
- pourquoi le cold start Wasm est 100-500x plus rapide qu'un conteneur

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es développeur plateforme / sécurité applicative. Tu configures les capacités explicitement (--dir, --env, --tcplisten), jamais globalement, tu mesures le cold start, et tu compares avec un conteneur quand un OS complet est requis. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le module .wasm du plugin
- Les capacités requises (dossiers, env, réseau)
- Le runtime (Wasmtime)

**Méthode** :
1. Lister les capacités strictement nécessaires au plugin (1 dossier, 1 variable d'env).
2. Lancer : wasmtime run --dir=./data app.wasm — tout le reste (réseau, /etc, autres dossiers) est refusé par défaut.
3. Verifier : tentative d'accès à /etc/passwd depuis le module -> refus.
4. Mesurer : cold start ~1 ms, empreinte Mo vs conteneur 500 ms / centaines de Mo. Si besoin d'un OS complet (drivers, libs natives) : conteneur, pas Wasm.

**Sorties attendues** :
- Le plugin sandboxé avec capacités explicites
- La preuve deny-by-default (accès refusé hors capacités)
- Le benchmark cold start Wasm vs conteneur

**Exemple de prompt** :
> « Plateforme de plugins 2027 : chaque plugin .wasm tourne via wasmtime --dir=./workspace --env=API_KEY=... — le plugin tente de lire /etc/shadow : refusé (deny-by-default), cold start 1 ms, un plugin compromis n'a accès à rien d'autre. »

**Cas d'usage** : Sandbox de code tiers. S'articule avec skills 1793 (WASI), 1797 (edge), 1721 (eBPF runtime).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
