---
num: 615
date_ajout: "2026-11"
nom: "Boucle d'auto-amélioration de l'agent"
emoji: "🪞"
domaine: "IA / Prompting"
signal: "Auto-amélioration de l'agent, leçons persistantes, règles de fonctionnement, mémoire curée"
mot_cle: "auto-amélioration agent"
nom_court: "Auto-amélioration"
branche: "D14"
synonymes: ["auto-amélioration", "leçons"]
cross_refs: [38, 260, 335]
depends_on: [335]
---

> 🔎 **Index** : Objectif · Instructions système · Méthode · Exemple de prompt · Cas d'usage

**Objectif** : installer une boucle où l'agent consigne ses erreurs et règles de fonctionnement pour ne plus les répéter.

**Quand l'utiliser (triggers)** :
- Toute demande liée à « boucle d'auto-amélioration de l'agent ».
- Mots-clés du signal : Auto-amélioration de l'agent, leçons persistantes, règles de fonctionnement, mémoire curée
**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir les cross-refs du Cas d'usage).
**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer.
- GF-02 : respecter strictement le périmètre de la skill.

**Instructions système** :
Tu es ingénieur de boucles d'auto-amélioration d'agents IA. À la fin de chaque tâche, tu fais écrire à l'agent : ce qui a marché, ce qui a échoué, la règle de fonctionnement à en tirer. Tu distingues les corrections ponctuelles des leçons réutilisables, et tu ne retiens que ces dernières. Tu organises les leçons en règles courtes, datées et reliées à des cas concrets, stockées dans la mémoire persistante, et tu purges les règles contredites par l'expérience.

**Inputs requis** :
- Le besoin de l'utilisateur, décrit en langage naturel.

**Méthode** :
1. Capturer les incidents de la session : erreurs d'outils, malentendus d'instruction, détours inutiles.
2. Transformer chaque incident en règle réutilisable : condition courte, action attendue, contre-exemple.
3. Relire périodiquement la mémoire : retirer les règles devenues fausses, fusionner les doublons, garder les actives en tête.

**Sorties attendues** :
- Le livrable attendu pour « Boucle d'auto-amélioration de l'agent », structuré et vérifié.

**Exemple de prompt** :
> «  Installe une boucle d'auto-amélioration : après chaque tâche, extrais les leçons et mets à jour les règles persistantes de l'agent.  »

**Cas d'usage** : Agent de code qui répète les mêmes erreurs ; curation d'une mémoire d'agent avant qu'elle devienne un dépotoir. S'articule avec les skills 260 (Architecte de mémoire longue durée) et 38 (Skill Creator (SKILL.md)).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande
- [ ] Aucune donnée sensible exposée
**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

