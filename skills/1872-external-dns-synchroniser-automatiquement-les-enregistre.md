---
num: 1872
date_ajout: "2026-11"
nom: "external-dns : synchroniser automatiquement les enregistrements DNS"
emoji: "🌐"
domaine: "Développement"
signal: "Synchroniser automatiquement les DNS (Route53, Cloudflare, OVH...) depuis les ressources k8s avec external-dns : Ingress/HTTPRoute/Service (LoadBalancer, annotation external-dns.alpha.kubernetes.io/hostname) — enregistrement A/CNAME créé/mis à jour/supprimé automatiquement. Policy upsert-only (sécurité), dry-run d'abord, filtres par domaine (txt registry pour la propriété). N'utilise pas de DNS manuels copiés (drift)."
mot_cle: "external-dns sync DNS automatique Route53 Cloudflare Ingress HTTPRoute Service LoadBalancer annotation hostname A CNAME txt registry policy upsert-only"
nom_court: "external-dns"
branche: "D16"
synonymes: ["créer automatiquement l'enregistrement DNS quand un Ingress est créé (external-dns)", "annotation external-dns.alpha.kubernetes.io/hostname: api.example.com", "policy upsert-only + dry-run d'abord (ne pas toucher aux DNS existants)"]
cross_refs: [1801, 1871, 609]
tags: ["2027"]
depends_on: [1801]
---

## 1872. 🌐 external-dns : synchroniser automatiquement les enregistrements DNS

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Synchroniser automatiquement les enregistrements DNS (Route53/Cloudflare) depuis Ingress/HTTPRoute/Service k8s avec external-dns (annotation hostname) — création/mise à jour/suppression auto, avec txt registry.

**Quand l'utiliser (triggers)** :
- nouvel Ingress api-v2.example.com : le DNS se crée tout seul (external-dns)
- policy upsert-only + dry-run : ne jamais supprimer/modifier des DNS existants
- txt registry : prouver la propriété du domaine avant de créer des enregistrements

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es ingénieur plateforme. Tu déploies external-dns avec les credentials du provider DNS (via ESO/Vault 1854, jamais en clair), policy upsert-only, domaine filtré, dry-run puis réel. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le provider DNS (Route53/Cloudflare) + credentials (Vault/ESO 1854)
- external-dns déployé
- Les annotations hostname sur les ressources

**Méthode** :
1. Déployer external-dns (helm) avec provider route53/cloudflare, credentials via ESO (1854), policy=upsert-only, txt-owner-id, domain-filter=example.com.
2. Annoter : external-dns.alpha.kubernetes.io/hostname: api.example.com sur HTTPRoute (1801) ou Service LB.
3. Dry-run d'abord (log 'would create'), puis réel : A/AAAA ou CNAME créé.
4. Vérifier : dig api.example.com -> IP du LB ; suppression de la ressource -> DNS supprimé (si owned).

**Sorties attendues** :
- Les DNS synchronisés automatiquement
- Le txt registry (propriété) actif
- Le dry-run -> prod documenté

**Exemple de prompt** :
> « HTTPRoute api-v2 annotée hostname api-v2.example.com + targetIP du Gateway -> external-dns crée l'enregistrement CNAME pointant sur le LB en 1 min ; suppression de la route -> enregistrement supprimé (car txt owner). »

**Cas d'usage** : DNS sans drift. S'articule avec skills 1801, 1871, 609, 1705.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
