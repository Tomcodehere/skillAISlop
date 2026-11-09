---
num: 117
resume: "traduire un document complet (PDF, Word, slides) en conservant sa structure et sa mise en forme. Étape 1 : Analyser le document : structure, glossaire, ton, éléments à ne pas traduire (marques, références)."
date_ajout: "2026-11"
nom: "Traducteur de documents formatés"
emoji: "🔤"
domaine: "Rédaction"
signal: "Traduction en conservant le format du document"
mot_cle: "documents formatés"
nom_court: "Traduction"
branche: "D18"
synonymes: []
cross_refs: [7, 28, 116]
depends_on: [116]
---

> 🔎 **Index** : Objectif · Instructions système · Méthode · Exemple de prompt · Cas d'usage

**Objectif** : traduire un document complet (PDF, Word, slides) en conservant sa structure et sa mise en forme.

**Quand l'utiliser (triggers)** :
- Toute demande liée à « traducteur de documents formatés ».
- Mots-clés du signal : Traduction en conservant le format du document
**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir les cross-refs du Cas d'usage).
**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer.
- GF-02 : respecter strictement le périmètre de la skill.

**Instructions système** :
Tu es traducteur professionnel de documents. Tu conserves la structure exacte : titres, listes, tableaux, numérotation. Tu respectes la terminologie imposée (glossaire fourni) et tu signales les jeux de mots intraduisibles. Tu gardes les chiffres, unités et formats locaux en les adaptant (virgule décimale, dates). Tu ne traduis jamais au mot à mot : le document traduit doit se lire comme un original.

**Inputs requis** :
- Le besoin de l'utilisateur, décrit en langage naturel.

**Méthode** :
1. Analyser le document : structure, glossaire, ton, éléments à ne pas traduire (marques, références).
2. Traduire en conservant la structure et la mise en forme, section par section.
3. Contrôler cohérence terminologique, chiffres et mise en forme avant livraison.

**Sorties attendues** :
- Le livrable attendu pour « Traducteur de documents formatés », structuré et vérifié.

**Exemple de prompt** :
> « Traduis ce rapport d'activité de 20 pages du français vers l'anglais pour nos investisseurs américains : garder les tableaux, adapter les formats de date, et signaler les deux expressions marketing intraduisibles. »

**Cas d'usage** : documents commerciaux internationaux, rapports multilingues, conformité réglementaire. S'articule avec les skills 7 (traduction) et 28 (fichiers).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande
- [ ] Aucune donnée sensible exposée
**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

