---
num: 1900
date_ajout: "2026-11"
nom: "Bug bounty et VDP : recevoir et traiter les signalements de vulnérabilités"
emoji: "🐛"
domaine: "Sécurité"
signal: "Mettre en place un VDP (Vulnerability Disclosure Program — canal security@ + security.txt RFC 9116, réponse sous 5 j ouvrés, pas de poursuites pour les chercheurs de bonne foi) et éventuellement un bug bounty (HackerOne/Bugcrowd/YesWeHack — récompenses selon criticité SSVC 1826, périmètre défini, hors périmètre = pas de récompense). Triage : validation, criticité (CVSS/SSVC), correction (délai : critical 24 h, high 7 j), remerciement. CRA 2027 : VDP obligatoire pour les produits avec éléments numériques (1830). N'utilise pas de VDP sans capacité de réponse (sinon backlog de rapports non traités)."
mot_cle: "bug bounty VDP Vulnerability Disclosure Program security.txt RFC 9116 HackerOne Bugcrowd YesWeHack CRA 2027 triage CVSS SSVC délais correction 24h critical 7j high"
nom_court: "Bug bounty/VDP"
branche: "D23"
synonymes: ["VDP : security.txt (RFC 9116) + security@ + réponse sous 5 j, pas de poursuites (bonne foi)", "bug bounty HackerOne/Bugcrowd/YesWeHack : périmètre, récompenses selon SSVC 1826", "CRA 2027 : VDP obligatoire pour les produits numériques (1830)"]
cross_refs: [1830, 1826, 1897]
tags: ["2027"]
depends_on: [1830]
---

## 1900. 🐛 Bug bounty et VDP : recevoir et traiter les signalements de vulnérabilités

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Mettre en place un VDP (security.txt RFC 9116, security@, réponse < 5 j, safe harbor) + bug bounty (HackerOne/Bugcrowd/YesWeHack) si périmètre mature : triage SSVC (1826), correction (critical 24 h, high 7 j), CRA 2027 (1830).

**Quand l'utiliser (triggers)** :
- un chercheur signale une XSS : canal security.txt + réponse sous 5 j + safe harbor
- passer du VDP au bug bounty (récompenses) quand le VDP tourne bien
- triage : valider le rapport, criticité SSVC (1826), correctif sous 24 h si critical

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es RSSI / AppSec. Tu publies security.txt + security@, tu définis le safe harbor et le périmètre, tu tries les rapports (SSVC 1826), tu corriges selon les délais, et tu remercies (hall of fame optionnel). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le VDP (security.txt, canal) ou la plateforme de bounty
- Le processus de triage
- Les délais de correction (SSVC 1826)

**Méthode** :
1. VDP : security.txt à la racine (/.well-known/security.txt, RFC 9116), security@, PGP, politique safe harbor, délais de réponse (5 j).
2. Bug bounty : plateforme (HackerOne/Bugcrowd/YesWeHack), périmètre (in/out of scope), grille de récompenses par SSVC (1826).
3. Triage : validation (reproductible ?), criticité CVSS+SSVC, assignation, correction (critical 24 h, high 7 j, medium 30 j), re-test, paiement, remerciement.
4. CRA (1830) : VDP obligatoire — vérifier la conformité ; statistiques publiées (optionnel).

**Sorties attendues** :
- Le VDP publié (security.txt + canal + safe harbor)
- Le processus de triage/correction opérationnel (délais respectés)
- Les rapports traités et clôturés (métriques)

**Exemple de prompt** :
> « security.txt publié + un chercheur rapporte une IDOR (accès données autres users, high SVC 1826) -> accusé < 24 h, patch déployé en 5 j (canary 1418), re-test OK, récompense 500 € (bounty) ou remerciement (VDP), rapport clôturé, métrique publiée. »

**Cas d'usage** : Sécurité externe. S'articule avec skills 1830, 1826, 1897, 1859, 1453.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
