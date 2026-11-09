---
num: 1820
resume: "Détecter le drift IaC en continu (plan -detailed-exitcode en CI hebdo + terraform query 1818) et bloquer les plans non conformes en CI via policy as code (OPA/Conftest, compatible OpenTofu ; Sentinel si HCP). Étape 1 : CI hebdo : tofu plan -detailed-exitcode -out=tfplan ; exit 2 = drift détecté -supérieur à alerte + ticket auto."
date_ajout: "2026-11"
nom: "Drift detection et policy as code sur l'IaC (OPA vs Sentinel)"
emoji: "🛡"
domaine: "Sécurité"
signal: "Détecter le drift IaC en continu et bloquer les plans non conformes en CI : drift = différence entre le state et la réalité (terraform query 1818, ou plan -detailed-exitcode en CI hebdo) ; policy as code = OPA/Conftest (open source, testable localement, OpenTofu-compatible) vs Sentinel (HCP Terraform only). Règles : pas de ressource publique, tags obligatoires, chiffrement activé, instance types autorisés."
mot_cle: "drift detection IaC terraform plan -detailed-exitcode CI hebdo OPA Conftest policy as code vs Sentinel HCP tags obligatoires"
nom_court: "Drift & policies"
branche: "D23"
synonymes: ["détecter le drift : plan -detailed-exitcode en CI hebdo + terraform query 1818", "OPA Conftest pour valider les plans terraform (open source) vs Sentinel (HCP only)", "bloquer en CI un plan avec une S3 publique ou sans tag cost-center"]
cross_refs: [1818, 1811, 1413]
tags: ["2027"]
depends_on: [1811]
---

## 1820. 🛡 Drift detection et policy as code sur l'IaC (OPA vs Sentinel)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Détecter le drift IaC en continu (plan -detailed-exitcode en CI hebdo + terraform query 1818) et bloquer les plans non conformes en CI via policy as code (OPA/Conftest, compatible OpenTofu ; Sentinel si HCP).

**Quand l'utiliser (triggers)** :
- le drift s'accumule : ressources modifiées en console jamais ramenées au state
- bloquer en CI : S3 publique, pas de tag cost-center, instance non autorisée
- OPA vs Sentinel : lequel pour notre CI (OpenTofu vs HCP)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es responsable sécurité IaC / DevOps. Tu mets en CI un job hebdo de drift (plan -detailed-exitcode + query 1818) et un gate de policy (conftest test sur le plan JSON) : deny si ressource non conforme, avec remediation auto quand possible. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le repo IaC + CI (1413)
- OPA/Conftest (ou Sentinel si HCP)
- Les règles de conformité (tags, chiffrement, types)

**Méthode** :
1. CI hebdo : tofu plan -detailed-exitcode -out=tfplan ; exit 2 = drift détecté -> alerte + ticket auto.
2. Gate policy : conftest test tfplan.json avec rules.rego (deny public S3, require tags, require encryption).
3. Bloquer le merge si policy échoue (GitHub required check).
4. Remediation : pour les drifts simples, tofu apply pour réaligner (avec revue).
5. Sentinel si HCP Terraform : policies en HCL, enforcement mode hard.

**Sorties attendues** :
- Le job CI de drift hebdomadaire actif
- Les policies OPA/Conftest testées et bloquantes en PR
- Le rapport de conformité (0 ressource non conforme)

**Exemple de prompt** :
> « PR qui crée une S3 sans tag cost-center et en public : conftest deny -> check CI rouge, PR bloquée ; drift hebdo : terraform query trouve une EC2 modifiée en console -> ticket auto + apply de réalignement après revue. »

**Cas d'usage** : Gouverner l'IaC. S'articule avec skills 1818, 1811, 1413 (CI), 1705 (Kyverno k8s), 1812.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
