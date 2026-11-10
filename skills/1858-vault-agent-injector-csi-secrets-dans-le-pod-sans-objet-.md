---
num: 1858
resume: "Injecter les secrets Vault directement dans le pod (fichier partagé via Vault Agent Injector, ou volume CSI) sans créer d'objet Secret dans etcd — 0 trace du secret dans le cluster. Étape 1 : Installer vault-agent-injector (helm), auth kubernetes (role -supérieur à policy)."
lang: "fr"
date_ajout: "2026-11"
nom: "Vault Agent Injector / CSI : secrets dans le pod sans objet Secret etcd"
emoji: "💉"
domaine: "Sécurité"
signal: "Injecter les secrets directement dans le pod SANS créer d'objet Secret dans etcd : Vault Agent Injector (sidecar qui écrit le secret dans un fichier partagé du pod, annotations vault.hashicorp.com/agent-inject) ou Vault CSI Provider (monte un volume CSI). Avantage : le secret n'est jamais dans etcd (même chiffré), ni dans un Secret k8s. Rotation : le sidecar re-écrit le fichier (app qui re-lit). Alternative à ESO (1854) quand on veut 0 trace etcd."
mot_cle: "Vault Agent Injector CSI Provider sidecar annotation agent-inject secret dans fichier pod volume CSI pas dans etcd rotation fichier"
nom_court: "Vault injector"
branche: "D23"
synonymes: ["injecter un secret Vault dans le pod sans objet Secret k8s (agent injector, annotation)", "Vault CSI Provider : volume CSI avec le secret, 0 trace dans etcd", "le sidecar Vault réécrit le fichier à la rotation (l'app re-lit)"]
cross_refs: [1852, 1854, 1851]
tags: ["2027"]
depends_on: [1852]
---

## 1858. 💉 Vault Agent Injector / CSI : secrets dans le pod sans objet Secret etcd

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Injecter les secrets Vault directement dans le pod (fichier partagé via Vault Agent Injector, ou volume CSI) sans créer d'objet Secret dans etcd — 0 trace du secret dans le cluster.

**Quand l'utiliser (triggers)** :
- 0 secret dans etcd : Vault Agent Injector (sidecar) au lieu d'ESO 1854
- annotations vault.hashicorp.com/agent-inject-secret-* sur le pod
- Vault CSI Provider : volume monté avec le secret, pas d'objet Secret

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es SRE plateforme. Tu installes l'agent injector (helm), tu ajoutes les annotations au pod (role + path du secret), et le secret apparaît dans /vault/secrets/ du conteneur — jamais dans etcd. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Vault Agent Injector installé (helm)
- Un rôle Vault pour le SA du pod (1852)
- Le pod à annoter

**Méthode** :
1. Installer vault-agent-injector (helm), auth kubernetes (role -> policy).
2. Annotations sur le pod : vault.hashicorp.com/agent-inject: 'true', role, agent-inject-secret-db: 'path' + template {{ secret }}.
3. Le sidecar écrit /vault/secrets/db avec le contenu ; l'app lit ce fichier.
4. Rotation (1853 dynamic) : le sidecar réécrit le fichier, l'app re-lit (ou restart via Reloader 1855 si env).
5. Vérifier : kubectl get secrets -> aucun objet créé pour ce secret ; etcd ne contient rien.

**Sorties attendues** :
- Le secret injecté dans le pod (fichier /vault/secrets/)
- 0 objet Secret créé (vérifié etcd)
- La rotation par réécriture du fichier

**Exemple de prompt** :
> « Pod api : annotations agent-inject avec role=api et secret database/creds/api (dynamic 1853) -> au démarrage, /vault/secrets/db contient user/pass TTL 24 h ; kubectl get secrets ne montre rien ; à expiration Vault renouvelle et réécrit le fichier. »

**Cas d'usage** : 0 trace etcd. S'articule avec skills 1852, 1854, 1851, 1853.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
