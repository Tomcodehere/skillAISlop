---
num: 1427
nom: "Sortie JSON fiable et validee (2027)"
emoji: "🧱"
domaine: "IA / Prompting"
signal: "Forcer une sortie JSON fiable d'un LLM en 2027 : schéma JSON dans le prompt, exemples few-shot du JSON attendu, parsing défensif + validation (Pydantic/JSON Schema) côté code, retry si invalide. Utilise quand on parse la sortie d'un LLM. N'utilise pas pour du texte libre."
mot_cle: "sortie JSON LLM fiable validation schema pydantic"
nom_court: "JSON fiable"
branche: "D14"
synonymes: ["forcer le JSON en sortie LLM", "valider la sortie JSON du modèle", "json schema prompt"]
cross_refs: [332, 1243, 326]
tags: ["2027"]
depends_on: [332]
---

## 1427. 🧱 Sortie JSON fiable et validee (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Obtenir une sortie JSON 100 % valide d'un LLM en 2027 : schéma + exemples dans le prompt, parsing défensif et validation (JSON Schema/Pydantic) côté code, avec retry si invalide.

**Quand l'utiliser (triggers)** :
- Le LLM renvoie du JSON invalide (texte autour)
- Valider la sortie JSON côté code
- JSON Schema dans le prompt

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es ingénieur sortie structurée. Tu donnes la recette : schéma JSON dans le system prompt + 2 exemples few-shot du JSON, extraction (premier { ... dernier }), validation Pydantic, retry avec message d'erreur si invalide. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le schéma JSON cible (champs, types)
- Le prompt actuel
- Le taux d'erreur actuel sur le parsing

**Méthode** :
1. Mettre le schéma JSON dans le prompt + instruction 'réponds UNIQUEMENT en JSON'.
2. Ajouter 1-2 exemples few-shot du JSON exact attendu.
3. Parser défensivement (extraire entre le premier { et le dernier }).
4. Valider avec Pydantic/JSON Schema ; si invalide, retry (max 2) avec le message d'erreur.
5. Logger les échecs pour améliorer le prompt.

**Sorties attendues** :
- Le prompt produisant du JSON valide
- Le parseur + validateur côté code
- Le taux de validité atteint (objectif 100 %)

**Exemple de prompt** :
> « Mon LLM renvoie parfois du texte autour du JSON et ça casse mon parse : rends la sortie JSON fiable (schéma + few-shot + validation Pydantic + retry). »

**Cas d'usage** : Agents, extraction de données, intégrations API. S'articule avec skills 332 (schémas de sortie), 1243 (structure de prompt) et 326 (tokens).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
