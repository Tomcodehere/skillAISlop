---
num: 1871
resume: "Automatiser les certificats TLS avec cert-manager (Issuer/ClusterIssuer ACME Let's Encrypt ou Vault PKI) : émission, renouvellement auto, injection Gateway API/Ingress (1801). Étape 1 : Installer cert-manager + créer ClusterIssuer letsencrypt-prod (ACME, DNS-01 si wildcard via Cloudflare API token)."
lang: "fr"
date_ajout: "2026-11"
nom: "cert-manager : certificats TLS automatiques"
emoji: "🔒"
domaine: "Développement"
signal: "Automatiser les certificats TLS avec cert-manager : Issuer/ClusterIssuer (Let's Encrypt ACME HTTP-01 ou DNS-01 pour les wildcards, Vault PKI 1852, CA interne), Certificate CR — renouvellement auto (~30 j avant expiration), injection dans Ingress/HTTPRoute (1801) ou Gateway API. Alertes sur expiration proche (1417). N'utilise pas de certificats manuels copiés (expirent, oubliés)."
mot_cle: "cert-manager Issuer ClusterIssuer Let's Encrypt ACME HTTP-01 DNS-01 wildcard Vault PKI Certificate renouvellement auto Gateway API"
nom_court: "cert-manager"
branche: "D16"
synonymes: ["certificat TLS auto Let's Encrypt sur HTTPRoute (cert-manager + ACME)", "wildcard *.example.com : DNS-01 (Cloudflare/Route53) pas HTTP-01", "certificat Vault PKI interne (cert-manager issuer vault)"]
cross_refs: [1801, 1852, 1417]
tags: ["2027"]
depends_on: [1801]
---

## 1871. 🔒 cert-manager : certificats TLS automatiques

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Automatiser les certificats TLS avec cert-manager (Issuer/ClusterIssuer ACME Let's Encrypt ou Vault PKI) : émission, renouvellement auto, injection Gateway API/Ingress (1801).

**Quand l'utiliser (triggers)** :
- certificat Let's Encrypt auto-renouvelé avant expiration (cert-manager)
- wildcard *.example.com : ACME DNS-01 avec Cloudflare
- certificats internes via Vault PKI (cert-manager issuer vault 1852)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es ingénieur plateforme. Tu installes cert-manager (helm), tu déclares le ClusterIssuer (ACME staging d'abord, puis prod), et chaque Certificate renouvelle automatiquement ~30 j avant expiration. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- cert-manager installé (helm)
- Le ClusterIssuer (ACME/Vault)
- Les domaines à certifier

**Méthode** :
1. Installer cert-manager + créer ClusterIssuer letsencrypt-prod (ACME, DNS-01 si wildcard via Cloudflare API token).
2. Tester d'abord avec letsencrypt-staging (rate limits).
3. Certificate CR par domaine -> Secret TLS créé, renouvelé auto.
4. Brancher sur HTTPRoute/Gateway (1801) tls: secretName.
5. Alerte : certificat expire dans < 15 j (métrique cert-manager 1417).

**Sorties attendues** :
- Les certificats émis et auto-renouvelés
- Les alertes expiration configurées
- Le passage staging->prod documenté

**Exemple de prompt** :
> « ClusterIssuer letsencrypt-prod (DNS-01 Cloudflare) + Certificate pour *.example.com -> Secret tls wildcard renouvelé auto tous les ~60 j ; HTTPRoute api.example.com référence ce secret, 0 intervention manuelle. »

**Cas d'usage** : TLS sans friction. S'articule avec skills 1801 (Gateway API), 1852 (Vault PKI), 1417, 609.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
