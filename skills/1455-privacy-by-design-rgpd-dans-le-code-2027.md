---
num: 1455
nom: "Privacy by design : RGPD dans le code (2027)"
emoji: "⚖️"
domaine: "Sécurité"
signal: "Appliquer le privacy by design en 2027 (RGPD art. 25) : minimisation des données collectées, finalité déclarée, durée de conservation limitée, pseudonymisation, chiffrement, droits des personnes (accès, effacement) faciles à exercer, registre des traitements. Utilise quand on conçoit une nouvelle fonctionnalité avec données perso. N'utilise pas pour l'audit RGPD global (189)."
mot_cle: "privacy by design RGPD art 25 minimisation rétention pseudonymisation"
nom_court: "Privacy by design"
branche: "D23"
synonymes: ["RGPD dès la conception", "minimiser données collectées", "droit à l'effacement facile"]
cross_refs: [189, 1226, 1440]
tags: ["2027"]
depends_on: [189]
---

## 1455. ⚖️ Privacy by design : RGPD dans le code (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Appliquer le privacy by design (RGPD art. 25) en 2027 sur une feature : minimisation des données, finalité et base légale, rétention limitée, pseudonymisation, chiffrement, et droits des personnes (accès/effacement) en un clic.

**Quand l'utiliser (triggers)** :
- On ajoute un champ 'téléphone' au formulaire : est-ce justifié ?
- Mettre le RGPD dès la conception d'une feature
- Droit à l'effacement : comment l'implémenter ?

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es DPO technique. Tu appliques la checklist RGPD art. 25 par feature : données strictement nécessaires, finalité, durée de conservation avec purge auto, pseudonymisation (id hashé), chiffrement, et endpoints de droits (export, suppression). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La feature à concevoir et ses données perso
- La base légale (consentement, contrat, intérêt légitime)
- La durée de conservation nécessaire

**Méthode** :
1. Lister les données perso collectées et justifier chacune (minimisation).
2. Définir finalité + base légale, l'écrire dans le registre (skill 1226).
3. Durée de conservation : purge automatique à l'échéance (TTL BDD).
4. Pseudonymiser (remplacer l'email par un id hashé côté analytics).
5. Implémenter les droits : export + effacement en 1 clic (API + UI), loggé.

**Sorties attendues** :
- La checklist RGPD de la feature remplie
- La purge auto + pseudonymisation en place
- Les endpoints de droits (export/effacement) fonctionnels

**Exemple de prompt** :
> « On ajoute la géoloc pour la livraison : applique le privacy by design (minimisation, consentement, durée 30 j avec purge, droit à l'effacement en 1 clic). »

**Cas d'usage** : Toute feature avec données perso, conformité RGPD, confiance. S'articule avec skills 189 (RGPD), 1226 (flux données) et 1440 (PII).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
