---
num: 1732
date_ajout: "2026-11"
nom: "eBPF et conteneurs : isolation réseau fine (2027)"
emoji: "📦"
domaine: "Sécurité"
signal: "Isoler finement le réseau des conteneurs en 2027 avec eBPF (Cilium 1721) : chaque pod a une identité réseau, les policies L3-L7 s'appliquent par identité (pas par IP qui tourne), egress control (quelle IP externe joignable), DNS-aware (filtrer par nom de domaine, pas juste IP). Utilise pour la micro-segmentation conteneurs (1203 réseau classique). N'utilise pas sans Cilium (1721)."
mot_cle: "eBPF isolation réseau conteneurs 2027 identité pod policies L7 egress control DNS-aware micro-segmentation Cilium"
nom_court: "eBPF netns"
branche: "D23"
synonymes: ["chaque pod a une identité réseau (pas une IP qui tourne) : Cilium eBPF", "egress control : ce pod ne peut sortir que vers api.exemple.com (Cilium)", "filtrer par nom de domaine DNS (pas juste IP) : Cilium DNS-aware"]
cross_refs: [1721, 1203, 1644]
tags: ["2027"]
depends_on: [1721]
---

## 1732. 📦 eBPF et conteneurs : isolation réseau fine (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Micro-segmenter le réseau des conteneurs en 2027 avec eBPF/Cilium (1721) : identité réseau par pod (stable, pas l'IP), policies L3-L7 par identité, egress control (IPs/allowlist), filtres DNS-aware (par nom de domaine).

**Quand l'utiliser (triggers)** :
- les IPs des pods tournent, les règles par IP sont ingérables
- egress : ce pod ne doit appeler que api.stripe.com (Cilium)
- bloquer par nom de domaine (DNS), pas par IP résolue (Cilium)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es sécurité réseau conteneurs. Tu écris des CiliumNetworkPolicy : ingress/egress par identité (labels), par domaine DNS (toFQDNs), ports/protocoles, et tu vérifies avec Hubble (1722) que seuls les flux autorisés passent. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Cilium déployé (1721)
- Les identités (labels) des pods
- Les règles (allowlist domaines/IPs)

**Méthode** :
1. Identité : chaque pod = identité Cilium (basée sur ses labels), stable malgré les IPs changeantes — les policies citent les identités, pas les IPs.
2. Ingress : autoriser seulement le trafic venant de l'identité 'frontend' sur le port 8080.
3. Egress : allowlist — ex. le pod 'paiement' ne peut appeler que *.stripe.com (toFQDNs, DNS-aware) + le DNS interne ; tout le reste deny + log.
4. DNS-aware : toFQDNs résout les noms via le DNS du cluster, met à jour les IPs automatiquement.
5. Vérifier : Hubble (1722) montre les flux bloqués (deny) vs autorisés (allow) ; alertes sur les tentatives bloquées répétées (1417 → SIEM 1453).

**Sorties attendues** :
- Les CiliumNetworkPolicy par identité + egress allowlist (FQDN) déployées
- Hubble (1722) montrant allow vs deny conforme aux règles
- Les alertes (1417) sur tentatives egress bloquées → SIEM (1453)

**Exemple de prompt** :
> « Les IPs des pods tournent et les règles cassent : passe en Cilium (1721) — identité par pod (labels), egress allowlist par domaine (toFQDNs : uniquement api.stripe.com pour le pod paiement), vérification Hubble (1722) allow/deny, alertes sur les bloqués (1417→1453). »

**Cas d'usage** : Micro-segmentation conteneurs. S'articule avec skills 1721 (Cilium), 1203 (segmentation), 1644 (IoT) et 1722 (Hubble).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
