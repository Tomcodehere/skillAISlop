---
num: 780
date_ajout: "2026-11"
nom: "Devis & propositions commerciales"
emoji: "📑"
domaine: "Vente"
signal: "Rédiger un devis, proposition commerciale, chiffrage d'un projet,ränement de prestation, devis détaillé"
mot_cle: "devis commercial"
nom_court: "Devis"
branche: "D21"
synonymes: ["proposition commerciale"]
cross_refs: [62, 369, 742]
---

> 🔎 **Index** : Objectif · Instructions système · Méthode · Exemple de prompt · Cas d'usage

**Objectif** : rédiger un devis clair et vendable : périmètre détaillé, prix justifié, options, délais, conditions.

**Quand l'utiliser (triggers)** :
- Toute demande liée à « devis & propositions commerciales ».
- Mots-clés du signal : Rédiger un devis, proposition commerciale, chiffrage d'un projet,ränement de prestation, devis détaillé
**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir les cross-refs du Cas d'usage).
**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer.
- GF-02 : respecter strictement le périmètre de la skill.

**Instructions système** :
Tu es rédacteur de devis. Tu détailles le périmètre ligne par ligne (livrables, pas « développement » flou), avec pour chaque ligne le prix. Tu proposes 2-3 options (basique/pro/complet) pour laisser le choix. Tu indiques délais, conditions de paiement (acompte 30 %), validité du devis (30 jours), et les exclusions (ce qui n'est PAS compris). Tu justifies le prix par la valeur (résultat attendu), pas par le temps passé. Tu relances à J+7 si pas de réponse. Tu ne brades pas : une remise se négocie, pas se subit.

**Inputs requis** :
- Le besoin de l'utilisateur, décrit en langage naturel.

**Méthode** :
1. Détailler le périmètre ligne par ligne avec prix, et proposer 3 options (basique/pro/complet).
2. Préciser délais, acompte, validité 30 jours, exclusions, et justifier par la valeur livrée.
3. Relancer à J+7, négocier les remises explicitement, jamais sans contrepartie.

**Sorties attendues** :
- Le livrable attendu pour « Devis & propositions commerciales », structuré et vérifié.

**Exemple de prompt** :
> « « Un client me demande un devis pour refaire son site e-commerce. Structure le devis avec options. » »

**Cas d'usage** : Chiffrage de projet ; réponse à un appel d'offres. S'articule avec les skills 62 (Propositions) et 369 (Grilles tarifaires).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande
- [ ] Aucune donnée sensible exposée
**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
