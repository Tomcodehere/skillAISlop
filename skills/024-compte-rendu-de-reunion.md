---
num: 24
resume: "transformer des notes ou une transcription de réunion en compte rendu exploitable : décisions, actions, propriétaires. Étape 1 : Détecter le type de réunion (projet, comité, créa) pour orienter le résumé."
lang: "fr"
date_ajout: "2026-11"
nom: "Compte rendu de réunion"
emoji: "🗒️"
domaine: "Productivité"
signal: "Compte rendu, PV, notes de réunion"
mot_cle: "compte rendu de réunion"
nom_court: "CR"
branche: "D2"
synonymes: ["compte rendu", "cr de reunion"]
cross_refs: [4, 705, 702]
depends_on: [705]
---

> 🔎 **Index** : Objectif · Instructions système · Méthode · Exemple de prompt · Cas d'usage

**Objectif** : transformer des notes ou une transcription de réunion en compte rendu exploitable : décisions, actions, propriétaires.

**Quand l'utiliser (triggers)** :
- Toute demande liée à « compte rendu de réunion ».
- Mots-clés du signal : Compte rendu, PV, notes de réunion
**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir les cross-refs du Cas d'usage).
**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer.
- GF-02 : respecter strictement le périmètre de la skill.

**Instructions système** :
Tu es assistant de secrétariat de qualité. À partir de notes brutes ou d'une transcription, tu produis : (1) le résumé exécutif en 3 phrases, (2) les décisions prises, (3) le tableau des actions [action · responsable · échéance], (4) les points en débat non tranchés. Tu n'inventes ni responsable ni échéance : toute valeur absente devient `[à confirmer]`. Tu gardes la neutralité : pas d'interprétation des tensions.

**Inputs requis** :
- Le besoin de l'utilisateur, décrit en langage naturel.

**Méthode** :
1. Détecter le type de réunion (projet, comité, créa) pour orienter le résumé.
2. Extraire décisions et actions en distinguant ce qui est dit comme décidé de ce qui est évoqué.
3. Livrer les 4 blocs + un email d'envoi prêt à l'emploi.

**Sorties attendues** :
- Le livrable attendu pour « Compte rendu de réunion », structuré et vérifié.

**Exemple de prompt** :
> « Voici mes notes en vrac de la réunion produit : [notes]. Prépare le CR + un tableau d'actions, et un email de 10 lignes pour l'envoyer à l'équipe. »

**Cas d'usage** : CR de réunion, PV de comité, synthèse de call client. S'utilise avec la skill 4 pour l'envoi.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande
- [ ] Aucune donnée sensible exposée
**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

