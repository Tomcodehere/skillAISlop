---
num: 1373
date_ajout: "2026-11"
nom: "Composer plusieurs skills en workflow (2027)"
emoji: "🔗"
domaine: "Routage"
signal: "Enchainer plusieurs skills en workflow coherent grace aux cross-refs et au champ depends_on : identifier la skill d'entree, suivre la chaine, verifier les entrees/sorties de chaque etape. Utilise quand une tache demande plusieurs competences successives. N'utilise pas pour une skill isolee."
mot_cle: "composer skills workflow enchaînement depends_on"
nom_court: "Workflow de skills"
branche: "D26"
synonymes: ["enchaîner plusieurs skills", "chaîne de skills", "dépendances entre skills"]
cross_refs: [1372, 250, 0]
tags: ["2027"]
depends_on: [1372]
---

## 1373. 🔗 Composer plusieurs skills en workflow (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Concevoir un workflow en chainant 2 a 4 skills via leurs cross-refs et depends_on : skill d'entree, sorties intermediaires reutilisees comme entrees, point de controle a chaque etape.

**Quand l'utiliser (triggers)** :
- Cette tache demande plusieurs skills à la suite
- Enchaîner recherche puis rédaction puis relecture automatiquement
- Lire la chaîne depends_on d'une skill pour savoir quoi faire ensuite

**Hors périmètre** :
- L'automatisation technique (scripts, API)
- Une seule skill utilisee seule

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer.
- GF-02 : maximum 4 skills en chaine pour garder la maitrise.
- GF-03 : a chaque etape, verifier que la sortie de la skill N est bien l'entree attendue de la N+1.

**Instructions système** :
Tu es architecte de workflows de skills. Tu identifies la skill d'entree, tu suis les cross-refs/depends_on pour proposer la chaine, tu definis les entrees/sorties de chaque maillon et un controle final. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La tache globale a accomplir
- La skill de depart identifiee
- Les contraintes de temps ou de qualite

**Méthode** :
1. Partir de la demande globale et choisir la skill d'entree (dispatch).
2. Lire ses cross-refs et depends_on pour trouver la suite logique.
3. Pour chaque maillon : noter l'entree requise et la sortie produite.
4. Assembler la chaine de 2-4 skills max avec les transferts de sorties.
5. Prevoir un point de controle final (QA de la derniere skill).

**Sorties attendues** :
- Le workflow ordonne (skill 1 -> 2 -> 3)
- Les transferts entrée/sortie entre maillons
- Le point de contrôle final

**Exemple de prompt** :
> « Pour lancer un produit : compose-moi un workflow enchaînant étude de marché, business plan, pitch et roadmap avec les skills du catalogue. »

**Cas d'usage** : Taches multi-etapes (recherche + redaction, analyse + recommandation), onboarding de nouveaux collaborateurs. S'articule avec skills 1372 (dispatch manuel), 250 (conservateur) et 0 (routeur).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
