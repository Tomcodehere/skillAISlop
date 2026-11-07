---
num: 1723
date_ajout: "2026-11"
nom: "Falco : détection d'intrusion runtime (2027)"
emoji: "🛡"
domaine: "Sécurité"
signal: "Déployer Falco en 2027 (CNCF graduated, eBPF) pour détecter les intrusions en runtime : règles sur les syscalls (shell dans un conteneur, lecture de /etc/shadow, connexion sortante anormale, exécution de binaire non packagé), alertes temps réel vers SIEM (1453) / SOAR (1651), faux positifs gérés par règles custom. Mode eBPF (kernel 5.8+) préféré au module. N'utilise pas sans pipeline d'alertes (sinon bruit)."
mot_cle: "falco CNCF eBPF détection intrusion runtime syscalls 2027 shell conteneur /etc/shadow alertes SIEM SOAR kernel 5.8"
nom_court: "Falco"
branche: "D23"
synonymes: ["détecter un shell ouvert dans un conteneur (Falco, syscall execve)", "lire /etc/shadow depuis un pod = alerte immédiate (Falco)", "Falco eBPF (kernel 5.8+) plutôt que module kernel en prod"]
cross_refs: [1720, 1453, 1651]
tags: ["2027"]
depends_on: [1720]
---

## 1723. 🛡 Falco : détection d'intrusion runtime (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Déployer Falco en 2027 (CNCF, eBPF) pour la détection d'intrusion runtime : règles sur les syscalls (shell dans conteneur, lecture /etc/shadow, connexion sortante anormale, binaire non packagé), alertes temps réel vers SIEM (1453)/SOAR (1651), règles custom pour les faux positifs.

**Quand l'utiliser (triggers)** :
- un attaquant ouvre un shell dans un pod (Falco alerte en 1 s)
- lire /etc/shadow ou les secrets du cluster = alerte (règle Falco)
- Falco en eBPF (kernel 5.8+) pas en module kernel en prod

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es SOC / sécurité runtime. Tu installes Falco (DaemonSet, mode eBPF si kernel 5.8+, sinon module), tu charges les règles par défaut (falcosecurity), tu ajoutes des règles custom (métier), et tu branches les alertes sur le SIEM (1453) + SOAR (1651). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les nœuds (kernel 5.8+ pour eBPF, 1720)
- Les règles par défaut + custom
- Le SIEM/SOAR (1453/1651)

**Méthode** :
1. Installer Falco en DaemonSet (un agent par nœud), mode eBPF (kernel 5.8+, recommandé) ou module (noyaux anciens).
2. Règles par défaut (falcosecurity rules) : shell dans conteneur, lecture /etc/shadow, /proc, montage, exec de binaire hors image, connexions sortantes vers IP suspectes.
3. Règles custom : par namespace/app (ex. le pod 'paiement' ne doit jamais exécuter de shell → alerte critique).
4. Alertes : Falco → webhook/file → SIEM (1453), corrélation UEBA (1652), playbook SOAR (isoler le pod, 1651).
5. Faux positifs : ajuster les règles (exclusions par image/conteneur), mesurer le taux (< 5 %).
6. Métriques : MTTR détection (objectif sous 60 s), alertes/jour, faux positifs.

**Sorties attendues** :
- Falco déployé (eBPF) avec règles par défaut + custom actives
- Les alertes temps réel vers SIEM (1453) + playbook SOAR (isolation 1651)
- Le taux de faux positifs < 5 % et le MTTR détection mesuré

**Exemple de prompt** :
> « Détecte les intrusions runtime en 2027 : déploie Falco (eBPF, kernel 5.8+, DaemonSet), règles par défaut (shell conteneur, /etc/shadow, binaire hors image) + custom par app, alertes SIEM (1453) + SOAR (isolation pod 1651), faux positifs < 5 %. »

**Cas d'usage** : Sécurité runtime conteneurs/k8s. S'articule avec skills 1720 (eBPF), 1453 (SIEM), 1651 (SOAR) et 1652 (UEBA).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
