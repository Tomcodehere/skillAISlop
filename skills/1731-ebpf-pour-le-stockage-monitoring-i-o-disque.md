---
num: 1731
resume: "Surveiller les I/O disque au niveau noyau en 2027 avec eBPF (1720) : latence par type/device/process, top des fichiers lus, via bpftrace (1726) ou agent eBPF — quand iostat ne dit pas QUI et QUEL fichier. Étape 1 : One-liner bpftrace (1726) : latence des reads : kprobe:vfs_read / tracepoint:block:block_rq_issue avec hist(arg)."
date_ajout: "2026-11"
nom: "eBPF pour le stockage : monitoring I/O disque"
emoji: "💾"
domaine: "Développement"
signal: "Surveiller les I/O disque au niveau noyau en 2027 avec eBPF (1720) : latence par type d'I/O (read/write/sync), par device, par process (top consommateurs), files les plus lus — via bpftrace one-liners (1726) ou un agent eBPF dédié, sans instrumenter l'app. Utilise quand un serveur rame en I/O et que iostat ne suffit pas (qui, quel fichier, quelle latence). N'utilise pas pour le monitoring permanent (Prometheus 1416 + node_exporter)."
mot_cle: "eBPF monitoring I/O disque 2027 latence par device par process top fichiers lus bpftrace block layer"
nom_court: "eBPF I/O"
branche: "D1"
synonymes: ["qui fait les I/O disque et avec quelle latence ? (eBPF)", "latence des reads par device (nvme0 vs sda) en live (eBPF)", "fichiers les plus lus sur le serveur (eBPF, pas iostat)"]
cross_refs: [1720, 1726, 308]
tags: ["2027"]
depends_on: [1726]
---

## 1731. 💾 eBPF pour le stockage : monitoring I/O disque (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Surveiller les I/O disque au niveau noyau en 2027 avec eBPF (1720) : latence par type/device/process, top des fichiers lus, via bpftrace (1726) ou agent eBPF — quand iostat ne dit pas QUI et QUEL fichier.

**Quand l'utiliser (triggers)** :
- le serveur rame en I/O, iostat dit 100% mais pas qui
- latence p99 des reads par process en live (eBPF)
- top 10 des fichiers les plus lus ce matin (eBPF)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es SRE stockage. Tu traces la couche block (kprobes sur blk_account_io ou les tracepoints block:) avec bpftrace (1726) ou un agent eBPF, tu produis : latence par device, par process, top fichiers, et tu exportes vers Prometheus (1416) pour le permanent. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le serveur (kernel 5.8+, 1720)
- Les devices à surveiller
- Le besoin (latence, top conso, fichiers)

**Méthode** :
1. One-liner bpftrace (1726) : latence des reads : kprobe:vfs_read / tracepoint:block:block_rq_issue avec hist(arg).
2. Par process : @[comm] = hist(lat) → top des consommateurs d'I/O.
3. Par device : filtre sur dev (major:minor).
4. Fichiers les plus lus : tracepoint:syscalls:sys_enter_openat + count par filename, ou kprobe sur vfs_read avec le file struct.
5. Permanent : exporter ces métriques vers Prometheus (node exporter custom eBPF ou agent dédié) → Grafana (1416), alertes latence p99 (1417).
6. Corréler avec les métriques app (1416) : quel endpoint déclenche les I/O.

**Sorties attendues** :
- Les one-liners eBPF I/O (latence/device/process/top fichiers) prêts
- Le dashboard Grafana (1416) avec latence I/O p99 par device/process
- Les alertes (1417) sur latence I/O anormale

**Exemple de prompt** :
> « Le serveur rame en I/O mais iostat ne dit pas qui : bpftrace (eBPF 1720) en live — top des process par latence de read, top des fichiers ouverts, latence p99 par device — cause trouvée, puis alerte permanente sur Grafana (1416). »

**Cas d'usage** : Debug/perf stockage. S'articule avec skills 1720 (eBPF), 1726 (bpftrace), 308 (profileur), 1416 (Grafana).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
