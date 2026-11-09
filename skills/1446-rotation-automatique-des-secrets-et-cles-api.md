---
num: 1446
resume: "Automatiser la rotation des secrets/clés API en 2027 : vault central (Vault/AWS Secrets Manager), rotation tous les 90 jours, double validité pendant la transition, révocation immédiate en cas de fuite suspectée. Étape 1 : Inventorier tous les secrets (grep, vault scan) et les migrer dans le vault."
lang: "fr"
date_ajout: "2026-11"
nom: "Rotation automatique des secrets et cles API"
emoji: "🔑"
domaine: "Sécurité"
signal: "Mettre en place la rotation automatique des secrets et clés API en 2027 : vault (HashiCorp Vault, AWS/GCP Secrets Manager) avec renouvellement périodique (90 jours), double clé pendant la transition (ancienne + nouvelle), alerte si fuite. Utilise quand des clés sont en dur ou partagées. N'utilise pas pour les mots de passe utilisateurs (voir MFA)."
mot_cle: "rotation automatique secrets clés API vault 90 jours"
nom_court: "Rotation secrets"
branche: "D23"
synonymes: ["renouveler clés API automatiquement", "vault hashicorp rotation 90 jours", "fuite de clé détection"]
cross_refs: [306, 267, 1337]
tags: ["2027"]
depends_on: [306]
---

## 1446. 🔑 Rotation automatique des secrets et cles API (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Automatiser la rotation des secrets/clés API en 2027 : vault central (Vault/AWS Secrets Manager), rotation tous les 90 jours, double validité pendant la transition, révocation immédiate en cas de fuite suspectée.

**Quand l'utiliser (triggers)** :
- Nos clés API datent de 2 ans, les faire tourner
- Rotation auto des secrets avec un vault
- Fuite de clé : révoquer immédiatement

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es responsable gestion des secrets. Tu décris le vault (stockage chiffré, API de livraison dynamique), le schedule de rotation (90 j), la double clé (old+new valides 24 h), et la procédure de révocation d'urgence. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'inventaire des secrets (clés API, DB, certificats)
- Le vault choisi
- La fréquence de rotation (90 jours)

**Méthode** :
1. Inventorier tous les secrets (grep, vault scan) et les migrer dans le vault.
2. Activer la rotation auto (lease 90 jours) avec génération de nouvelle version.
3. Double validité : ancienne + nouvelle actives 24 h pendant la transition.
4. Apps lisent le secret dynamiquement (pas de copie en dur, skill 306).
5. Procédure fuite : révoquer (revoke) + rotation forcée + investigation logs.

**Sorties attendues** :
- Le vault déployé avec tous les secrets migrés
- La rotation auto à 90 jours active
- La procédure de révocation d'urgence testée

**Exemple de prompt** :
> « Nos clés API Stripe/OpenAI ont 2 ans et sont dans des .env : migre-les dans un vault avec rotation auto 90 jours et révocation d'urgence. »

**Cas d'usage** : Sécurité des accès, conformité (ISO 27001), réponse à incident. S'articule avec skills 306 (secrets), 267 (SBOM) et 1337 (mots de passe).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
