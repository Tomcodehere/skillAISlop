---
num: 1765
resume: "Tracer l'exécution des agents IA (appels d'outils MCP, lectures de fichiers, commandes) via les spans sémantiques gen_ai.* d'OpenTelemetry, et choisir une plateforme d'observabilité agent (self-host, managé ou proxy). Étape 1 : Identifier tous les tool calls de l'agent (MCP tools, read_file, run_shell) et les wrapper dans des spans gen_ai.tool.call."
date_ajout: "2026-11"
nom: "Observabilité de la couche MCP et des appels d'outils des agents"
emoji: "🔌"
domaine: "Data & IA"
signal: "Observer en 2027 ce que font réellement les agents IA : chaque appel d'outil (tool call), lecture de fichier, commande shell, appel MCP (Model Context Protocol) trace via les spans gen_ai.* d'OpenTelemetry, sur 7 types de plateformes (self-host, managé, proxy : Langfuse, Helicone, Datadog, Arize). Utilise pour debugger un agent qui boucle ou coute cher."
mot_cle: "observabilite agents IA couche MCP tool calls spans gen_ai OpenTelemetry Langfuse Helicone 2027"
nom_court: "Observabilité agents/MCP"
branche: "D14"
synonymes: ["tracer chaque tool call de mon agent IA (MCP, fichiers, shell)", "7 plateformes d'observabilité agent : self-host vs managé vs proxy", "cout par requete agent : tokens entree sortie et appels d'outils"]
cross_refs: [1750, 1767, 1751]
tags: ["2027"]
depends_on: [1750]
---

## 1765. 🔌 Observabilité de la couche MCP et des appels d'outils des agents (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Tracer l'exécution des agents IA (appels d'outils MCP, lectures de fichiers, commandes) via les spans sémantiques gen_ai.* d'OpenTelemetry, et choisir une plateforme d'observabilité agent (self-host, managé ou proxy).

**Quand l'utiliser (triggers)** :
- mon agent boucle 20 fois sur le meme outil, pourquoi ?
- combien coute chaque requete agent en tokens et appels d'outils ?
- choisir entre Langfuse (self-host), Helicone (proxy) et Datadog (managé)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es ingénieur IA / observabilité. Tu instrumentes les tool calls (MCP, shell, fichiers) en spans gen_ai.*, tu traces tokens entrée/sortie et latence par appel d'outil, et tu déploies une des 7 plateformes (self-host/managé/proxy) selon la conformité requise. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'agent et ses outils (MCP, shell, fichiers)
- La plateforme d'observabilité choisie
- Les exigences de conformité (données sensibles)

**Méthode** :
1. Identifier tous les tool calls de l'agent (MCP tools, read_file, run_shell) et les wrapper dans des spans gen_ai.tool.call.
2. Tracer pour chaque appel : arguments (sanitisés), résultat, latence, tokens consommés.
3. Choisir la plateforme : self-host (Langfuse) si données sensibles, proxy (Helicone) pour du rapide, managé (Datadog, Arize) pour l'enterprise.
4. Analyser : agent qui boucle, outil le plus lent, coût par requête (1767).

**Sorties attendues** :
- Les tool calls tracés en spans gen_ai.*
- La plateforme déployée et le dashboard agent
- Le rapport : boucles détectées, outil le plus coûteux

**Exemple de prompt** :
> « Agent de support qui boucle : les spans gen_ai.tool.call montrent 20 appels identiques à search_docs avec les mêmes arguments — bug de boucle detecte en 5 min, cout de la requete 0,04 $ en tokens traces. »

**Cas d'usage** : Déboguer et coûter les agents. S'articule avec skills 1750 (OTel GenAI), 1767 (coût LLM), 1751 (SLO LLM).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
