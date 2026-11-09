---
num: 1726
resume: "Déboguer le noyau Linux en live en 2027 avec bpftrace (eBPF 1720, langage type awk, lecture seule) : one-liners pour compter les syscalls par process, mesurer la latence I/O disque, tracer qui ouvre quels fichiers — sans redémarrer. Étape 1 : Installer bpftrace (apt/brew), vérifier bpftrace --info (kernel features OK)."
lang: "fr"
date_ajout: "2026-11"
nom: "bpftrace : debug ad-hoc du noyau Linux"
emoji: "🔎"
domaine: "Développement"
signal: "Déboguer le noyau Linux en live en 2027 avec bpftrace (langage de tracing haut niveau, style awk, sur eBPF 1720) : one-liners pour compter les syscalls, mesurer la latence des lectures disque, voir qui ouvre quels fichiers, les desched — sans redémarrer ni instrumenter. Utilise pour le debug ponctuel sur un serveur en prod (lecture seule). N'utilise pas pour du monitoring permanent (utiliser Pixie/Beyla 1724 ou Prometheus 1416)."
mot_cle: "bpftrace debug noyau linux live 2027 one-liner syscalls latence disque fichiers eBPF awk lecture seule"
nom_court: "bpftrace"
branche: "D1"
synonymes: ["compter les syscalls par process en 1 ligne (bpftrace)", "mesurer la latence des reads disque en live (bpftrace)", "qui ouvre /etc/passwd en ce moment ? (bpftrace)"]
cross_refs: [1720, 308, 1104]
tags: ["2027"]
depends_on: [1720]
---

## 1726. 🔎 bpftrace : debug ad-hoc du noyau Linux (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Déboguer le noyau Linux en live en 2027 avec bpftrace (eBPF 1720, langage type awk, lecture seule) : one-liners pour compter les syscalls par process, mesurer la latence I/O disque, tracer qui ouvre quels fichiers — sans redémarrer.

**Quand l'utiliser (triggers)** :
- quel process fait le plus de reads disque ? (bpftrace 1 ligne)
- latence des lectures disque p99 en live (bpftrace)
- bpftrace -e 'kprobe:do_sys_open { printf(...) }'

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es SRE / admin système. Tu installes bpftrace, tu écris des one-liners sûrs (lecture seule : tracepoints, kprobes read-only), tu les testes d'abord en staging, et tu ne laisses jamais tourner indéfiniment en prod (coût CPU). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le serveur Linux (kernel 5.8+, 1720)
- La question de debug ponctuelle
- bpftrace installé

**Méthode** :
1. Installer bpftrace (apt/brew), vérifier bpftrace --info (kernel features OK).
2. One-liners : bpftrace -e 'tracepoint:syscalls:sys_enter_read { @[comm] = count(); }' (top reads par process), latence disque : kprobe:vfs_read avec @lat histogram, qui ouvre quel fichier : tracepoint:syscalls:sys_enter_openat avec filename.
3. Limiter : toujours un timeout (timeout 30 bpftrace ...) et un filtre (pid, comm) pour ne pas surcharger le noyau en prod.
4. Lire les résultats : @maps (count, hist, avg) s'affichent à la fin (Ctrl-C).
5. Ne jamais écrire (pas de kprobe avec side-effect) : bpftrace en lecture seule. Permanent ? Non : passer à Pixie/Beyla (1724) ou Prometheus (1416).

**Sorties attendues** :
- Les one-liners bpftrace prêts (syscalls, latence I/O, fichiers ouverts)
- La preuve sur un cas réel en staging (résultat + overhead < 5 %)
- La règle : timeout + filtre + lecture seule, jamais permanent en prod

**Exemple de prompt** :
> « Le disque est lent mais on ne sait pas qui lit : bpftrace -e 'kprobe:vfs_read { @lat = hist(arg2); }' en live avec timeout 30 → top des tailles/latence de reads, overhead mesuré, sans redémarrer. »

**Cas d'usage** : Debug ponctuel Linux. S'articule avec skills 1720 (eBPF), 308 (profileur), 1104 (admin) et 1724 (Pixie).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
