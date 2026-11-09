---
num: 1887
resume: "Organiser un monorepo avec Nx (affected + remote cache Nx Cloud), Turborepo (pipeline turbo.json) ou Bazel (hermetic + remote execution) — ne builder/tester que ce qui a changé pour garder une CI rapide. Étape 1 : Nx : nx.json (targetDefaults, cache), nx affected -t test/build (ne teste que l'impacté), Nx Cloud pour le remote cache partagé."
date_ajout: "2026-11"
nom: "Monorepo : Nx, Turborepo, Bazel (cache, affected, remote cache)"
emoji: "🏗️"
domaine: "Développement"
signal: "Organiser un monorepo en 2027 avec Nx (cache local + Nx Cloud remote, 'affected' pour ne builder/tester que ce qui a changé, générateurs de code) ou Turborepo (Vercel, pipeline déclaratif, remote cache) ou Bazel (build/test hermetic, remote execution, plus rapide à très grande échelle, courbe d'apprentissage). Critère : temps CI avant/après 'affected'. N'utilise pas de monorepo sans outil de cache (CI explose)."
mot_cle: "monorepo Nx Turborepo Bazel cache remote cache affected ne builder que le changé générateurs CI hermetic remote execution"
nom_court: "Monorepo"
branche: "D1"
synonymes: ["Nx affected : ne builder/tester que les projets impactés par le commit (CI -70 %)", "Turborepo (Vercel) : pipeline turbo.json + remote cache, plus simple que Nx", "Bazel : remote execution + cache hermetic pour les très gros repos (Google-scale)"]
cross_refs: [1413, 1885, 1884]
tags: ["2027"]
depends_on: [1413]
---

## 1887. 🏗️ Monorepo : Nx, Turborepo, Bazel (cache, affected, remote cache)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Organiser un monorepo avec Nx (affected + remote cache Nx Cloud), Turborepo (pipeline turbo.json) ou Bazel (hermetic + remote execution) — ne builder/tester que ce qui a changé pour garder une CI rapide.

**Quand l'utiliser (triggers)** :
- la CI du monorepo fait 45 min pour un changement de 10 lignes : activer affected (Nx)
- Nx vs Turborepo vs Bazel : lequel selon la taille du repo
- remote cache : partager le cache de build entre les devs et la CI (Nx Cloud/Turborepo)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es développeur / plateforme dev. Tu choisis l'outil selon la taille (Turborepo < 50 apps, Nx 50-500, Bazel > 500 ou besoin hermetic), tu actives le remote cache, et tu mesures le gain CI (affected). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le monorepo (apps/ + packages/)
- L'outil choisi (Nx/Turborepo/Bazel)
- La CI (1413)

**Méthode** :
1. Nx : nx.json (targetDefaults, cache), nx affected -t test/build (ne teste que l'impacté), Nx Cloud pour le remote cache partagé.
2. Turborepo : turbo.json pipeline (build dependsOn ^build, test dependsOn build), remote cache Vercel.
3. Bazel : BUILD files, bazel test //... --remote_cache, hermetic (pas de dépendance réseau).
4. Mesurer : temps CI avant/après affected (objectif -60 %), taille du cache.

**Sorties attendues** :
- Le monorepo outillé (affected + remote cache)
- La CI accélérée (mesurée : -60 %)
- Les générateurs de code (Nx) ou conventions (Turborepo) en place

**Exemple de prompt** :
> « Monorepo 30 apps : avant = CI 45 min (tout build/test). Après Nx affected + Nx Cloud : un commit sur packages/ui ne build/test que app-web (dépendant) -> CI 6 min, cache partagé entre devs. »

**Cas d'usage** : Grande codebase. S'articule avec skills 1413, 1885, 1884, 1886.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
