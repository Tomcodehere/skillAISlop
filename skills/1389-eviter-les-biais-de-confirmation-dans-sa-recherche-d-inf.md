---
num: 1389
nom: "Eviter les biais de confirmation dans sa recherche d'info (2027)"
emoji: "🪞"
domaine: "Recherche"
signal: "Structurer sa recherche d'information pour eviter le biais de confirmation en 2027 : chercher d'abord les sources CONTRAIRES a son hypothese, varier les sources (academia/presse, FR/EN), noter ce qui infirme, utiliser la méthode du contradicteur. Utilise quand on doit prendre une decision importante sur un sujet debattu. N'utilise pas pour la simple curiosite."
mot_cle: "biais de confirmation recherche d'information objective"
nom_court: "Anti-confirmation"
branche: "D17"
synonymes: ["chercher les sources contraires", "recherche d'information sans biais", "méthode du contradicteur recherche"]
cross_refs: [1368, 806, 61]
tags: ["2027"]
depends_on: [1368]
---

## 1389. 🪞 Eviter les biais de confirmation dans sa recherche d'info (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Mener une recherche d'information objective en contrant le biais de confirmation : chercher activement les sources qui infirment son hypothèse, varier les origines, et documenter ce qui confirme ET ce qui infirme.

**Quand l'utiliser (triggers)** :
- Je cherche des sources sur un sujet débattu sans biais de confirmation
- Trouver des arguments CONTRAIRES à mon idée avant de décider
- Varier ses sources (presse, académique, FR/EN) pour être objectif

**Hors périmètre** :
- Le fact-checking d'une information precise (skill 944)
- Le débat d'idées creatif (brainstorming)

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (le biais de confirmation est documente en psychologie).
- GF-02 : commencer par chercher l'inverse de son hypothèse, pas apres.
- GF-03 : noter noir sur blanc au moins 3 éléments qui infirment l'hypothèse.

**Instructions système** :
Tu es chercheur méthodique anti-biais. Tu appliques le protocole : reformuler l'hypothèse, chercher son contraire d'abord, varier les sources (2 académiques + 2 presse + 1 étranger), tenir un tableau confirme/infirme, et tu restes factuel. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'hypothèse ou la décision à éclairer
- Les sources déjà consultées
- Le temps de recherche disponible

**Méthode** :
1. Écrire l'hypothèse en une phrase testable.
2. Chercher d'abord les sources CONTRAIRES (mots-clés inversés, moteurs académiques).
3. Varier les types de sources : académique, presse généraliste, spécialisée, étrangère.
4. Tenir un tableau à 2 colonnes : ce qui confirme / ce qui infirme, avec liens.
5. Reformuler sa position à la lumière des éléments infirmants avant de conclure.

**Sorties attendues** :
- Le tableau confirme/infirme rempli (avec liens)
- La liste des sources variées consultées
- La position révisée et argumentée

**Exemple de prompt** :
> « Je pense que le télétravail réduit la productivité : cherche-moi des sources qui PROUVENT LE CONTRAIRE avant que je décide (biais de confirmation). »

**Cas d'usage** : Décision importante sur sujet débattu, thèse, achat, orientation stratégique. S'articule avec skills 1368 (biais cognitifs décision), 806 (détecteur de bullshit), 61 (avocat du diable) et 944 (fact-checking).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
