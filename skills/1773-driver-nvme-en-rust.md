---
num: 1773
resume: "Évaluer le driver NVMe en Rust comme preuve de faisabilité du Rust sur un chemin I/O critique (latence SSD), avec les garanties : pas de GC, allocations contrôlées, objets pinés. Étape 1 : Confirmer le driver NVMe Rust livre et teste (rust-for-linux)."
lang: "fr"
date_ajout: "2026-11"
nom: "Driver NVMe en Rust"
emoji: "💾"
domaine: "Développement"
signal: "Un driver NVMe (SSD) a ete porte en Rust dans le noyau via rust-for-linux : preuve de faisabilité sur un driver de stockage haute performance. En 2027, reference pour les nouveaux drivers de stockage. Utilise pour évaluer Rust sur un chemin I/O critique (latence, pas de GC, pas d'allocateur au mauvais moment)."
mot_cle: "driver NVMe SSD en Rust noyau stockage haute performance latence 2027"
nom_court: "NVMe en Rust"
branche: "D1"
synonymes: ["driver NVMe porte en Rust preuve de faisabilite stockage", "Rust sur le chemin I/O critique : pas d'allocation surprise", "nouveau driver SSD en Rust en 2027 sur kernel 7.x"]
cross_refs: [1770, 1771, 1731]
tags: ["2027"]
depends_on: [1770]
---

## 1773. 💾 Driver NVMe en Rust

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Évaluer le driver NVMe en Rust comme preuve de faisabilité du Rust sur un chemin I/O critique (latence SSD), avec les garanties : pas de GC, allocations contrôlées, objets pinés.

**Quand l'utiliser (triggers)** :
- nouveau driver SSD : Rust acceptable sur le chemin I/O ?
- latence NVMe : le Rust ajoute-t-il de la latence ?
- les allocations dans le driver NVMe Rust sont-elles bornees ?

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es développeur noyau Rust / stockage. Tu cites le portage NVMe comme preuve, tu exiges un profil d'allocation (pas d'alloc dans la fast path, preallocation), et tu benchmarkes latence p99 Rust vs C. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le driver NVMe Rust du tree
- Le benchmark latence (fio)
- Les regles d'allocation du noyau (GFP_ATOMIC en IRQ, etc.)

**Méthode** :
1. Confirmer le driver NVMe Rust livre et teste (rust-for-linux).
2. Auditer les allocations : fast path sans alloc (buffers prealloues), GFP conforme au contexte (IRQ/process).
3. Benchmark : latence p99 Rust vs C sur la meme cible, ecart < 5 %.
4. Decider : nouveau driver stockage en Rust si le profil d'allocation est maîtrisé.

**Sorties attendues** :
- La preuve de faisabilite NVMe Rust
- Le profil d'allocation audite (fast path zero-alloc)
- Le benchmark latence p99 comparatif

**Exemple de prompt** :
> « Nouveau driver SSD NVMe en 2027 : ecrit en Rust en suivant le portage pionnier, buffers prealloues a l'init, zero allocation dans la completion path, fio montre p99 identique au C. »

**Cas d'usage** : Stockage haute perf en Rust. S'articule avec skills 1770, 1771, 1731 (I/O eBPF).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
