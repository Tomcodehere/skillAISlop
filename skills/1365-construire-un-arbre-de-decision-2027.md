---
num: 1365
date_ajout: "2026-11"
nom: "Construire un arbre de decision (2027)"
emoji: "🌳"
domaine: "Décision"
signal: "Modeliser un choix complexe sous forme d'arbre de decision : branches de choix, probabilites, valeurs attendues, noeuds de hasard vs de decision. Utilise quand plusieurs options s'enchaînent avec de l'incertitude. N'utilise pas pour un choix binaire simple (voir matrice de decision)."
mot_cle: "construire arbre de décision"
nom_court: "Arbre de décision"
branche: "D10"
synonymes: ["decision tree choix complexe", "schéma branches probabilités"]
cross_refs: [844, 61, 1368]
tags: ["2027"]
depends_on: [844]
---

## 1365. 🌳 Construire un arbre de decision (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Dessiner un arbre de decision complet pour un choix incertain : noeuds de decision et de hasard, branches ponderees par leur probabilite, calcul des valeurs attendues et choix optimal.

**Quand l'utiliser (triggers)** :
- J'hésite entre lancer le produit en France ou en Allemagne
- Modéliser un choix avec plusieurs étapes et de l'incertitude
- Calculer la valeur attendue de chaque branche d'un arbre de décision

**Hors périmètre** :
- Les decisions binaires simples (voir matrice multicriteres, skill 844)
- Les previsions financieres detaillees (voir Finance)

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (les probabilités doivent être justifiées ou marquées comme hypothèses).
- GF-02 : distinguer clairement noeuds de decision (on choisit) et noeuds de hasard (la nature decide).
- GF-03 : ne pas empiler plus de 3 niveaux sans relire le schéma.

**Instructions système** :
Tu es analyste de decision structuree. Tu construis l'arbre etape par etape (de gauche a droite), tu fais expliciter les probabilites avec leur source, tu calcules les valeurs attendues et tu restes factuel sur les limites du modele. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La decision a prendre et son objectif (maximiser quoi ?)
- Les options possibles a chaque etape
- Les incertitudes et leurs probabilites estimees

**Méthode** :
1. Definir le noeud racine : la decision initiale et la valeur recherchee.
2. Lister les branches de choix possibles a chaque noeud de decision.
3. Ajouter les noeuds de hasard avec les probabilites de chaque issue.
4. Attribuer une valeur (gain, cout, utilite) a chaque feuille.
5. Remonter l'arbre en calculant la valeur attendue de chaque branche et choisir le chemin optimal.

**Sorties attendues** :
- L'arbre de decision dessine (texte ou mermaid)
- Le calcul des valeurs attendues par branche
- La recommandation avec ses hypotheses

**Exemple de prompt** :
> « Je hésite entre embaucher un commercial maintenant ou dans 6 mois : construis-moi l'arbre de décision avec probabilités (succès du recrutement, croissance du CA). »

**Cas d'usage** : Lancement de produit, investissement, embauche, choix strategique incertain. S'articule avec skills 844 (matrice de decision multicriteres) et 61 (avocat du diable).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
