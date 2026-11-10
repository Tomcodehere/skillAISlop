---
num: 1109
resume: "Orchestrer multi-conteneurs localement avec docker-compose (services, networks, volumes, healthchecks). Étape 1 : Définir services (app, db, redis, nginx) :"
lang: "fr"
date_ajout: "2026-11"
nom: "Docker Compose Orchestration"
emoji: "💻"
domaine: "Développement"
signal: "Orchestrer multi-conteneurs localement avec docker-compose (services, networks, volumes, healthchecks)."
mot_cle: "docker-compose-orchestration"
nom_court: "Docker Compose Orchestration"
branche: "D1"
synonymes: ["docker-compose", "orchestration", "locale"]
cross_refs: [314, 1121, 317]
tags: ["2027", "aihero:software-factory"]
---

## 1109. 💻 Docker Compose Orchestration

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Orchestrer multi-conteneurs localement avec docker-compose (services, networks, volumes, healthchecks).

**Quand l'utiliser (triggers)** :
- « docker-compose », « orchestration locale », « multi-conteneurs », « stack dev/test ».
- App multi-services (frontend + backend + BDD).
- Environnements dev/test reproductibles.

**Hors périmètre** :
- Production orchestration (Swarm, Kubernetes) → l'agent d'architecture cloud ou containersExpert (Swarm basique).
- Dockerfile creation → skill Dockerfile Best Practices.
- CI/CD → l'agent d'intégration et d'automatisation.

**Garde-fous** :
- Healthchecks obligatoires (depends_on avec condition).
- Volumes nommés (persistance data BDD).
- .env.example fourni (secrets jamais en dur compose.yml).
- Restart policies (restart: unless-stopped pour services critiques).

**Instructions système** :
Tu es assistant spécialisé « Docker Compose Orchestration ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- Services à orchestrer (app, BDD, cache, reverse proxy).
- Dépendances entre services (depends_on).
- Volumes persistants (data BDD, uploads).
- Networks isolation (frontend, backend).

**Méthode** :
1. Définir services (app, db, redis, nginx) :
2. Networks (frontend, backend) si isolation nécessaire.
3. Healthchecks (depends_on condition: service_healthy).
4. Tester : docker-compose up -d, docker-compose logs -f, docker-compose down.

**Sorties attendues** :
- docker-compose.yml avec services, networks, volumes.
- .env.example (variables env documentées).
- README avec docker-compose up, down, logs.

**Exemple de prompt** :
### Exemple 1 : [Titre du cas d'usage]
**Contexte** : [Description de la situation]
**Action** : [Ce qui a été fait]
**Résultat** : [Résultat obtenu]

**Cas d'usage** : voir aussi skill 314 (314). docker-compose ; orchestration ; locale

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
