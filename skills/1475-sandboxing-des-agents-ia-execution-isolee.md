---
num: 1475
resume: "Faire exécuter un agent IA dans un sandbox en 2027 : conteneur jetable (gVisor/Firecracker) par tâche, réseau en allowlist, aucun secret, FS éphémère, timeout strict, et logs de tout ce qui sort. Étape 1 : Choisir l'isolation : conteneur gVisor (léger) ou microVM Firecracker (fort) par exécution."
lang: "fr"
date_ajout: "2026-11"
nom: "Sandboxing des agents IA (execution isolee)"
emoji: "🏖️"
domaine: "Data & IA"
signal: "Exécuter les actions d'un agent IA dans un bac à sable (sandbox) en 2027 : conteneur jetable par tâche (Docker/gVisor/Firecracker), réseau restreint (allowlist), pas de secrets, filesystem éphémère, timeout, logs. Utilise quand un agent exécute du code ou touche des fichiers. N'utilise pas pour un agent 100 % lecture seule."
mot_cle: "sandbox agent IA conteneur jetable gVisor firecracker réseau restreint"
nom_court: "Sandbox agent"
branche: "D14"
synonymes: ["exécuter code agent en sécurité", "conteneur jetable par tâche agent", "réseau allowlist agent IA"]
cross_refs: [818, 194, 723]
tags: ["2027"]
depends_on: [194]
---

## 1475. 🏖️ Sandboxing des agents IA (execution isolee, 2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Faire exécuter un agent IA dans un sandbox en 2027 : conteneur jetable (gVisor/Firecracker) par tâche, réseau en allowlist, aucun secret, FS éphémère, timeout strict, et logs de tout ce qui sort.

**Quand l'utiliser (triggers)** :
- Mon agent exécute du code Python généré, c'est dangereux
- Isoler l'exécution d'un agent dans un conteneur
- Quels ports ouvrir au sandbox ?

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte sécurité agents. Tu donnes la recette : microVM Firecracker ou conteneur gVisor, image minimale, --network avec allowlist (API approuvées seules), pas de volume monté, secrets injectés en env à la volée, timeout 60 s, tout loggé. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les actions que l'agent peut faire (code, fichiers, réseau)
- L'isolation choisie (Docker, gVisor, Firecracker)
- Les ressources à autoriser (API externes)

**Méthode** :
1. Choisir l'isolation : conteneur gVisor (léger) ou microVM Firecracker (fort) par exécution.
2. Image minimale (python:slim) sans outils, user non-root, FS read-only sauf /tmp éphémère.
3. Réseau : none par défaut, ou allowlist (proxy qui ne laisse passer que les domaines approuvés).
4. Secrets : injectés en variables d'env à la création, jamais dans l'image ni les logs.
5. Timeout (60 s) + kill, logs stdout/stderr capturés, résultat renvoyé à l'agent.

**Sorties attendues** :
- Le sandbox d'exécution d'agent configuré
- La politique réseau (allowlist) et timeout
- Les logs d'exécution capturés

**Exemple de prompt** :
> « Notre agent code exécute du Python arbitraire : mets-le dans un sandbox (Firecracker jetable, réseau allowlist via proxy, pas de secrets, timeout 60 s). »

**Cas d'usage** : Agents de code, data analysis auto, actions sur fichiers. S'articule avec skills 818 (injection web), 194 (garde-fous) et 723 (SOC agentique).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
