---
num: 1770
date_ajout: "2026-11"
nom: "Rust dans le noyau Linux : bilan et trajectorie"
emoji: "🧀"
domaine: "Développement"
signal: "Faire le bilan en 2027 de Rust for Linux : le flag 'plus experimental' a ete retire en decembre 2025 (kernel 6.8+), la branche rust-for-linux (Ojeda) a livre ses premiers drivers. Au kernel 7.3 : 496 fichiers Rust, 120 019 SLOC, soit 24,6x le volume du 6.1. Utilise pour decider si un nouveau driver se ecrit en Rust. N'utilise pas pour réécrire tout le noyau en Rust (ajout, pas remplacement)."
mot_cle: "Rust for Linux noyau 2027 bilan plus experimental 496 fichiers 120 000 SLOC kernel 7.3"
nom_court: "Rust in Linux"
branche: "D1"
synonymes: ["Rust n'est plus experimental dans le noyau depuis decembre 2025", "496 fichiers 120 019 SLOC de Rust dans le kernel 7.3 (24,6x vs 6.1)", "premiers drivers Rust livres depuis 6.8 : Binder, NVMe, Asahi, Nova"]
cross_refs: [1776, 1777, 1778]
tags: ["2027"]
depends_on: [1772]
---

## 1770. 🧀 Rust dans le noyau Linux en 2027 : bilan et trajectorie

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Situer Rust dans le noyau Linux en 2027 : plus experimental depuis dec. 2025, 496 fichiers / 120 019 SLOC au kernel 7.3 (x24,6 vs 6.1), premiers drivers livrees (Binder, NVMe, Asahi, Nova), avec la doctrine Torvalds : un ajout, pas un remplacement.

**Quand l'utiliser (triggers)** :
- peut-on ecrire un nouveau driver en Rust en 2027 ?
- Rust est-il encore experimental dans le noyau ?
- combien de code Rust dans le kernel 7.3 ?

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es développeur noyau / contributeur Linux. Tu presentes l'etat factuel 2027 (chiffres par version, drivers livres), la gouvernance (tree rust-for-linux 1777) et la limite : Rust progresse par ajouts de nouveaux drivers, jamais par réécriture du C existant. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La version du noyau cible (6.8+ pour Rust stable)
- Le type de driver (Binder/NVMe/Asahi/Nova ont des pionniers)
- Le guide de contribution kernel

**Méthode** :
1. Verifier la version du noyau : flag experimental retire en dec. 2025, Rust utilisable pour les nouveaux drivers depuis 6.8.
2. Consulter rusted-kernel.com : courbe SLOC par version (6.1 -> 7.3 : 120 019 SLOC, x24,6).
3. Lister les drivers pionniers : Binder (1772), NVMe (1773), Asahi (1774), Nova (1775).
4. Appliquer la doctrine 1776 : nouveau code en Rust quand pertinent, C existant intact.

**Sorties attendues** :
- Le bilan chiffre 2027 (fichiers, SLOC, drivers)
- La decision : nouveau driver en Rust oui/non avec justification
- Le lien vers le tree rust-for-linux et sa gouvernance (1777)

**Exemple de prompt** :
> « Nouveau driver de stockage en 2027 sur kernel 7.3 : oui, ecrit en Rust (NVMe pionnier 1773, pinned-init 1771), le C existant n'est pas touche (doctrine 1776), contribution via le tree rust-for-linux (1777). »

**Cas d'usage** : Décider pour un nouveau driver. S'articule avec skills 1776 (doctrine), 1777 (gouvernance), 1778 (sécurité mémoire).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
