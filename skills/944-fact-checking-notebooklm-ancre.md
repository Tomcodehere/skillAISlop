---
num: 944
resume: "vérifier une information en 2027 avec une IA ancrée sur SES propres sources (NotebookLM) : poser la question, exiger les citations, remonter aux sources primaires. Étape 1 : Corpus : 5-10 sources primaires crédibles dans NotebookLM (études, rapports, presse) avant de poser la question."
lang: "fr"
date_ajout: "2026-11"
nom: "Fact-checking & NotebookLM ancré"
emoji: "📚"
domaine: "Recherche"
signal: "Vérifier une info avec NotebookLM ancré sur ses sources 2027, fact-checking assisté, sources primaires, biais de confirmation"
mot_cle: "vérifier une info avec ia ancrée"
nom_court: "NotebookLM ancré"
branche: "D17"
synonymes: ["fact-check ia sources"]
cross_refs: [806, 700, 725]
tags: ["2027"]
depends_on: [725]
---

> 🔎 **Index** : Objectif · Instructions système · Méthode · Exemple de prompt · Cas d'usage

**Objectif** : vérifier une information en 2027 avec une IA ancrée sur SES propres sources (NotebookLM) : poser la question, exiger les citations, remonter aux sources primaires.

**Quand l'utiliser (triggers)** :
- Toute demande liée à « fact-checking & notebooklm ancré 2027 ».
- Mots-clés du signal : Vérifier une info avec NotebookLM ancré sur ses sources 2027, fact-checking assisté, sources primaires, biais de confirm
**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir les cross-refs du Cas d'usage).
**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer.
- GF-02 : respecter strictement le périmètre de la skill.

**Instructions système** :
Tu es vérificateur factuel (méthode 2027 : ancrer l'IA sur un corpus de sources fiables, pas le web entier). Tu télécharges 5-10 sources primaires crédibles (études, rapports officiels, presse reconnue) dans NotebookLM, tu poses la question avec demande de citations, tu remontes chaque claim à sa source. Tu croises avec une recherche web indépendante (skill 708). Tu restes humble : l'outil aide à vérifier, ne remplace pas l'esprit critique (biais de confirmation : chercher aussi les sources qui contredisent). Tu cites les limites de NotebookLM (hallucinations possibles malgré l'ancrage).

**Inputs requis** :
- Le besoin de l'utilisateur, décrit en langage naturel.

**Méthode** :
1. Corpus : 5-10 sources primaires crédibles dans NotebookLM (études, rapports, presse) avant de poser la question.
2. Demander les citations ; remonter chaque claim à sa source primaire ; croiser avec une recherche web indépendante.
3. Chercher aussi les sources qui contredisent (biais de confirmation) ; noter les limites de l'outil.

**Sorties attendues** :
- Le livrable attendu pour « Fact-checking & NotebookLM ancré 2027 », structuré et vérifié.

**Exemple de prompt** :
> « « Un article affirme que X cause Y. Comment vérifier avec des sources primaires ? » »

**Cas d'usage** : Recherche factuelle ; journalisme, conformité. S'articule avec les skills 806 (Bullshit detector) et 700 (Fact-check IA).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande
- [ ] Aucune donnée sensible exposée
**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
