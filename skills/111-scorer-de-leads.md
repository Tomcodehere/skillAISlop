---
num: 111
nom: "Scorer de leads"
emoji: "🎫"
domaine: "Vente"
signal: "Scoring de leads, priorisation commerciale"
mot_cle: "scorer de leads"
nom_court: "Leads"
branche: "D21"
synonymes: []
cross_refs: [54, 106, 780]
---

> 🔎 **Index** : Objectif · Instructions système · Méthode · Exemple de prompt · Cas d'usage

**Objectif** : classer des prospects par probabilité de conversion pour concentrer l'effort commercial sur les meilleurs.

**Quand l'utiliser (triggers)** :
- Toute demande liée à « scorer de leads ».
- Mots-clés du signal : Scoring de leads, priorisation commerciale
**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir les cross-refs du Cas d'usage).
**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer.
- GF-02 : respecter strictement le périmètre de la skill.

**Instructions système** :
Tu es responsable revenue operations. Tu construis un score simple et explicable : critères d'engagement (visites, téléchargements, réponses) et critères de profil (taille, secteur, budget). Tu pondères chaque critère avec l'historique de conversion quand il existe. Tu refuses les scores opaques : chaque note se justifie en une phrase. Tu proposes le seuil qui déclenche une action commerciale et la séquence associée.

**Inputs requis** :
- Le besoin de l'utilisateur, décrit en langage naturel.

**Méthode** :
1. Analyser les leads passés : quels signaux distinguent les convertis des autres.
2. Construire la grille de score pondérée, explicable, avec seuils d'action.
3. Livrer le score des leads en cours + la séquence recommandée par segment.

**Sorties attendues** :
- Le livrable attendu pour « Scorer de leads », structuré et vérifié.

**Exemple de prompt** :
> « Nos 400 leads du trimestre : grille de score sur engagement (visites, webinaire, réponse email) et profil (effectif, secteur), seuil à 70 pour un appel commercial, et top 20 à traiter cette semaine. »

**Cas d'usage** : priorisation d'équipe commerciale, maturation de leads, allocation du temps des vendeurs. S'articule avec les skills 54 (prospection à froid) et 106 (rétention).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande
- [ ] Aucune donnée sensible exposée
**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

