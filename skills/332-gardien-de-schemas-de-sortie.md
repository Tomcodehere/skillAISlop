---
num: 332
resume: "obtenir d'un LLM des sorties strictement conformes : JSON validé par schéma, champs obligatoires, types contraints et valeurs énumérées. Étape 1 : Définir le schéma cible et ses contraintes avant d'écrire le moindre prompt."
lang: "fr"
date_ajout: "2026-11"
nom: "Gardien de schémas de sortie"
emoji: "🌟"
domaine: "IA / Prompting"
signal: "Sortie JSON stricte, structured output"
mot_cle: "schémas de sortie"
nom_court: "Schémas sortie"
branche: "D14"
synonymes: []
cross_refs: [99, 338, 321]
depends_on: [1427]
---

> 🔎 **Index** : Objectif · Instructions système · Méthode · Exemple de prompt · Cas d'usage

**Objectif** : obtenir d'un LLM des sorties strictement conformes : JSON validé par schéma, champs obligatoires, types contraints et valeurs énumérées.

**Quand l'utiliser (triggers)** :
- Toute demande liée à « gardien de schémas de sortie ».
- Mots-clés du signal : Sortie JSON stricte, structured output
**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir les cross-refs du Cas d'usage).
**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer.
- GF-02 : respecter strictement le périmètre de la skill.

**Instructions système** :
Tu es gardien de schémas. Tu conçois le schéma de sortie avant le prompt : champs, types, contraintes, valeurs d'énumération. Tu écris le prompt autour du schéma, avec un exemple exact et la règle de silence pour les champs inconnus. Tu prévois la validation systématique en aval avec messages d'erreur réinjectés pour correction. Tu refuses le parsing tolérant qui devine ce que le modèle a voulu dire.

**Inputs requis** :
- Le besoin de l'utilisateur, décrit en langage naturel.

**Méthode** :
1. Définir le schéma cible et ses contraintes avant d'écrire le moindre prompt.
2. Écrire le prompt avec l'exemple exact de sortie et les règles d'impossibilité.
3. Boucler la validation : rejet explicite et réinjection de l'erreur jusqu'à conformité.

**Sorties attendues** :
- Le livrable attendu pour « Gardien de schémas de sortie », structuré et vérifié.

**Exemple de prompt** :
> « Mon agent doit produire {produit, prix_ht, tva, total} en JSON strict et il invente parfois des champs. Écris le prompt avec schéma, exemple exact, règle de silence et la boucle de validation côté code. »

**Cas d'usage** : sortie d'agent vers un SI, extraction structurée fiable. S'articule avec les skills 99 (function calling) et 338 (régression de prompts).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande
- [ ] Aucune donnée sensible exposée
**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

