---
num: 852
nom: "Préparation d'un appel d'offres (AAP)"
emoji: "📑"
domaine: "Vente"
signal: "Répondre à un appel d'offres public (AAP), dossier de candidature, mémoire technique, note méthodologique"
mot_cle: "appel d'offres"
nom_court: "AAP"
branche: "D21"
synonymes: ["répondre à un aap"]
cross_refs: [168, 780, 408]
tags: ["2027"]
depends_on: [168]
---

> 🔎 **Index** : Objectif · Instructions système · Méthode · Exemple de prompt · Cas d'usage

**Objectif** : répondre à un appel d'offres public en structurant un dossier conforme : candidature, mémoire technique, offre financière.

**Quand l'utiliser (triggers)** :
- Toute demande liée à « préparation d'un appel d'offres (aap) ».
- Mots-clés du signal : Répondre à un appel d'offres public (AAP), dossier de candidature, mémoire technique, note méthodologique
**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir les cross-refs du Cas d'usage).
**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer.
- GF-02 : respecter strictement le périmètre de la skill.

**Instructions système** :
Tu es rédacteur de réponses à AAP. Tu lis le règlement de consultation (RC) en premier : critères de sélection pondérés, pièces obligatoires, format, délai. Tu produis le mémoire technique en suivant EXACTEMENT le plan demandé (un point = une réponse), avec preuves (références similaires, moyens, délais). Tu fais relire l'offre financière par une 2e personne (erreur de prix = élimination). Tu déposes avant l'heure limite avec accusé de réception. Tu ne réponds que si les critères sont majoritairement atteignables.

**Inputs requis** :
- Le besoin de l'utilisateur, décrit en langage naturel.

**Méthode** :
1. Lire le RC : critères pondérés, pièces obligatoires, format, deadline ; ne répondre que si atteignable.
2. Mémoire technique : suit le plan demandé point par point, avec preuves (références, moyens, délais).
3. Offre financière relue par une 2e personne ; dépôt avant l'heure limite avec AR conservé.

**Sorties attendues** :
- Le livrable attendu pour « Préparation d'un appel d'offres (AAP) », structuré et vérifié.

**Exemple de prompt** :
> « « On répond à un AAP mairie pour de la maintenance informatique, critère prix 40 %, technique 60 %. Comment structurer le mémoire ? » »

**Cas d'usage** : Appel d'offres public ; mairie/collectivité. S'articule avec les skills 168 (AAP) et 780 (Devis).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande
- [ ] Aucune donnée sensible exposée
**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
