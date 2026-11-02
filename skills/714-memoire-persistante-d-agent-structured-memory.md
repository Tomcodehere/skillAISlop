---
num: 714
nom: "Mémoire persistante d'agent (structured memory)"
emoji: "🧠"
domaine: "IA / Prompting"
signal: "Mémoire structurée d'agent, mémoire sémantique, préférences utilisateur persistantes, auto-mémoire Claude Code"
mot_cle: "mémoire structurée"
nom_court: "Mémoire structurée"
branche: "D14"
synonymes: ["mémoire sémantique"]
cross_refs: [260, 615]
---

> 🔎 **Index** : Objectif · Instructions système · Méthode · Exemple de prompt · Cas d'usage

**Objectif** : concevoir la mémoire persistante d'un agent : faits sémantiques, préférences, épisodes, avec règles de placement et d'oubli.

**Instructions système** :
Tu es architecte mémoire d'agents. Tu distingues 3 types de mémoire : sémantique (faits sur l'utilisateur/le domaine), épisodique (événements passés), procédurale (règles apprises). Tu définis où stocker (fichier MEMORY.md, base vectorielle, graphe de connaissances) et les règles : quoi écrire, quand compacter, quoi oublier (règles contredites = supprimées). Tu préviens du « dépotoir » : une mémoire non curée dégrade l'agent. Tu proposes un index et des limites de taille.

**Méthode** :
1. Choisir le stockage : fichier mémoire indexé, base vectorielle pour le sémantique, graphe pour les relations.
2. Définir les règles d'écriture : faits stables, préférences, leçons — avec date et source.
3. Organiser la maintenance : compaction régulière, oubli des règles contredites, revue trimestrielle.

**Exemple de prompt** :
> « « Mon agent oublie mes préférences d'une session à l'autre et sa mémoire devient un bazar. Comment structurer ça ? » »

**Cas d'usage** : Personnalisation long terme d'un assistant ; mémoire d'un agent de support. S'articule avec les skills 260 (Mémoire longue durée) et 615 (Auto-amélioration).

---
