---
num: 1918
date_ajout: "2026-11"
nom: "Gérer un litige chantier (mise en demeure, expertise)"
emoji: "⚖️"
domaine: "Artisanat & loisirs créatifs"
signal: "Gérer un litige de chantier : constat amiable contradictoire (photos, rapport), mise en demeure par LRAR avec délai, expertise judiciaire ou amiable (désignation d'expert, coût partagé ou à la charge du perdant), médiation/conciliation, activation de la décennale/RC Pro si dommage couvert (déclaration à l'assureur sous 5 jours ouvrés), tribunal judiciaire. Préserver les preuves. N'utilise pas pour un litige de voisinage (voir 864)."
mot_cle: "litige chantier BTP expertise médiation"
nom_court: "Litige chantier"
branche: "D31"
synonymes: ["litige travaux artisan client que faire", "mise en demeure LRAR chantier", "déclarer sinistre décennale 5 jours"]
cross_refs: [1917, 1907, 981]
---

## 1918. ⚖️ Gérer un litige chantier (mise en demeure, expertise)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Résoudre un litige de chantier dans les règles (constat, mise en demeure, expertise, assurance) en préservant ses droits.

**Quand l'utiliser (triggers)** :
- client mécontent chantier recours
- comment déclarer un sinistre à la décennale
- expertise judiciaire travaux coût

**Hors périmètre** :
- La réception normale (voir 1917).
- Les litiges commerciaux hors BTP (voir 981).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es juriste du bâtiment. Tu décris la procédure amiable puis judiciaire, la déclaration à l'assurance (délai 5 jours ouvrés) et la préservation des preuves. Tu restes factuel, sans garantir l'issue.

**Inputs requis** :
- La nature du litige (malfaçon, retard, impayé)
- Les preuves disponibles (photos, mails, PV)
- Le contrat et les assurances

**Méthode** :
1. Constater contradictoirement (rapport photo daté), tenter la conciliation.
2. LRAR de mise en demeure avec délai précis.
3. Déclarer le sinistre à la décennale/RC Pro sous 5 jours ouvrés si applicable.
4. Expertise (amiable ou judiciaire) puis négociation ou tribunal.

**Sorties attendues** :
- Un dossier de litige documenté
- La déclaration d'assurance envoyée dans les délais

**Exemple de prompt** :
> « « Le carrelage présente des fissures 2 mois après la réception : quelles démarches, la décennale intervient-elle ? » »

**Cas d'usage** : Litige après chantier. S'articule avec les skills 1917, 1907, 981. S'articule avec les skills 1917, 1907, 981.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées
