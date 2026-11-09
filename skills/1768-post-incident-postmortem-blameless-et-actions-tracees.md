---
num: 1768
resume: "Rédiger un postmortem blameless après chaque incident majeur (chronologie, cause racine via 5 pourquoi, facteurs contributifs) et transformer les leçons en actions correctives tracées (responsable + échéance) dans le backlog. Étape 1 : Reunir les acteurs sous 72 h, reconstruire la chronologie factuelle (depuis les traces/logs, pas la mémoire)."
date_ajout: "2026-11"
nom: "Post-incident : postmortem blameless et actions tracées"
emoji: "🧪"
domaine: "Gestion"
signal: "Mener en 2027 un postmortem blameless après chaque incident SEV1/SEV2 : chronologie factuelle, cause racine (5 pourquoi), facteurs contributifs, et actions correctives avec responsable et échéance tracées dans le backlog (pas dans un doc qui dort). Règle d'or : on ne blame jamais une personne, on répare le système. N'utilise pas pour les incidents mineurs (note rapide suffit)."
mot_cle: "postmortem blameless incident SEV cause racine 5 pourquoi actions correctives tracees 2027"
nom_court: "Postmortem blameless"
branche: "D25"
synonymes: ["post-incident blameless : on ne blame pas la personne, on repare le systeme", "5 pourquoi pour trouver la cause racine de l'incident", "actions correctives avec responsable et echeance dans le backlog"]
cross_refs: [1758, 1764, 1761]
tags: ["2027"]
depends_on: [1758]
---

## 1768. 🧪 Post-incident : postmortem blameless et actions tracées (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Rédiger un postmortem blameless après chaque incident majeur (chronologie, cause racine via 5 pourquoi, facteurs contributifs) et transformer les leçons en actions correctives tracées (responsable + échéance) dans le backlog.

**Quand l'utiliser (triggers)** :
- incident SEV1 de 2 h hier, qui ecrit le postmortem ?
- la cause racine est 'erreur humaine' — creuser avec les 5 pourquoi
- les actions du dernier postmortem ne sont jamais faites

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es responsable incident / engineering manager. Tu anime la revue blameless sous 72 h, tu exiges une chronologie factuelle et une cause racine système (jamais 'faute de X'), et chaque action corrective a un responsable et une échéance dans le backlog avec suivi. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les logs et métriques de l'incident (1753, 1762)
- Les acteurs de l'incident
- Le backlog pour tracer les actions

**Méthode** :
1. Reunir les acteurs sous 72 h, reconstruire la chronologie factuelle (depuis les traces/logs, pas la mémoire).
2. 5 pourquoi jusqu'a la cause racine systemique (ex. 'pas de canary' plutot que 'mauvais deploiement').
3. Lister les facteurs contributifs (fatigue, outillage, doc manquante).
4. Actions correctives : chacune avec responsable, échéance, et lien dans le backlog — revue à J+30 de leur avancement.

**Sorties attendues** :
- Le postmortem publie (blameless, chronologie, cause racine)
- 5-10 actions correctives tracees avec responsable et echeance
- Le suivi a J+30 : actions faites / en retard

**Exemple de prompt** :
> « SEV1 de 2 h (deploiement sans canary) : 5 pourquoi -> cause racine 'pas de deploiement progressif obligatoire sur ce service' -> actions : canary auto (1418), runbook rollback (1764), alerte config (1761), responsable + echeance pour chacune, revue J+30. »

**Cas d'usage** : Apprendre de chaque incident. S'articule avec skills 1758 (gestion incident), 1764 (runbooks), 1761 (alerting).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
