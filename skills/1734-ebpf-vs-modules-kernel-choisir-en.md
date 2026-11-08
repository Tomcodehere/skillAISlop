---
num: 1734
date_ajout: "2026-11"
nom: "eBPF vs modules kernel : choisir en"
emoji: "⚖️"
domaine: "Développement"
signal: "Choisir en 2027 entre eBPF (1720) et les modules kernel traditionnels : eBPF = sandboxé, vérifié (pas de crash noyau), dynamique (charge/décharge à chaud), idéal pour observabilité/sécurité/réseau moderne ; module kernel = accès total, perf max, mais un bug = panic noyau, nécessite rebuild/reboot, review LKML difficile. Règle : eBPF par défaut ; module seulement pour ce qu'eBPF ne peut pas faire (nouveau driver, subsystem). N'utilise pas de module pour du monitoring."
mot_cle: "eBPF vs module kernel choisir 2027 sandboxé vérifié dynamique vs accès total perf panic noyau LKML"
nom_court: "eBPF vs module"
branche: "D1"
synonymes: ["pourquoi eBPF plutôt qu'un module kernel en 2027 (pas de panic)", "module kernel = un bug = kernel panic (risque)", "eBPF par défaut, module seulement pour les drivers/subsystems"]
cross_refs: [1720, 1178, 1770]
tags: ["2027"]
depends_on: [1720]
---

## 1734. ⚖️ eBPF vs modules kernel : choisir en 2027 (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Choisir en 2027 entre eBPF (1720) et les modules kernel : eBPF (sandboxé, vérifié, dynamique, pas de panic) par défaut pour observabilité/sécurité/réseau ; module kernel réservé aux drivers/subsystems (accès total mais risque de panic + review LKML).

**Quand l'utiliser (triggers)** :
- un module kernel a fait paniquer le serveur en prod
- eBPF : programme vérifié, charge à chaud, pas de reboot
- quand écrire un vrai module kernel en 2027 ? (driver, subsystem)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte système. Tu compares : eBPF (verifier = sécurité, chargement dynamique sans reboot, perf ~native) vs module (accès mémoire total, mais sign-off LKML, risque panic, déploiement lourd). Règle : eBPF par défaut, module pour driver/subsystem uniquement. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le besoin (monitoring, réseau, driver, subsystem)
- Le kernel cible et sa politique de modules signés
- Les compétences de l'équipe

**Méthode** :
1. eBPF par défaut pour : observabilité (Pixie/Beyla 1724), sécurité runtime (Falco/Tetragon 1723/1725), réseau (Cilium 1721), debug (bpftrace 1726). Avantages : vérifié (pas de boucle infinie/crash), dynamique (bpftool, pas de reboot), overhead faible.
2. Module kernel uniquement pour : nouveau driver matériel, nouveau filesystem, nouveau subsystem — là où eBPF ne peut pas (accès matériel bas niveau). Inconvénients : un bug = kernel panic, build du noyau, sign-off LKML, déploiement (dkms/reboot).
3. Politiques : Secure Boot + signature de modules (kernel lockdown), revue de code stricte, tests en VM avant prod.
4. Ne jamais charger de module non signé en prod (politique noyau).
5. Décision documentée par besoin (ADR 88).

**Sorties attendues** :
- La matrice de décision eBPF vs module (critères + exemples)
- La règle 'eBPF par défaut, module pour driver/subsystem' écrite
- La politique de modules signés (Secure Boot) en place

**Exemple de prompt** :
> « Un module custom a paniqué le serveur en prod : règle 2027 — eBPF (1720, vérifié, sans reboot) par défaut pour monitoring/réseau/sécurité (1721/1723/1724/1726), module kernel uniquement pour driver/subsystem (avec Secure Boot + modules signés + revue LKML). »

**Cas d'usage** : Architecture système. S'articule avec skills 1720 (eBPF), 1178 (hardening), 1770 (Rust kernel) et 88 (ADR).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
