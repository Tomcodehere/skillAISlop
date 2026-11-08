---
num: 1839
date_ajout: "2026-11"
nom: "Gouvernance data : classification, PII, accès RBAC/ABAC, rétention"
emoji: "🛡"
domaine: "Juridique"
signal: "Gouverner les données en 2027 : classification (public/interne/confidentiel/restreint), détection PII (email, téléphone, IBAN — cf 1440 pour les prompts), accès RBAC (rôles) ou ABAC (attributs : équipe, région, projet), row-level security (1788), rétention/légal hold, masking dynamique. Catalogue 1095 + tags PII. Conformité RGPD : registre des traitements, DPO, DPIA. N'utilise pas de rôles trop larges (accès 'all tables' en prod)."
mot_cle: "gouvernance data classification PII RGPD RBAC ABAC row-level security rétention legal hold masking DPIA registre traitements"
nom_court: "Gouvernance data"
branche: "D29"
synonymes: ["classer les données (public/interne/confidentiel/restreint) et taguer les PII", "RBAC vs ABAC pour l'accès aux données (attributs équipe/région/projet)", "RGPD : registre des traitements + DPIA + rétention/légal hold"]
cross_refs: [1095, 1788, 1440]
tags: ["2027"]
depends_on: [1095]
---

## 1839. 🛡 Gouvernance data : classification, PII, accès RBAC/ABAC, rétention

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Gouverner les données : classification (4 niveaux), tags PII, accès RBAC/ABAC + row-level security (1788), rétention et legal hold, registre RGPD des traitements — le tout catalogué (1095).

**Quand l'utiliser (triggers)** :
- quelles tables contiennent des PII ? (scan + tags dans le catalog 1095)
- accès ABAC : l'équipe finance Europe uniquement (pas US)
- RGPD : registre des traitements à jour + DPIA sur le nouveau projet

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es DPO / responsable gouvernance data. Tu classes les données (scan PII 1440 + tags 1095), tu mets les accès en ABAC (équipe/région/projet) avec RLS (1788), et tu tiens le registre RGPD + les rétentions. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le catalog 1095
- Le warehouse (RLS 1788, RBAC)
- Le registre RGPD

**Méthode** :
1. Classification : scanner les colonnes (PII : email/tel/IBAN — cf 1440), taguer dans le catalog (1095) : public/interne/confidentiel/restreint.
2. Accès : ABAC par attributs (équipe, région, projet) + RLS au niveau ligne (1788) ; jamais de rôle 'all tables' en prod.
3. RGPD : registre des traitements à jour, DPIA pour les nouveaux projets à risque, DPO contact, droit à l'effacement procédure.
4. Rétention : durées par classe de données, legal hold (suspension suppression) pour les litiges.

**Sorties attendues** :
- Les données classifiées et taguées PII (catalog 1095)
- Les accès ABAC+RLS en place (1788)
- Le registre RGPD + rétentions/legal hold documentés

**Exemple de prompt** :
> « Table clients : tag PII (email, téléphone) dans OpenMetadata (1836), accès ABAC : équipe finance + région=EU uniquement, RLS : un commercial ne voit que ses clients (owner_id = user) — audit RGPD OK. »

**Cas d'usage** : Conformité RGPD. S'articule avec skills 1095, 1788, 1440, 1836, 1786.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
