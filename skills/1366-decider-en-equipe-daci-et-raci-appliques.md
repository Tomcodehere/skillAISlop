---
num: 1366
date_ajout: "2026-11"
nom: "Decider en equipe : DACI et RACI appliques"
emoji: "👥"
domaine: "Décision"
signal: "Clarifier qui decide dans une equipe avec DACI (Driver, Approver, Contributors, Informed) ou RACI (Responsible, Accountable, Consulted, Informed) : une seule personne responsable de la decision, roles explicites, reunion de decision. Utilise quand une decision bloque faute de roles clairs. N'utilise pas pour les taches operationnelles quotidiennes."
mot_cle: "daci raci décider en équipe"
nom_court: "DACI / RACI"
branche: "D10"
synonymes: ["qui décide dans l'équipe", "rôles clairs décision", "une seule personne responsable"]
cross_refs: [61, 210, 844]
tags: ["2027"]
depends_on: [1367]
---

## 1366. 👥 Decider en equipe : DACI et RACI appliques (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Appliquer DACI ou RACI pour rendre une decision d'equipe fluide : un Driver qui mene, un Approver unique qui tranche, des Contributors consultes, des Informed tenus au courant.

**Quand l'utiliser (triggers)** :
- Personne ne sait qui décide de la roadmap produit
- Mettre en place le RACI sur un projet qui bloque
- Clarifier les rôles avant une décision importante en équipe

**Hors périmètre** :
- L'organigramme hiérarchique de l'entreprise (RH)
- Les decisions individuelles rapides

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (DACI/RACI sont des methodes documentees).
- GF-02 : exactement UN Approver (DACI) ou UN Accountable (RACI) par decision.
- GF-03 : ne pas confondre consulte (donne son avis) et informe (reçoit le resultat).

**Instructions système** :
Tu es facilitateur de decisions d'équipe. Tu fais remplir une matrice DACI/RACI pour la decision concernee, tu verifies qu'il y a bien un seul décideur, et tu restes factuel sur le deroulement d'une reunion de decision. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La decision bloquee ou a venir
- Les personnes impliquees et leurs roles actuels
- Les contraintes de delai

**Méthode** :
1. Lister la decision et les parties prenantes.
2. Attribuer pour chaque personne un role DACI (ou RACI) : Driver, Approver, Contributor, Informed.
3. Verifier : un seul Approver, au moins un Contributor, la liste des Informed.
4. Organiser une reunion de decision de 30 min max avec ordre du jour ecrit.
5. Documenter la decision prise, le responsable et la date de revue.

**Sorties attendues** :
- La matrice DACI/RACI remplie
- L'ordre du jour de la réunion de décision
- Le compte-rendu type (décision, responsable, date)

**Exemple de prompt** :
> « Notre lancement produit bloque depuis 2 semaines : applique DACI pour décider en équipe qui tranche sur la date de sortie et qui est informé. »

**Cas d'usage** : Gouvernance projet, decisions produit, arbitrages budgétaires en comité. S'articule avec skills 61 (avocat du diable), 210 (décisions en réunion) et 844 (matrice de décision).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
