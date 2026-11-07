---
num: 1499
date_ajout: "2026-11"
nom: "Resumer automatiquement une reunion avec actions (2027)"
emoji: "🎤"
domaine: "Productivité"
signal: "Enregistrer et résumer une réunion automatiquement en 2027 avec un outil IA (Fireflies, Otter, tl;dv, ou bot Microsoft Teams/Google Meet intégré) : transcription, résumé structuré (décisions, actions avec responsables et échéances), partage aux absents, recherche dans les transcriptions. Utilise pour les réunions récurrentes. N'utilise pas pour un entretien confidentiel sans consentement (RGPD)."
mot_cle: "résumé automatique réunion transcription actions responsables Fireflies Otter 2027"
nom_court: "Résumé réunion IA"
branche: "D25"
synonymes: ["transcrire une réunion automatiquement", "Fireflies ou Otter 2027", "extraire décisions et actions d'une réunion"]
cross_refs: [705, 285, 378]
tags: ["2027"]
depends_on: [705]
---

## 1499. 🎤 Resumer automatiquement une reunion avec actions (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Automatiser le compte-rendu de réunion en 2027 (Fireflies/Otter/tl;dv ou bot Teams/Meet) : transcription, résumé structuré (sujets, décisions, actions avec responsable + échéance), partage aux absents, recherche dans les transcriptions.

**Quand l'utiliser (triggers)** :
- Qui a dit quoi dans la réunion de mardi ?
- Résumé auto avec actions et responsables
- Partager le CR aux absents automatiquement

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es assistant de réunion IA. Tu compares les outils (Fireflies, Otter, tl;dv, bots natifs Teams/Meet), tu insistes sur le consentement (annoncer l'enregistrement, RGPD), et tu définis le format de CR (décisions, actions owner+date, points ouverts). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La réunion (visio Teams/Meet/Zoom ou présentiel + micro)
- L'outil choisi et les participants à notifier
- Le canal de partage (mail, Slack, Notion)

**Méthode** :
1. Choisir l'outil (bot intégré à la visio = le plus simple) et annoncer l'enregistrement à l'oral.
2. Laisser le bot rejoindre, enregistrer, transcrire (diarisation : qui parle quand).
3. Générer le CR structuré : sujets, décisions, actions (owner + échéance), questions ouvertes.
4. Partager automatiquement aux participants + absents (mail/Slack avec lien transcription).
5. Classer et rendre recherchable ('qui a parlé de X ?') pour les prochaines réunions.

**Sorties attendues** :
- Le CR auto (décisions + actions owner/date) partagé
- La transcription recherchable archivée
- La procédure consentement RGPD appliquée

**Exemple de prompt** :
> « Nos réunions hebdo n'ont jamais de CR : mets en place un résumé auto (bot Meet, transcription, CR avec actions owner+date, partagé à tous + absents). »

**Cas d'usage** : Productivité équipe, suivi des décisions, onboarding des absents. S'articule avec skills 705 (notes réunion), 285 (action items) et 378 (transcriptions).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
