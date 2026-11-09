---
num: 1725
resume: "Faire du security enforcement runtime en 2027 avec Tetragon (Cilium/eBPF) : Tracing Policies (YAML) qui bloquent en temps réel l'exécution de binaires interdits, l'écriture sur des fichiers sensibles, les connexions sortantes non autorisées — au-delà de la détection (Falco 1723). Étape 1 : Installer Tetragon (daemonset eBPF, avec Cilium ou standalone), vérifier tetragon status."
lang: "fr"
date_ajout: "2026-11"
nom: "Tetragon : sécurité runtime avec enforcement"
emoji: "🛡"
domaine: "Sécurité"
signal: "Aller plus loin que la détection avec Tetragon (Cilium, eBPF) en 2027 : au-delà d'alerter (Falco 1723), Tetragon peut ENFORcer (bloquer) en temps réel : empêcher l'exécution d'un binaire, le write sur un fichier sensible, une connexion sortante — via des Tracing Policies (YAML). Utilise pour les conteneurs critiques (paiement). N'utilise pas sans tests (risque de bloquer le légitime)."
mot_cle: "tetragon cilium eBPF enforcement policies blocage runtime 2027 TracingPolicy exec write network kill"
nom_court: "Tetragon"
branche: "D23"
synonymes: ["bloquer (pas juste alerter) un binaire dans un conteneur (Tetragon)", "TracingPolicy : interdire l'exec de /tmp/x, le write sur /etc, la connexion vers IP externe", "Tetragon (Cilium) vs Falco (1723) : enforce vs detect"]
cross_refs: [1721, 1723, 1705]
tags: ["2027"]
depends_on: [1723]
---

## 1725. 🛡 Tetragon : sécurité runtime avec enforcement (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Faire du security enforcement runtime en 2027 avec Tetragon (Cilium/eBPF) : Tracing Policies (YAML) qui bloquent en temps réel l'exécution de binaires interdits, l'écriture sur des fichiers sensibles, les connexions sortantes non autorisées — au-delà de la détection (Falco 1723).

**Quand l'utiliser (triggers)** :
- bloquer (pas juste logger) l'exec de /tmp/xyz dans le pod paiement
- interdire toute connexion sortante depuis le conteneur BDD
- Tetragon TracingPolicy : action Kill / Error / Log

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es sécurité runtime k8s. Tu installes Tetragon (avec Cilium 1721), tu écris des TracingPolicy (kprobes sur execve/openat/connect avec filtres pod/namespace + action: Log/Error/Kill/Signal), tu testes en mode Log d'abord, puis enforce. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Cilium/Tetragon déployé (1721)
- Les conteneurs critiques à protéger
- Les règles d'enforcement

**Méthode** :
1. Installer Tetragon (daemonset eBPF, avec Cilium ou standalone), vérifier tetragon status.
2. TracingPolicy exemple : bloquer execve hors des binaires packagés dans l'image (whitelist par digest 1457) → action Error (retourne erreur) ou Kill (tue le process).
3. Bloquer les writes sur /etc, /root, les secrets montés ; bloquer les connexions sortantes sauf allowlist (egress).
4. Modes : Log (audit) → Error (bloque, loggue) → Kill (tue le process, alerte critique 1417).
5. Tester en Log 1 semaine (faux positifs), puis Error/Enforce sur les conteneurs critiques uniquement.
6. Alertes : chaque blocage → SIEM (1453) + SOAR (1651) ; métriques de blocages/jour.

**Sorties attendues** :
- Tetragon déployé avec TracingPolicies (exec/write/egress) en mode enforce
- Le test Log→Enforce documenté (faux positifs < 5 %)
- Les blocages alertés vers SIEM (1453) + SOAR (1651)

**Exemple de prompt** :
> « Le conteneur 'paiement' ne doit jamais exécuter de shell ni sortir sur Internet : Tetragon (Cilium 1721) TracingPolicy = bloquer execve hors image signée (1457) + egress deny-all sauf API banque — testé en Log 1 semaine puis enforce, alertes SIEM (1453). »

**Cas d'usage** : Sécurité runtime renforcée. S'articule avec skills 1721 (Cilium), 1723 (Falco), 1705 (Kyverno) et 1453 (SIEM).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
