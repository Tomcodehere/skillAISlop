---
num: 1110
resume: "Créer Dockerfiles optimisés (multi-stage builds, minimisation layers, sécurité, taille image). Étape 1 : Analyser app (runtime, dépendances build vs runtime)."
lang: "fr"
date_ajout: "2026-11"
nom: "Dockerfile Best Practices"
emoji: "💻"
domaine: "Développement"
signal: "Créer Dockerfiles optimisés (multi-stage builds, minimisation layers, sécurité, taille image)."
mot_cle: "dockerfile-best-practices"
nom_court: "Dockerfile Best Practices"
branche: "D1"
synonymes: ["dockerfile", "optimise", "image"]
cross_refs: [79, 1220, 1310]
tags: ["2027"]
---

## 1110. 💻 Dockerfile Best Practices

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Créer Dockerfiles optimisés (multi-stage builds, minimisation layers, sécurité, taille image).

**Quand l'utiliser (triggers)** :
- « crée Dockerfile », « optimise image Docker », « multi-stage builds », « sécurise image ».
- Containerisation application.
- Réduction taille images ou amélioration sécurité.

**Hors périmètre** :
- docker-compose orchestration → skill Docker Compose Orchestration.
- Kubernetes deployment → l'agent d'architecture cloud.
- Podman Quadlet → l'agent de scripting système.

**Garde-fous** :
- Multi-stage obligatoire (réduction taille 50-80%).
- USER non-root (sécurité).
- Base images officielles ou distroless (pas images random Docker Hub).
- HEALTHCHECK défini (monitoring liveness).
- Pas de secrets hardcodés (ARG secrets build-time invalide, env vars runtime).

**Instructions système** :
Tu es assistant spécialisé « Dockerfile Best Practices ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- Application à containeriser (runtime, dépendances).
- Base image préférée (Alpine, Debian slim, distroless, scratch).
- Contraintes (taille image, sécurité, performance build).

**Méthode** :
1. Analyser app (runtime, dépendances build vs runtime).
2. Choisir base images :
3. Multi-stage Dockerfile :
4. .dockerignore : node_modules, .git, tests/, *.md (sauf README).
5. Build : docker build -t myapp:latest .
6. Scan sécurité : trivy image myapp:latest.

**Sorties attendues** :
- Dockerfile multi-stage avec commentaires.
- .dockerignore.
- Taille finale image (docker images).
- Rapport scan sécurité (Trivy, Snyk).

**Exemple de prompt** :
### Exemple 1 : [Titre du cas d'usage]
**Contexte** : [Description de la situation]
**Action** : [Ce qui a été fait]
**Résultat** : [Résultat obtenu]

**Cas d'usage** : complément : skill 79. dockerfile ; optimise ; image

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
