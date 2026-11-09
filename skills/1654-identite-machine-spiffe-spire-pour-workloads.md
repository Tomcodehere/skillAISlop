---
num: 1654
resume: "Donner une identité cryptographique à chaque workload en 2027 avec SPIFFE/SPIRE : SVID (certificat X.509 à courte durée de vie, renouvelé automatiquement), mTLS entre services, plus de secrets longue durée (1446), révocation instantanée. Étape 1 : Déployer SPIRE server + agents (sur chaque nœud), configurer les attestations (k8s ServiceAccount, AWS instance profile, etc.)."
date_ajout: "2026-11"
nom: "Identite machine : SPIFFE/SPIRE pour workloads"
emoji: "🖥️"
domaine: "Sécurité"
signal: "Gérer l'identité des machines (workloads, conteneurs, services cloud) en 2027 avec SPIFFE/SPIRE : chaque workload a une identité cryptographique (SVID, certificat X.509 court) émise automatiquement, mTLS entre services, pas de clés longue durée (1446). Utilise dans un mesh de services/k8s. N'utilise pas pour l'identité utilisateur (501)."
mot_cle: "SPIFFE SPIRE identité machine workloads SVID certificat X.509 court mTLS mesh services 2027"
nom_court: "Identité machine"
branche: "D23"
synonymes: ["chaque conteneur a son identité crypto (SPIFFE SVID)", "mTLS automatique entre services (SPIRE)", "plus de clés API longue durée entre services (1446)"]
cross_refs: [1644, 1446, 609]
tags: ["2027"]
depends_on: [609]
---

## 1654. 🖥️ Identite machine : SPIFFE/SPIRE pour workloads (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Donner une identité cryptographique à chaque workload en 2027 avec SPIFFE/SPIRE : SVID (certificat X.509 à courte durée de vie, renouvelé automatiquement), mTLS entre services, plus de secrets longue durée (1446), révocation instantanée.

**Quand l'utiliser (triggers)** :
- mes microservices s'authentifient avec des clés API dans des .env
- certificat X.509 court par workload, renouvelé auto (SPIRE)
- mTLS automatique entre tous les services du mesh

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte identité infra. Tu déploies SPIRE (serveur + agents), chaque workload s'enregistre (attestation : k8s SA, cloud metadata, node), reçoit un SVID (certificat 1 h), le renouvelle auto, mTLS via Envoy/Linkerd. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le mesh de services (k8s 609, VMs, cloud)
- SPIRE (serveur + agents)
- Le proxy mTLS (Envoy/Linkerd)

**Méthode** :
1. Déployer SPIRE server + agents (sur chaque nœud), configurer les attestations (k8s ServiceAccount, AWS instance profile, etc.).
2. Chaque workload obtient un SPIFFE ID (spiffe://trust-domain/ns/xxx/sa/yyy) + SVID (certificat X.509, TTL 1 h, renouvelé auto).
3. mTLS : le proxy (Envoy/Linkerd) présente le SVID, vérifie celui du pair, pas de mot de passe/clé longue durée.
4. Autorisation : policies SPIRE (qui peut appeler qui, ex. frontend→api seulement).
5. Révocation : retirer l'attestation → plus de SVID émis, les anciens expirent en 1 h.

**Sorties attendues** :
- SPIRE déployé, chaque workload a un SVID renouvelé auto
- Le mTLS automatique entre services (plus de secrets longue durée)
- Les policies d'autorisation (qui appelle qui)

**Exemple de prompt** :
> « Mes 30 microservices s'authentifient avec des clés API dans des .env (volées = catastrophe) : SPIRE leur donne un certificat X.509 de 1 h renouvelé auto (SPIFFE), mTLS via Envoy, révocation en retirant l'attestation. »

**Cas d'usage** : Mesh de services, k8s, multi-cloud. S'articule avec skills 1644 (IoT), 1446 (rotation secrets) et 609 (k8s).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
