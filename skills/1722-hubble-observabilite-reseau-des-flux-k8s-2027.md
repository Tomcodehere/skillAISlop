---
num: 1722
date_ajout: "2026-11"
nom: "Hubble : observabilité réseau des flux k8s (2027)"
emoji: "🔍"
domaine: "Développement"
signal: "Observer le réseau k8s en temps réel en 2027 avec Hubble (intégré à Cilium 1721) : service map (qui parle à qui, L3-L7), filtres par identité de workload, protocole (HTTP méthode/path, DNS, Kafka topic), métriques de flux (bytes, drops, retransmits), export vers Prometheus/Grafana (1416) et logs. Utilise pour déboguer 'pourquoi ce service ne répond plus'. N'utilise pas sans Cilium (1721)."
mot_cle: "hubble observabilité réseau k8s 2027 service map flux L3 L7 filtres identité protocole DNS HTTP Kafka export prometheus grafana"
nom_court: "Hubble"
branche: "D16"
synonymes: ["service map temps réel : quel pod parle à quel pod (Hubble)", "filtrer les flux par méthode HTTP path ou topic Kafka (Hubble)", "métriques de flux (bytes drops retransmits) exportées vers Grafana 1416"]
cross_refs: [1721, 1416, 1282]
tags: ["2027"]
depends_on: [1721]
---

## 1722. 🔍 Hubble : observabilité réseau des flux k8s (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Observer le réseau k8s en temps réel en 2027 avec Hubble (Cilium 1721) : service map des flux L3-L7 avec identités de workload, filtres (protocole, méthode HTTP, DNS, Kafka), métriques (bytes/drops/retransmits) vers Prometheus/Grafana (1416).

**Quand l'utiliser (triggers)** :
- pourquoi le service X ne répond plus à Y ? (service map Hubble)
- filtrer les flux : méthode HTTP POST sur /api/payments uniquement
- alertes sur drops/retransmits anormaux (Grafana 1416)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es SRE réseau. Tu actives Hubble (cilium hubble enable), tu ouvres l'UI ou le CLI (hubble observe), tu filtres par namespace/labels/pod, et tu exportes les métriques de flux vers Prometheus (1416). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Cilium déployé (1721) avec Hubble activé
- Les métriques à exporter (Prometheus 1416)
- Les filtres de debug

**Méthode** :
1. Activer : cilium hubble enable --ui (UI web) ou CLI hubble observe.
2. Service map : hubble ui → visualisation des flux entre workloads (avec direction, protocole, statut).
3. CLI : hubble observe --namespace prod --protocol http --http-method POST --since 5m.
4. Filtres L7 : HTTP (method, path, status), DNS (query), Kafka (topic), gRPC (method).
5. Métriques : exporter vers Prometheus (hubble metrics enable) : flux/s, bytes, drops, retransmits, latence — dashboards Grafana (1416), alertes (1417).
6. Rétention : Hubble garde en mémoire (ring buffer) — pour l'historique long, exporter vers ClickHouse/ES (1469).

**Sorties attendues** :
- Hubble actif (UI + CLI) avec service map temps réel
- Les filtres L7 (HTTP/DNS/Kafka/gRPC) utilisés en debug
- Les métriques de flux dans Prometheus/Grafana (1416) + alertes (1417)

**Exemple de prompt** :
> « Le service paiement ne répond plus : ouvre Hubble (Cilium 1721), filtre namespace=prod + HTTP + path /charge, vois les flux, les drops, les 5xx — cause trouvée en 2 min, métriques flux déjà dans Grafana (1416). »

**Cas d'usage** : Debug réseau k8s, sécurité réseau, perf. S'articule avec skills 1721 (Cilium), 1416 (Grafana), 1282 (monitoring) et 1417 (alertes).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
