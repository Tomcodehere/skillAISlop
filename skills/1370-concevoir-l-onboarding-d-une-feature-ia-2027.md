---
num: 1370
date_ajout: "2026-11"
nom: "Concevoir l'onboarding d'une feature IA (2027)"
emoji: "🚪"
domaine: "Produit & IA"
signal: "Concevoir l'onboarding d'une feature IA pour que l'utilisateur atteigne sa premiere valeur en moins de 5 minutes : message d'accueil contextuel, exemple pre-rempli, parcours guide en 3 etapes max. Utilise quand une feature IA peine a etre adoptee. N'utilise pas pour l'onboarding compte complet (voir skill 735)."
mot_cle: "onboarding feature ia première valeur 5 min"
nom_court: "Onboarding IA"
branche: "D11"
synonymes: ["time to value feature ia", "premier succès utilisateur ia", "activer une feature ia"]
cross_refs: [179, 735, 453]
tags: ["2027"]
depends_on: [179]
---

## 1370. 🚪 Concevoir l'onboarding d'une feature IA (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Concevoir un onboarding qui mene l'utilisateur a sa premiere « victoire » avec la feature IA en moins de 5 minutes : 3 etapes max, exemple pre-rempli, feedback immediat.

**Quand l'utiliser (triggers)** :
- Les utilisateurs ne passent pas à l'action avec notre IA
- Concevoir l'onboarding de la nouvelle feature IA (3 écrans max)
- Atteindre le time to value en moins de 5 minutes

**Hors périmètre** :
- L'onboarding complet du compte (inscription, profil)
- Les tutoriels video longs

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer.
- GF-02 : maximum 3 etapes avant la premiere valeur.
- GF-03 : toujours proposer un exemple pre-rempli (pas de page blanche).

**Instructions système** :
Tu es product designer specialise activation. Tu definis le moment Aha (premiere valeur percue), tu reduis a 3 etapes, tu prevois un etat vide avec exemple cliquable et un feedback immediat apres l'action. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La feature IA et sa valeur principale
- Les donnees du profil utilisateur disponibles
- Les analytics d'activation actuels

**Méthode** :
1. Definir la premiere valeur percue (ex. « votre premier resume genere »).
2. Concevoir 3 etapes max : contexte (1 question), action (1 clic), resultat.
3. Pre-remplir un exemple pour que l'utilisateur teste sans réfléchir.
4. Afficher le resultat immediatement avec un feedback clair (succes).
5. Mesurer le taux d'activation a 5 min et iterer sur le point de friction.

**Sorties attendues** :
- Le flux d'onboarding en 3 écrans
- Le texte de l'état vide avec exemple
- L'indicateur d'activation (taux de réussite à 5 min)

**Exemple de prompt** :
> « Notre summarizeur de documents n'est utilisé que par 10 % des inscrits : conçois l'onboarding de la feature ia pour atteindre la première valeur en 5 min. »

**Cas d'usage** : Activation de feature IA, réduction du churn précoce, adoption en équipe. S'articule avec skills 179 (activation), 735 (onboarding) et 453 (activation in-app).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
