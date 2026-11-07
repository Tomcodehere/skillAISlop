---
num: 1724
date_ajout: "2026-11"
nom: "Pixie / Beyla : observabilité zero-instrumentation (2027)"
emoji: "🧮"
domaine: "Data & IA"
signal: "Observer une application en 2027 SANS toucher au code avec Pixie (eBPF, CNCF sandbox, auto-trace HTTP/gRPC/Redis/MySQL/Postgres + service map + requêtes SQL live) ou Beyla (eBPF, OTel auto, tout langage, traces+metrics+logs sans SDK). Choisir : Pixie = k8s natif riche ; Beyla = multi-langages léger, standard OTel (1680). N'utilise pas si l'app est déjà instrumentée OTel manuellement."
mot_cle: "pixie beyla observabilité zero-instrumentation eBPF 2027 auto-trace HTTP gRPC Redis Postgres OTel service map"
nom_court: "Pixie/Beyla"
branche: "D14"
synonymes: ["tracer une appli legacy sans toucher au code (Pixie/Beyla eBPF)", "Beyla : OTel auto pour n'importe quel langage (Go Rust Java Python)", "Pixie : requêtes SQL live + service map k8s sans SDK (1680)"]
cross_refs: [1720, 1680, 1282]
tags: ["2027"]
depends_on: [1720]
---

## 1724. 🧮 Pixie / Beyla : observabilité zero-instrumentation (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Observer une appli en 2027 sans instrumentation manuelle (zero-instrumentation eBPF) : Pixie (CNCF, k8s natif : service map, requêtes SQL live, protocoles auto) ou Beyla (OTel auto multi-langages, traces+métriques+logs standard 1680).

**Quand l'utiliser (triggers)** :
- mon appli legacy en Go n'a aucune métrique, sans toucher au code
- Beyla : OTel auto (traces+métriques+logs) pour Java/Go/Python/Rust
- Pixie : voir les requêtes Postgres lentes en live sur le cluster

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es SRE observabilité. Tu déploies Beyla (DaemonSet eBPF, un binaire, génère spans/métriques OTel standards 1680 vers Grafana 1416) ou Pixie (CLI/helm, UI riche k8s), tu valides sur une app legacy sans code modifié. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les apps à observer (sans toucher au code)
- Le cluster k8s (kernel 5.8+, 1720)
- Le backend OTel (Grafana 1416 / Jaeger)

**Méthode** :
1. Choisir : Beyla (léger, OTel standard 1680, tout langage, DaemonSet simple) vs Pixie (UI k8s riche, requêtes SQL live, plus lourd).
2. Beyla : déployer en DaemonSet (eBPF), configurer l'export OTel (endpoint Grafana/Jaeger 1416), vérifier : traces HTTP/gRPC + métriques RED (rate/errors/duration) + logs apparaissent sans code modifié.
3. Pixie : px deploy (CLI), ouvrir l'UI (px.dev ou self-host), voir le service map, les requêtes SQL/Redis live, les latences p99 par endpoint.
4. Valider : une app legacy (ex. vieux service Java) a soudain traces complètes + métriques, zéro ligne de code modifiée.
5. Coût : overhead eBPF mesuré (moins de 5 % de CPU), rétention des traces (échantillonnage si gros volume).

**Sorties attendues** :
- L'observabilité zero-instrumentation déployée (Beyla ou Pixie)
- Les traces/métriques OTel (1680) de l'app legacy sans code modifié
- L'overhead eBPF mesuré (moins de 5 % de CPU)

**Exemple de prompt** :
> « Mon vieux service Java n'a aucune métrique et on ne peut pas toucher au code : déploie Beyla (eBPF, DaemonSet) → traces OTel (1680) + métriques RED automatiques vers Grafana (1416), zéro code modifié, overhead mesuré sous 5 % CPU. »

**Cas d'usage** : Legacy, k8s, microservices. S'articule avec skills 1720 (eBPF), 1680 (OTel), 1282 (monitoring) et 1416 (Grafana).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
