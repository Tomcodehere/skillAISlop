---
num: 1730
date_ajout: "2026-11"
nom: "Katran : load balancer L4 eBPF de Meta (2027)"
emoji: "⚖️"
domaine: "Développement"
signal: "Utiliser Katran en 2027 (load balancer L4 open source basé sur eBPF/XDP, développé par Meta, gère des milliards de requêtes/jour chez eux) pour un load balancing ultra-performant (kernel bypass, pas de proxy userspace) : maglev consistent hashing, health checks actifs, DSR. Alternative cloud : les LB managés (AWS ALB/NLB 1612 edge). N'utilise pas pour du L7 (prendre un reverse proxy L7)."
mot_cle: "katran load balancer L4 eBPF XDP Meta 2027 maglev consistent hashing DSR milliards requêtes jour"
nom_court: "Katran"
branche: "D16"
synonymes: ["load balancer kernel bypass (XDP eBPF) : Katran (Meta) 2027", "maglev consistent hashing : même backend pour le même client", "Katran vs ALB/NLB cloud : L4 pur ultra-perf vs managé L7"]
cross_refs: [1720, 1612, 1203]
tags: ["2027"]
depends_on: [1720]
---

## 1730. ⚖️ Katran : load balancer L4 eBPF de Meta (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Déployer Katran en 2027 (load balancer L4 eBPF/XDP de Meta, milliards de requêtes/jour en prod chez Meta) : kernel bypass, maglev consistent hashing, health checks, DSR — pour du L4 ultra-perf ; garder un LB cloud/L7 pour le L7.

**Quand l'utiliser (triggers)** :
- notre LB userspace (nginx/haproxy) sature à 100k req/s
- XDP/eBPF : le trafic ne passe plus par la stack réseau classique
- maglev : le même client va toujours sur le même backend

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es ingénieur réseau perf. Tu déploies Katran (binaire C++ eBPF, config IPVS-like), maglev pour le consistent hashing, health checks actifs (TCP/HTTP), DSR pour éviter le retour par le LB. Tu benchmarks vs haproxy. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les serveurs de backend
- La VIP (IP virtuelle) exposée
- Les besoins (débit, latence, session persistence)

**Méthode** :
1. Installer Katran (build depuis GitHub ou package), configurer la VIP + les real servers (backend).
2. Maglev : consistent hashing (même client → même backend, utile pour le cache/stateful).
3. Health checks actifs (sonde TCP/HTTP periodique, retire du pool si KO).
4. DSR (Direct Server Return) : la réponse repart directement du backend au client (pas par le LB) → latence divisée.
5. Benchmark : req/s et latence p99 vs haproxy/nginx userspace (objectif x5-x10).
6. L7 (TLS termination, path routing) reste sur un reverse proxy L7 (nginx/envoy 1727) devant/derrière.

**Sorties attendues** :
- Katran déployé (VIP + backends + maglev + health checks + DSR)
- Le benchmark req/s et latence vs LB userspace (x5-x10)
- L'architecture L4 (Katran) + L7 (proxy) documentée

**Exemple de prompt** :
> « Notre haproxy sature à 100k req/s : déploie Katran (eBPF/XDP, Meta) en L4 (maglev, health checks, DSR), benchmark vs haproxy (objectif x5-10 req/s, latence p99 divisée), le L7 reste sur nginx. »

**Cas d'usage** : Haute perf réseau, datacenter. S'articule avec skills 1720 (eBPF), 1612 (edge), 1203 (réseau) et 1727 (mesh).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
