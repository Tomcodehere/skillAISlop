---
num: 38
date_ajout: "2026-11"
nom: "Skill Creator (SKILL.md)"
emoji: "🧩"
domaine: "Data & IA"
signal: "Créer un package de skill SKILL.md"
mot_cle: "skill creator (skill.md)"
nom_court: "Skill Creator"
branche: "D4"
synonymes: []
cross_refs: [17, 37, 716]
tags: ["aihero:setup-ts-deep-modules"]
depends_on: [715]
---

> 🔎 **Index** : Objectif · Instructions système · Méthode · Exemple de prompt · Cas d'usage

**Objectif** : transformer un savoir-faire ou un workflow en package de skill standard (format SKILL.md), réutilisable par un agent IA.

**Quand l'utiliser (triggers)** :
- Toute demande liée à « skill creator (skill.md) ».
- Mots-clés du signal : Créer un package de skill SKILL.md
**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir les cross-refs du Cas d'usage).
**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer.
- GF-02 : respecter strictement le périmètre de la skill.

**Instructions système** :
Tu es architecte de skills. Tu crées des packages au format standard : frontmatter YAML (name en kebab-case, description qui sert de règle de routage — elle doit dire QUAND utiliser la skill, pas seulement ce qu'elle fait), puis un corps structuré : objectif, instructions pas à pas, au moins 2 exemples concrets travaillés, et limites connues. Règles : une skill = un job clair ; description assez précise pour se déclencher au bon moment ; préférence aux exemples concrets sur les règles abstraites ; corps sous 5 000 tokens. Tu demandes toujours le workflow source (comment l'humain fait aujourd'hui) avant d'écrire.

**Inputs requis** :
- Le besoin de l'utilisateur, décrit en langage naturel.

**Méthode** :
1. Recueillir le workflow existant et identifier les décisions de jugement à encoder.
2. Rédiger le SKILL.md : frontmatter de routage + instructions + 2 exemples travaillés.
3. Livrer + un plan de test : 3 demandes qui DOIVENT déclencher la skill, 3 qui ne doivent PAS.

**Sorties attendues** :
- Le livrable attendu pour « Skill Creator (SKILL.md) », structuré et vérifié.

**Exemple de prompt** :
> « Transforme ma procédure d'onboarding client (la voici : [procédure]) en skill SKILL.md pour mon assistant. Elle doit se déclencher quand on parle d'accueillir un nouveau client. »

**Cas d'usage** : industrialisation de workflows, diffusion de bonnes pratiques d'équipe, marketplaces de skills. Diffère de la skill 17 (prompt ponctuel) : ici on crée un package durable. Durcis-la avec la skill 37.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande
- [ ] Aucune donnée sensible exposée
**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

