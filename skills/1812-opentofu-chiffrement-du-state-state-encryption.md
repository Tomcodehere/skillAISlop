---
num: 1812
resume: "Activer la state encryption d'OpenTofu (1.7+) : chiffrement AES-256-GCM du state local et remote avec clé externe (KMS cloud, age ou fichier) — le state contient des secrets en clair. Étape 1 : Choisir le key provider : aws:kms / gcp:kms / azurerm:keyvault (recommandé) ou age/fichier pour du local."
date_ajout: "2026-11"
nom: "OpenTofu : chiffrement du state (state encryption)"
emoji: "🔒"
domaine: "Sécurité"
signal: "Chiffrer le state Terraform/OpenTofu au repos et en transit avec la state encryption d'OpenTofu (depuis 1.7) : clés externes (AWS KMS, GCP KMS, Azure Key Vault, age, ou fichier), chiffrement AES-256-GCM du state local ET du state remote (S3/GCS avec clé KMS). Le state contient des secrets en clair : sans chiffrement, un leak de bucket = compromission. N'utilise pas Terraform open CLI (pas de feature équivalente)."
mot_cle: "OpenTofu state encryption chiffrement state AES-256-GCM KMS AWS GCP Azure key Vault age secrets dans le state"
nom_court: "State encryption"
branche: "D23"
synonymes: ["chiffrer le terraform state (OpenTofu state encryption KMS) : le state contient des secrets", "state S3 non chiffré = risque : activer state encryption OpenTofu 1.7+", "clés externes KMS pour le state : aws:kms, gcp:kms, azurerm:keyvault, age, fichier"]
cross_refs: [1811, 1851, 1852]
tags: ["2027"]
depends_on: [1811]
---

## 1812. 🔒 OpenTofu : chiffrement du state (state encryption)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Activer la state encryption d'OpenTofu (1.7+) : chiffrement AES-256-GCM du state local et remote avec clé externe (KMS cloud, age ou fichier) — le state contient des secrets en clair.

**Quand l'utiliser (triggers)** :
- notre state S3 est en clair et contient des mots de passe de BDD
- activer le chiffrement du state : OpenTofu state encryption + KMS
- migrer un state existant vers le chiffrement (sans le casser)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es responsable sécurité IaC. Tu configures encryption { key_provider ... } dans le bloc terraform, tu choisis la clé (KMS cloud recommandé), et tu migres un state existant en chiffré sans downtime (tofu state reconfigure). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- OpenTofu 1.7+
- La clé de chiffrement (KMS/age/fichier)
- Le state existant (local ou remote)

**Méthode** :
1. Choisir le key provider : aws:kms / gcp:kms / azurerm:keyvault (recommandé) ou age/fichier pour du local.
2. Configurer encryption { key_provider aws:kms ... method aes-gcm { keys = ... } } dans le bloc terraform.
3. tofu init -reconfigure pour migrer le state existant (il est rechiffré).
4. Vérifier : le fichier state local est chiffré (contenu illisible), le remote aussi (S3 SSE-KMS).
5. Gérer les clés : rotation KMS, accès restreint (IAM), backup de la clé age.

**Sorties attendues** :
- Le state chiffré (local + remote) avec clé externe
- La migration du state existant réussie (tofu init -reconfigure)
- La procédure de rotation de clé documentee

**Exemple de prompt** :
> « State S3 prod contenant des creds BDD : encryption aws:kms key_id arn:aws:kms:... — tofu init -reconfigure, le state est rechiffré, lecture via KMS uniquement (IAM restreint à l'équipe platform). »

**Cas d'usage** : Protéger le state IaC. S'articule avec skills 1811, 1851/1852 (Vault/secrets), 1860 (OIDC CI).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
