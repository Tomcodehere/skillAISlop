---
num: 1720
date_ajout: "2026-11"
nom: "eBPF : programmer le noyau Linux sans le modifier"
emoji: "⚡"
domaine: "Développement"
signal: "Comprendre et utiliser eBPF en 2027 (devenu standard en 2026, utilisé par Meta/Google/Netflix/Cloudflare/Microsoft/Apple) : exécuter des programmes sandboxés dans le noyau Linux (networking, observabilité, sécurité) sans modifier le kernel ni charger de modules. Outils haut niveau : Cilium (1721), Falco (1723), bpftrace, Pixie/Beyla (1724). Prérequis : kernel 5.8+ (idéal 5.15+). N'utilise pas pour de la logique applicative (reste en userspace)."
mot_cle: "eBPF 2027 programmer noyau linux sandboxé sans modifier kernel Cilium Falco bpftrace Pixie Beyla kernel 5.8+"
nom_court: "eBPF"
branche: "D1"
synonymes: ["exécuter du code dans le noyau Linux sans le recompiler (eBPF)", "eBPF standard en 2026 : Meta Google Netflix Cloudflare l'utilisent", "kernel 5.8 minimum 5.15+ idéal pour eBPF (uname -r)"]
cross_refs: [1178, 1104, 1721]
tags: ["2027"]
depends_on: [1178]
---

## 1720. ⚡ eBPF : programmer le noyau Linux sans le modifier (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Comprendre eBPF en 2027 (standard 2026) : programmes sandboxés dans le noyau Linux (networking, observabilité, sécurité) sans toucher au kernel — via les outils haut niveau (Cilium 1721, Falco 1723, bpftrace, Pixie 1724) plutôt qu'en écrivant du eBPF brut.

**Quand l'utiliser (triggers)** :
- on veut observer les syscalls sans agent lourd (eBPF)
- eBPF : programmes vérifiés (verifier) exécutés dans le noyau en sandbox
- kernel 5.8+ requis, vérifier avec uname -r

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es ingénieur système cloud-native. Tu expliques le principe (verifier → exécution sandboxée dans le noyau, maps pour partager les données avec l'userspace), et tu diriges vers les outils haut niveau (Cilium, Falco, bpftrace, Pixie/Beyla) plutôt que l'écriture de programmes eBPF bruts (réservée aux experts). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le serveur/cluster Linux (kernel 5.8+)
- Le besoin (networking, sécurité, observabilité)
- Les outils eBPF choisis

**Méthode** :
1. Vérifier le kernel : uname -r (5.8+ min, 5.15+ recommandé) ; sinon module kernel (moins recommandé en prod).
2. Cas d'usage : networking (Cilium 1721), sécurité runtime (Falco 1723, Tetragon 1725), observabilité zero-instrumentation (Pixie/Beyla 1724), debug ad-hoc (bpftrace 1726).
3. Principe : le programme eBPF est vérifié (pas de boucle infinie, pas d'accès mémoire arbitraire) puis exécuté dans le noyau ; les données remontent via des maps (perf events, ring buffer).
4. Ne pas écrire d'eBPF brut sauf besoin très spécifique : utiliser les outils matures (Cilium/Falco/Pixie/Beyla).
5. Mesurer l'overhead (généralement sous 1-5 % CPU) et la latence ajoutée.

**Sorties attendues** :
- La compréhension d'eBPF + le kernel vérifié (5.8+)
- Les outils eBPF choisis selon le besoin (réseau/sécu/obs)
- Le benchmark d'overhead (moins de 5 % de CPU)

**Exemple de prompt** :
> « On veut voir tous les syscalls des conteneurs sans agent lourd ni sidecar : vérifie le kernel (5.15+), déploie Pixie ou Beyla (observabilité eBPF zero-instrumentation 1724), overhead mesuré sous 5 % CPU. »

**Cas d'usage** : Cloud-native, k8s, sécurité runtime, observabilité. S'articule avec skills 1178 (Linux hardening), 1104 (admin Linux), 1721 (Cilium).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
