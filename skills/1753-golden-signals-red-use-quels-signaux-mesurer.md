---
num: 1753
date_ajout: "2026-11"
nom: "Golden signals + RED + USE : quels signaux mesurer"
emoji: "📊"
domaine: "Data"
signal: "Choisir les bons signaux en 2027 : Golden Signals (Google SRE : latence, trafic, erreurs, saturation — la vision service), RED (Rate/Errors/Duration — par endpoint), USE (Utilization/Saturation/Errors — par ressource machine). Règle : Golden Signals pour le service, RED pour les endpoints, USE pour l'infra. Toujours commencer par ceux-là avant d'ajouter des métriques custom. N'utilise pas pour remplacer le jugement métier (351)."
mot_cle: "golden signals RED USE 2027 latence trafic erreurs saturation Rate Errors Duration Utilization choisir signaux"
nom_court: "Signaux"
branche: "D17"
synonymes: ["golden signals : latence trafic erreurs saturation (Google SRE 2027)", "RED par endpoint (Rate Errors Duration) vs USE par ressource (Utilization Saturation Errors)", "commencer par golden signals avant les métriques custom"]
cross_refs: [351, 1416, 1282]
tags: ["2027"]
depends_on: [351]
---

## 1753. 📊 Golden signals + RED + USE : quels signaux mesurer (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Choisir les bons signaux d'observabilité en 2027 : Golden Signals (latence, trafic, erreurs, saturation — vue service), RED (Rate/Errors/Duration — par endpoint), USE (Utilization/Saturation/Errors — par ressource) — avant toute métrique custom.

**Quand l'utiliser (triggers)** :
- quelles métriques mesurer en priorité en 2027 ? (golden signals)
- RED : rate/errors/duration par endpoint API
- USE : utilization/saturation/errors par ressource (CPU, disque 1731, réseau)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es SRE. Tu appliques : Golden Signals sur chaque service (dashboard 1416), RED sur chaque endpoint critique, USE sur chaque ressource (CPU, mémoire, disque 1731 eBPF, réseau 1722 Hubble), puis seulement les custom métier (351). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le service/endpoint/ressource à monitorer
- La stack (Prometheus 1416 / OTel 1680)
- Les alertes (1417)

**Méthode** :
1. Golden Signals (service) : latence (p50/p95/p99 1416), trafic (req/s), erreurs (taux 5xx), saturation (CPU/mémoire/file d'attente).
2. RED (endpoint) : Rate (req/s), Errors (taux), Duration (latence) — ex. POST /checkout.
3. USE (ressource) : Utilization (% utilisé), Saturation (file d'attente, I/O disque 1731), Errors (disque plein, drops réseau 1722).
4. Dashboards Grafana (1416) : 1 par service (golden) + 1 par ressource (USE) + endpoints RED critiques.
5. Alertes (1417) sur ces signaux uniquement au début, puis ajouter custom métier (SLO 351) — jamais l'inverse.

**Sorties attendues** :
- Les 3 familles de signaux déployées (golden/RED/USE) sur services, endpoints, ressources
- Les dashboards Grafana (1416) + alertes (1417) sur ces signaux de base
- La règle : signaux de base d'abord, custom métier ensuite (351)

**Exemple de prompt** :
> « On a 200 métriques custom et on ne voit rien : applique 2027 — Golden Signals par service (latence/trafic/erreurs/saturation), RED par endpoint critique (POST /checkout), USE par ressource (CPU, disque eBPF 1731, réseau Hubble 1722) — dashboards 1416 + alertes 1417. »

**Cas d'usage** : Mise en place monitoring. S'articule avec skills 351 (SLI/SLO), 1416 (Grafana), 1282 (monitoring), 1731 (I/O eBPF), 1722 (Hubble).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
