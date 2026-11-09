---
num: 1856
resume: "Committer des secrets chiffrés dans Git (GitOps) avec Sealed Secrets : kubeseal chiffre avec la clé publique du cluster, le controller déchiffre in-cluster — clé privée à backuper impérativement. Étape 1 : Installer le controller (helm) ; récupérer la clé publique : kubeseal --fetch-cert supérieur à pub.pem."
date_ajout: "2026-11"
nom: "Sealed Secrets (Bitnami) : secrets chiffrés dans Git (GitOps)"
emoji: "🏗️"
domaine: "Sécurité"
signal: "Committer des secrets CHIFFRÉS dans Git avec Sealed Secrets (Bitnami) : kubeseal chiffre avec la clé publique du cluster (asymétrique) — SealedSecret YAML committable ; le controller in-cluster déchiffre avec la clé privée. Clé privée cluster à backuper impérativement (sans elle, les SealedSecrets sont irrécupérables). Rotation de clé possible (re-encrypt). Alternative : SOPS (1857) pour les fichiers hors cluster. N'utilise pas de secrets en clair dans Git, même 'temporairement'."
mot_cle: "Sealed Secrets Bitnami kubeseal chiffrement asymétrique clé publique cluster SealedSecret YAML GitOps backup clé privée rotation re-encrypt"
nom_court: "Sealed Secrets"
branche: "D23"
synonymes: ["commiter un secret chiffré dans Git (kubeseal — SealedSecret) pour ArgoCD/Flux", "backup de la clé privée Sealed Secrets : sans elle, tout est perdu", "re-encrypt après rotation de clé : kubeseal --re-encrypt"]
cross_refs: [1854, 1857, 1851]
tags: ["2027"]
depends_on: [1851]
---

## 1856. 🏗️ Sealed Secrets (Bitnami) : secrets chiffrés dans Git (GitOps)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Committer des secrets chiffrés dans Git (GitOps) avec Sealed Secrets : kubeseal chiffre avec la clé publique du cluster, le controller déchiffre in-cluster — clé privée à backuper impérativement.

**Quand l'utiliser (triggers)** :
- GitOps (ArgoCD 1704) : comment mettre des secrets dans Git en sécurité ? (Sealed Secrets)
- backup de la clé privée du controller sealed-secrets (perte = secrets irrécupérables)
- chiffrer un secret existant : kubeseal < secret.yaml > sealed.yaml

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es SRE plateforme / GitOps. Tu installes le controller sealed-secrets, tu récupères la clé publique (kubeseal --fetch-cert), tu back up la clé privée (Vault 1852 ou coffre physique), et tu chiffre avec kubeseal. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le controller sealed-secrets installé
- La clé publique (fetch-cert)
- Le backup de la clé privée (impératif)

**Méthode** :
1. Installer le controller (helm) ; récupérer la clé publique : kubeseal --fetch-cert > pub.pem.
2. BACKUP la clé privée (secret sealed-secrets-key dans kube-system) -> copié dans Vault (1852) ou coffre offline.
3. Chiffrer : kubectl create secret generic api --from-literal=password=... --dry-run=client -o yaml | kubeseal --cert pub.pem -o yaml > sealed-api.yaml (committable).
4. ArgoCD/Flux (1704) applique le SealedSecret -> le controller déchiffre -> Secret k8s.
5. Rotation de clé : kubeseal --re-encrypt pour rechiffrer tous les SealedSecrets.

**Sorties attendues** :
- Les SealedSecret committés dans Git (chiffrés)
- La clé privée backupée (Vault/coffre)
- La procédure de rotation de clé documentee

**Exemple de prompt** :
> « Secret api-key Stripe en prod : kubeseal chiffre avec pub.pem -> sealed-stripe.yaml committé ; ArgoCD l'applique, le controller déchiffre in-cluster ; clé privée backupée dans Vault (1852) — commit Git ne contient que du chiffré. »

**Cas d'usage** : GitOps sécurisé. S'articule avec skills 1854, 1857, 1851, 1704.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
