---
num: 1447
date_ajout: "2026-11"
nom: "IAM cloud : auditer et reduire les permissions (2027)"
emoji: "🚡"
domaine: "Sécurité"
signal: "Auditer et réduire les permissions IAM cloud en 2027 (AWS/GCP/Azure) selon le moindre privilège : inventaire des rôles/policies, détection des admins, des clés longue durée, des ressources publiques, rotation des credentials, IaC pour les droits. Utilise quand on durcit un compte cloud. N'utilise pas pour l'IAM applicatif interne (voir 458)."
mot_cle: "IAM cloud moindre privilège audit permissions AWS GCP Azure"
nom_court: "IAM cloud"
branche: "D23"
synonymes: ["réduire permissions admin cloud", "audit accès AWS trop larges", "clés longue durée supprimer"]
cross_refs: [1070, 197, 507]
tags: ["2027"]
depends_on: [197]
---

## 1447. 🚡 IAM cloud : auditer et reduire les permissions (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Auditer un compte cloud en 2027 et appliquer le moindre privilège IAM : supprimer les admins inutiles, les clés > 90 jours, les ressources publiques, et gérer les droits en IaC (Terraform) avec revue de PR.

**Quand l'utiliser (triggers)** :
- Qui a les droits admin sur notre AWS ?
- Trop de permissions larges, audit IAM
- Clés d'accès de 2 ans à supprimer

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es auditeur IAM cloud. Tu utilises les outils (AWS IAM Access Analyzer, GCP Recommender), tu cibles : wildcard policies, admins, clés anciennes, S3/buckets publics, et tu mets les droits en IaC avec revue. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le compte cloud et ses utilisateurs/rôles
- L'outil d'audit (Access Analyzer, Forseti)
- La politique de droits cible (matrice rôle/ressource)

**Méthode** :
1. Inventorier users, rôles, policies (aws iam list-*).
2. Détecter : admin wildcard, clés > 90 j, ressources publiques (Access Analyzer).
3. Remplacer par des rôles à privilège minimal + MFA + session courte.
4. Supprimer les clés longue durée, passer en rôle assumable (SSO).
5. Gérer les droits en IaC (Terraform) avec revue de PR obligatoire.

**Sorties attendues** :
- Le rapport d'audit IAM (écarts trouvés)
- Les permissions réduites (moins de wildcard)
- Les droits en IaC + revue de PR

**Exemple de prompt** :
> « Personne ne sait qui a les droits admin sur notre compte AWS : fais l'audit IAM (Access Analyzer, clés anciennes, buckets publics) et réduis au moindre privilège. »

**Cas d'usage** : Sécurité cloud, conformité, réponse à incident. S'articule avec skills 1070 (blueprint IAM), 197 (permissions accès) et 507 (audit cloud).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
