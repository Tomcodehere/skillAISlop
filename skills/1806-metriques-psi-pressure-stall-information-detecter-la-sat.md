---
num: 1806
resume: "Exploiter les métriques PSI (Pressure Stall Information, GA 1.36) du kubelet pour détecter la saturation CPU/mémoire/IO d'un nœud avant OOMKill/throttle, et alerter (cpu some avg10 supérieur à 5 %). Étape 1 : Vérifier que le kubelet expose PSI (k8s 1.36+, feature gate on)."
lang: "fr"
date_ajout: "2026-11"
nom: "Métriques PSI (Pressure Stall Information) : détecter la saturation"
emoji: "📈"
domaine: "Data"
signal: "Lire les métriques PSI (Pressure Stall Information, GA dans k8s 1.36) exposées par le kubelet : quelque chose 'stall' quand une ressource manque (CPU, mémoire, IO) — some/avg10/total. Détecte la saturation AVANT le OOMKill ou le throttle CPU. Alertes : cpu some avg10 supérieur à 5 % sur 10 min = saturation. N'utilise pas pour remplacer les métriques applicatives (1753), c'est le niveau nœud."
mot_cle: "PSI Pressure Stall Information métriques kubelet saturation CPU mémoire IO some avg10 k8s 1.36 GA"
nom_court: "PSI metrics"
branche: "D17"
synonymes: ["pourquoi mes pods sont lents sans OOM : lire le PSI (pressure stall) du nœud", "cpu some avg10 supérieur à 5 % alerte saturation PSI", "PSI mémoire IO aussi, pas que le CPU"]
cross_refs: [1416, 1753, 1803]
tags: ["2027"]
depends_on: [1416]
---

## 1806. 📈 Métriques PSI (Pressure Stall Information) : détecter la saturation

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Exploiter les métriques PSI (Pressure Stall Information, GA 1.36) du kubelet pour détecter la saturation CPU/mémoire/IO d'un nœud avant OOMKill/throttle, et alerter (cpu some avg10 > 5 %).

**Quand l'utiliser (triggers)** :
- pods lents sur un nœud sans OOMKill : checker le PSI
- alerte PSI cpu some avg10 > 5 % sur 10 min
- PSI IO : disque saturé ralentit les pods

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es SRE. Tu scrapes les métriques PSI du kubelet (node-exporter ou kubelet /metrics/stats), tu alertes sur some avg10, et tu corrèles avec les limites des pods (throttle CPU = PSI cpu some élevé). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le kubelet 1.36+ expose PSI
- Prometheus scraping nœuds (1416)
- Les alertes PSI (1417/1761)

**Méthode** :
1. Vérifier que le kubelet expose PSI (k8s 1.36+, feature gate on).
2. Scraper node_pressure_* dans Prometheus (1416).
3. Alerter : node_pressure_cpu_waiting_seconds_total some avg10 > 5 % = saturation CPU.
4. Corréler : throttle CPU des pods (container_cpu_cfs_throttled) + PSI → augmenter limits ou resizer (1803).
5. PSI mémoire/IO : OOMKill imminent / disque lent.

**Sorties attendues** :
- Les dashboards PSI par nœud (cpu/mem/io)
- Les alertes PSI configurées (1761)
- Les actions : resize 1803 ou scale nœuds (1810)

**Exemple de prompt** :
> « Nœud gpu-worker-01 : PSI cpu some avg10 = 12 % alors qu'aucun pod n'est OOM — alerte, diagnostic : 3 pods batch throttlés (CFS), action : monter leurs limits ou ajouter un nœud (1810). »

**Cas d'usage** : Diagnostic saturation nœud. S'articule avec skills 1416, 1753, 1803, 1417/1761.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
