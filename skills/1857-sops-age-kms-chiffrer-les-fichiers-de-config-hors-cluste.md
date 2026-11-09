---
num: 1857
resume: "Chiffrer les fichiers de config (YAML, .env) hors cluster avec SOPS + age/KMS : valeurs chiffrées dans Git, déchiffrement local ou en CI (OIDC) — pre-commit pour bloquer les fuites. Étape 1 : Clé : age-keygen (clé privée dans Vault 1852/coffre) ou KMS (aws:kms arn)."
lang: "fr"
date_ajout: "2026-11"
nom: "SOPS + age/KMS : chiffrer les fichiers de config hors cluster"
emoji: "🗝️"
domaine: "Sécurité"
signal: "Chiffrer les fichiers de config (YAML/JSON/.env) hors cluster avec Mozilla SOPS + age (clés simples) ou KMS cloud (AWS/GCP/Azure) : le fichier committé ne contient que les valeurs chiffrées + métadonnées (clé, chiffrement) ; déchiffrement local ou en CI avec la clé. Pour les petits/moyens équipes (vs Vault 1852 pour l'entreprise). SOPS dans le pre-commit (1403) pour éviter les fuites. N'utilise pas de .env en clair dans Git."
mot_cle: "SOPS Mozilla age KMS chiffrer fichiers config YAML env CI pre-commit clés chiffrement métadonnées déchiffrement local"
nom_court: "SOPS"
branche: "D23"
synonymes: ["chiffrer un .env avant de le committer (sops + age ou KMS)", "sops en pre-commit (1403) : bloque un commit avec secret en clair", "déchiffrer en CI : sops -d avec la clé KMS (OIDC 1860)"]
cross_refs: [1856, 1852, 1403]
tags: ["2027"]
depends_on: [1856]
---

## 1857. 🗝️ SOPS + age/KMS : chiffrer les fichiers de config hors cluster

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Chiffrer les fichiers de config (YAML, .env) hors cluster avec SOPS + age/KMS : valeurs chiffrées dans Git, déchiffrement local ou en CI (OIDC) — pre-commit pour bloquer les fuites.

**Quand l'utiliser (triggers)** :
- chiffrer config/prod.yaml avant commit (sops --encrypt --kms ou age)
- pre-commit sops : un fichier avec secret en clair est bloqué au commit (1403)
- CI déchiffre avec KMS via OIDC (1860), jamais de clé en clair dans les secrets CI

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es développeur / SRE. Tu génères une clé age (ou configures KMS), tu chiffres avec sops -e, tu mets sops dans le pre-commit (update + encrypt), et la CI déchiffre via OIDC/KMS. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- age (clé privée à protéger) ou KMS cloud
- sops installé
- Le pre-commit (1403)

**Méthode** :
1. Clé : age-keygen (clé privée dans Vault 1852/coffre) ou KMS (aws:kms arn).
2. Chiffrer : sops -e --kms 'arn:aws:kms:...' config/prod.yaml > prod.enc.yaml (commit).
3. Pre-commit (1403) : sops --config .sops.yaml updatekeys + encrypt sur les fichiers modifiés.
4. CI (1413) : configure-aws-credentials OIDC (1860) puis sops -d prod.enc.yaml -> prod.yaml déployé.

**Sorties attendues** :
- Les fichiers de config chiffrés committés
- Le pre-commit anti-fuite actif
- Le déchiffrement CI (OIDC/KMS) fonctionnel

**Exemple de prompt** :
> « config/staging.env contient DATABASE_URL avec mot de passe : sops -e --kms arn... -> commit du .enc ; pre-commit bloque si quelqu'un commit le .env en clair ; CI déchiffre via OIDC AWS (1860) au déploiement. »

**Cas d'usage** : Config chiffrée hors cluster. S'articule avec skills 1856, 1852, 1403, 1413, 1860.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
