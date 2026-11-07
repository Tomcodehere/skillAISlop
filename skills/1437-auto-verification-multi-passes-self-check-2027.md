---
num: 1437
date_ajout: "2026-11"
nom: "Auto-verification multi-passes (self-check, 2027)"
emoji: "✅"
domaine: "IA / Prompting"
signal: "Faire vérifier sa réponse par le LLM lui-même en 2 passes en 2027 : passe 1 répond, passe 2 relit la réponse avec une grille de vérification (complétude, exactitude, format) et corrige. Utilise quand la qualité est critique. N'utilise pas si le coût/latence est prohibitif."
mot_cle: "self-check vérification multi-passes grille relecture LLM"
nom_court: "Self-check"
branche: "D14"
synonymes: ["le LLM se relit et corrige", "vérification en 2 passes", "grille de relecture réponse"]
cross_refs: [738, 1243, 337]
tags: ["2027"]
depends_on: [738]
---

## 1437. ✅ Auto-verification multi-passes (self-check, 2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Améliorer la qualité d'une réponse LLM en 2027 par self-check : passe 1 génère, passe 2 applique une grille de vérification (exactitude, complétude, format, biais) et corrige, avec un score final.

**Quand l'utiliser (triggers)** :
- Le LLM se trompe parfois, ajouter une relecture
- Self-consistency : plusieurs réponses puis vote
- Grille de vérification d'une réponse IA

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es réviseur IA interne. Tu donnes le pattern 2 passes (génération puis critique avec grille notée), la variante self-consistency (3 réponses + vote majoritaire), et tu mesures le gain vs coût doublé. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La réponse à vérifier
- La grille de vérification (critères + échelle)
- Le budget tokens disponible (x2)

**Méthode** :
1. Passe 1 : le LLM génère la réponse (prompt habituel).
2. Passe 2 : même LLM reçoit réponse + grille (exactitude /10, complétude /10, format OK ?) et corrige.
3. Variante : self-consistency, 3 générations indépendantes + vote majoritaire sur la réponse finale.
4. Comparer qualité avant/après self-check (échantillon de 20).
5. N'appliquer que si le gain justifie le coût x2 (tokens, latence).

**Sorties attendues** :
- Le pattern self-check (2 passes)
- Le gain de qualité mesuré
- La décision d'appliquer ou non (coût x2)

**Exemple de prompt** :
> « Mes réponses longues ont parfois des oublis : ajoute un self-check en 2 passes (génération puis relecture avec grille notée + correction). »

**Cas d'usage** : Rédaction critique, code, analyses. S'articule avec skills 738 (chaîne de pensée), 1243 (structure prompt) et 337 (cartes de modèle).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
