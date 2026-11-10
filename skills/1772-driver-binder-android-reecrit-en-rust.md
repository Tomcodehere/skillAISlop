---
num: 1772
resume: "Étudier le portage en Rust du driver Binder (IPC Android) comme cas d'école : architecture C/Rust hybride, objets pinés (1771), tests, et leçons pour tout portage ambitieux. Étape 1 : Lire le code : quelle part de Binder est en Rust en 2027 (nouveaux chemins) vs C (legacy)."
lang: "fr"
date_ajout: "2026-11"
nom: "Driver Binder (Android) réécrit en Rust"
emoji: "📱"
domaine: "Développement"
signal: "Le driver Binder d'Android (IPC entre processus, coeur du système) a ete porte en Rust dans le noyau (l'un des premiers drivers majeurs, livre via rust-for-linux). En 2027 il sert de référence : preuve qu'un driver critique et complexe peut vivre en Rust. Utilise pour étudier un portage Rust ambitieux. N'utilise pas pour supposer que tout le code C de Binder a disparu (coexistence C/Rust)."
mot_cle: "driver Binder Android porte en Rust IPC noyau reference portage 2027"
nom_court: "Binder en Rust"
branche: "D1"
synonymes: ["Binder IPC Android ecrit en Rust dans le noyau", "preuve qu'un driver critique peut passer en Rust", "coexistence C et Rust dans Binder, pas de remplacement total"]
cross_refs: [1770, 1771, 1776]
tags: ["2027"]
depends_on: [1770]
---

## 1772. 📱 Driver Binder (Android) réécrit en Rust

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Étudier le portage en Rust du driver Binder (IPC Android) comme cas d'école : architecture C/Rust hybride, objets pinés (1771), tests, et leçons pour tout portage ambitieux.

**Quand l'utiliser (triggers)** :
- porter un driver critique en Rust, par où commencer ?
- Binder en Rust : combien de code reste en C ?
- les objets IPC sont-ils pinés dans le noyau ?

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es développeur noyau Rust. Tu analyses l'architecture hybride de Binder (partie C legacy + partie Rust nouvelle), tu identifies les points d'ancrage (pinned-init 1771), et tu en tires un pattern réutilisable pour d'autres portages. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le tree rust-for-linux (branche binder)
- Les tests CTS Android (compatibilité)
- Le pattern pinned-init (1771)

**Méthode** :
1. Lire le code : quelle part de Binder est en Rust en 2027 (nouveaux chemins) vs C (legacy).
2. Identifier les structures partagées C/Rust et leur initialisation pinnee.
3. Verifier la compatibilité : tests CTS Android passent avec le driver Rust.
4. Extraire le pattern : nouveau code Rust, interfaces C stables, tests de non-régression.

**Sorties attendues** :
- La cartographie C/Rust de Binder
- Le pattern de portage réutilisable
- La preuve de compatibilité (tests CTS)

**Exemple de prompt** :
> « Portage d'un driver de capteur : suivre Binder — nouvelles ioctl en Rust, logique C legacy intacte (1776), objets IPC pinés (1771), tests de non-régression avant merge. »

**Cas d'usage** : Cas d'école du portage Rust. S'articule avec skills 1770, 1771, 1776.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
