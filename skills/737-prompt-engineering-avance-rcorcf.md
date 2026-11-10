---
num: 737
resume: "rédiger des prompts structurés et fiables avec le cadre RCORCF (Rôle, Contexte, Objectif, Ressources, Contraintes, Format). Étape 1 : Rédiger le prompt en RCORCF : rôle, contexte, objectif, ressources, contraintes, format de sortie."
lang: "fr"
date_ajout: "2026-11"
nom: "Prompt engineering avancé (RCORCF)"
emoji: "🧠"
domaine: "IA / Prompting"
signal: "Structurer un prompt, RCORCF, rôle contexte objectif ressources contraintes format, prompt système efficace"
mot_cle: "prompt structuré"
nom_court: "Prompt structuré"
branche: "D14"
synonymes: ["rcorcf"]
cross_refs: [17, 334, 817]
depends_on: [817]
---

> 🔎 **Index** : Objectif · Instructions système · Méthode · Exemple de prompt · Cas d'usage

**Objectif** : rédiger des prompts structurés et fiables avec le cadre RCORCF (Rôle, Contexte, Objectif, Ressources, Contraintes, Format).

**Quand l'utiliser (triggers)** :
- Toute demande liée à « prompt engineering avancé (rcorcf) ».
- Mots-clés du signal : Structurer un prompt, RCORCF, rôle contexte objectif ressources contraintes format, prompt système efficace
**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir les cross-refs du Cas d'usage).
**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer.
- GF-02 : respecter strictement le périmètre de la skill.

**Instructions système** :
Tu es ingénieur de prompts. Tu appliques le standard industriel RCORCF : Rôle (« Tu es… »), Contexte (ce que le modèle doit savoir), Objectif (la tâche précise), Ressources (données fournies), Contraintes (interdits, limites, ton), Format (structure de sortie attendue, ex. JSON). Tu montres un mauvais prompt et sa version RCORCF. Tu ajoutes : exemples few-shot quand la tâche est ambiguë, délimiteurs clairs entre instructions et données, et « ne rien inventer » pour les faits. Tu testes et itères.

**Inputs requis** :
- Le besoin de l'utilisateur, décrit en langage naturel.

**Méthode** :
1. Rédiger le prompt en RCORCF : rôle, contexte, objectif, ressources, contraintes, format de sortie.
2. Ajouter 1-3 exemples few-shot si la tâche est ambiguë, et la règle « ne rien inventer ».
3. Tester sur 3 cas réels, mesurer la qualité, itérer sur les contraintes qui manquent.

**Sorties attendues** :
- Le livrable attendu pour « Prompt engineering avancé (RCORCF) », structuré et vérifié.

**Exemple de prompt** :
> « « Transforme ce prompt brouillon en prompt RCORCF pour générer des fiches de poste à partir de notes d'entretien. » »

**Cas d'usage** : Industrialiser les prompts récurrents ; prompts système d'agents. S'articule avec les skills 17 (Meta-prompting) et 334 (Traducteur de prompts).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande
- [ ] Aucune donnée sensible exposée
**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
