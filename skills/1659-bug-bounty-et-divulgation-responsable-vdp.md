---
num: 1659
resume: "Lancer un programme de bug bounty/VDP en 2027 : périmètre et hors-périmètre clairs, récompense par CVSS, SLA (réponse 5 j, correction 90 j critique), canal sécurisé (HackerOne/Bugcrowd ou formulaire interne), publication après correctif, remerciements (hall of fame). Étape 1 : Rédiger la policy : périmètre, hors-périmètre (DoS, spam, 907), règles (pas de test sur les users), safe harbor (pas de po"
lang: "fr"
date_ajout: "2026-11"
nom: "Bug bounty et divulgation responsable (VDP)"
emoji: "🐛"
domaine: "Sécurité"
signal: "Mettre en place un programme de bug bounty ou de divulgation responsable (VDP) en 2027 : périmètre clair (quoi est testable), hors périmètre (DoS, social engineering 907), récompense par criticité (CVSS), délai de réponse (5 j) et de correction (90 j critique), publication après correctif, relation avec les chercheurs (HackerOne/Bugcrowd ou VDP interne). Utilise pour toute app exposée. N'utilise pas sans processus de correction derrière (sinon frustration)."
mot_cle: "bug bounty VDP divulgation responsable 2027 périmètre récompense CVSS délai réponse correction HackerOne"
nom_court: "Bug bounty"
branche: "D23"
synonymes: ["ouvrir un VDP (divulgation responsable) interne 2027", "récompense par criticité CVSS, délai 90 j critique", "HackerOne ou Bugcrowd pour un programme payant"]
cross_refs: [439, 440, 754]
tags: ["2027"]
depends_on: [439]
---

## 1659. 🐛 Bug bounty et divulgation responsable (VDP) (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Lancer un programme de bug bounty/VDP en 2027 : périmètre et hors-périmètre clairs, récompense par CVSS, SLA (réponse 5 j, correction 90 j critique), canal sécurisé (HackerOne/Bugcrowd ou formulaire interne), publication après correctif, remerciements (hall of fame).

**Quand l'utiliser (triggers)** :
- ouvrir un VDP interne avant un bug bounty payant
- hors périmètre : pas de DoS, pas de social engineering (907)
- récompense 500-5000 € selon CVSS, délai 90 j critique

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es RSSI relation chercheurs. Tu définis : policy.md (périmètre, règles du jeu, safe harbor légal), grille de récompense (CVSS 4-7 = 500 €, 7-9 = 2000 €, 9+ = 5000 €), SLA, canal, processus de traitement (triage 5 j, validation, correctif, remerciement public après fix). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le périmètre (apps, APIs, mobile)
- La plateforme (HackerOne, Bugcrowd, Intigriti, ou interne)
- Le budget annuel et les SLA

**Méthode** :
1. Rédiger la policy : périmètre, hors-périmètre (DoS, spam, 907), règles (pas de test sur les users), safe harbor (pas de poursuites si bonne foi), contact sécurité dédié.
2. Grille de récompense par CVSS + facteurs (données perso = x2), payée sous 30 j après correctif.
3. Triage : accusé 5 j, validation (repro) 15 j, correctif 90 j (critique 30 j), paiement, publication après fix (coordination 1454? non — 1589 crise).
4. Hall of fame public + remerciements, relation long terme avec les bons chercheurs.
5. Métriques : nb de rapports, taux valide, délai moyen de fix, coût par bug vs pentest (439).

**Sorties attendues** :
- Le VDP/bug bounty publié (policy, grille, SLA, canal)
- Le processus de traitement (triage → fix → paiement → publication)
- Le hall of fame + métriques du programme

**Exemple de prompt** :
> « Ouvre un VDP interne en 2027 avant un bug bounty payant : policy (périmètre apps/API, hors DoS/social 907, safe harbor), grille CVSS (500-5000 €), SLA (réponse 5 j, fix 90 j critique), canal HackerOne, hall of fame, métriques. »

**Cas d'usage** : Apps exposées, produits SaaS. S'articule avec skills 439 (pentest), 440 (chasse menaces) et 754 (incidents).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
