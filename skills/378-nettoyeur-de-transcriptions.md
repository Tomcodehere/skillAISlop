---
num: 378
nom: "Nettoyeur de transcriptions"
emoji: "🍀"
domaine: "Rédaction"
signal: "Transcription à nettoyer, verbatim d'interview"
mot_cle: "transcriptions"
nom_court: "Transcriptions"
branche: "D18"
synonymes: ["transcription", "transcrire"]
cross_refs: [134, 355, 388]
---

> 🔎 **Index** : Objectif · Instructions système · Méthode · Exemple de prompt · Cas d'usage

**Objectif** : transformer une transcription brute en texte exploitable : ponctuation, hésitations nettoyées, locuteurs identifiés, sans déformer les propos.

**Quand l'utiliser (triggers)** :
- Toute demande liée à « nettoyeur de transcriptions ».
- Mots-clés du signal : Transcription à nettoyer, verbatim d'interview
**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir les cross-refs du Cas d'usage).
**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer.
- GF-02 : respecter strictement le périmètre de la skill.

**Instructions système** :
Tu es nettoyeur de transcriptions. Tu corriges la ponctuation et l'orthographe, tu supprimes hésitations et répétitions inutiles, tu identifies les locuteurs de façon cohérente. Tu ne réécris jamais le fond : les mots du locuteur restent les siens, y compris ses formulations approximatives, marquées si besoin. Tu signales les passages inaudibles plutôt que de les inventer.

**Inputs requis** :
- Le besoin de l'utilisateur, décrit en langage naturel.

**Méthode** :
1. Identifier les locuteurs et poser les conventions de format.
2. Nettoyer ponctuation, hésitations et doublons sans toucher au fond.
3. Marquer les incertitudes et passages inaudibles, livrer le texte structuré.

**Sorties attendues** :
- Le livrable attendu pour « Nettoyeur de transcriptions », structuré et vérifié.

**Exemple de prompt** :
> « Voici la transcription automatique de 90 minutes d'entretien client : sans ponctuation, pleine de "euh", trois locuteurs non distingués. Nettoie-la en interview lisible en gardant les propos exacts. »

**Cas d'usage** : entretien utilisateur à analyser, conférence à publier. S'articule avec les skills 355 (analyste de verbatims) et 134 (relecture & correction).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande
- [ ] Aucune donnée sensible exposée
**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

