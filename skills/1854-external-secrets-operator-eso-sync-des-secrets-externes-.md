---
num: 1854
resume: "Déployer ESO (v0.10+) pour synchroniser les secrets d'un store externe (Vault, AWS/GCP/Azure — 15+ backends) vers des Secrets k8s via ExternalSecret (refreshInterval), sans que l'app ne connaisse le store. Étape 1 : helm install external-secrets (namespace external-secrets)."
lang: "fr"
date_ajout: "2026-11"
nom: "External Secrets Operator (ESO) : sync des secrets externes vers k8s"
emoji: "🔄"
domaine: "Sécurité"
signal: "Déployer External Secrets Operator (CNCF, v0.10+) pour synchroniser les secrets d'un store externe (Vault 1852, AWS Secrets Manager, GCP, Azure Key Vault — 15+ backends) vers des Secrets k8s natifs : SecretStore/ClusterSecretStore + ExternalSecret (refreshInterval, dataFrom). L'app ne voit que des Secrets k8s classiques. N'utilise pas ESO si le Vault agent injector (1858) suffit (moins d'objets etcd)."
mot_cle: "External Secrets Operator ESO v0.10 SecretStore ClusterSecretStore ExternalSecret refreshInterval sync Vault AWS Secrets Manager GCP Azure Key Vault 15 backends"
nom_court: "ESO"
branche: "D23"
synonymes: ["synchroniser Vault dans des Secrets k8s avec ESO (ExternalSecret refreshInterval 1h)", "ClusterSecretStore pour partager le backend Vault entre namespaces", "15+ backends ESO : Vault, AWS SM, GCP SM, Azure KV, Doppler, Infisical"]
cross_refs: [1852, 1851, 1855]
tags: ["2027"]
depends_on: [1852]
---

## 1854. 🔄 External Secrets Operator (ESO) : sync des secrets externes vers k8s

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Déployer ESO (v0.10+) pour synchroniser les secrets d'un store externe (Vault, AWS/GCP/Azure — 15+ backends) vers des Secrets k8s via ExternalSecret (refreshInterval), sans que l'app ne connaisse le store.

**Quand l'utiliser (triggers)** :
- mes secrets sont dans Vault, mes pods veulent des Secrets k8s : ESO (ExternalSecret)
- refreshInterval 1h : le Secret k8s se met à jour tout seul si Vault change
- ClusterSecretStore vault-backend partagé par tous les namespaces

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es SRE plateforme. Tu installes ESO (helm), tu déclares le ClusterSecretStore (backend Vault avec auth kubernetes 1852), et chaque app déclare un ExternalSecret pointant vers son path Vault. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- ESO installé (helm)
- Le ClusterSecretStore (Vault/AWS/...)
- Les ExternalSecret par app

**Méthode** :
1. helm install external-secrets (namespace external-secrets).
2. ClusterSecretStore : provider vault (server, path, auth kubernetes role=...) ou aws (region, auth IRSA/OIDC 1860).
3. ExternalSecret par app : secretStoreRef + dataFrom extract key=... + refreshInterval 1h + target Secret.
4. Vérifier : le Secret k8s est créé/mis à jour (kubectl get secret), la source Vault inchangée.
5. Rotation : quand Vault change, ESO resync à refreshInterval puis Reloader (1855) restart les pods.

**Sorties attendues** :
- ESO déployé + ClusterSecretStore configuré
- Les ExternalSecret -> Secrets k8s synchronisés
- Le refreshInterval actif (sync auto)

**Exemple de prompt** :
> « App api en ns=prod : ExternalSecret api-secrets (store vault-backend, dataFrom key=prod/api) refreshInterval 1h -> Secret api-secrets créé ; si le secret Vault change, le Secret k8s est mis à jour en 1 h max, Reloader (1855) restart le pod. »

**Cas d'usage** : Bridge store externe -> k8s. S'articule avec skills 1852, 1851, 1855, 1609.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
