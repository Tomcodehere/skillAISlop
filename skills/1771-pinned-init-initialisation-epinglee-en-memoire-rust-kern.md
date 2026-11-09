---
num: 1771
resume: "Utiliser pinned-init (depuis kernel 6.4) pour garantir qu'un objet Rust initialisé garde une adresse fixe (Pin), obligatoire dès qu'il est embarqué dans une structure C à pointeurs intrusifs. Étape 1 : Identifier les objets Rust embarqués dans des structures C (listes, arbres, callbacks)."
date_ajout: "2026-11"
nom: "pinned-init : initialisation épinglée en mémoire (Rust kernel)"
emoji: "📌"
domaine: "Développement"
signal: "Comprendre pinned-init en 2027 : l'API Rust du noyau qui garantit qu'un objet initialise reste a une adresse fixe en mémoire (Pin), indispensable pour les pointeurs intrusifs (listes chainees, arbres) utilises par le noyau C. Disponible depuis le kernel 6.4. Utilise pour tout objet Rust embarque dans une structure C. N'utilise pas pour du code purement Rust userland."
mot_cle: "pinned-init Pin adresse fixe mémoire kernel Rust 6.4 pointeurs intrusifs listes chainees 2027"
nom_court: "pinned-init"
branche: "D1"
synonymes: ["garantir qu'un objet Rust ne bouge pas en memoire (Pin) dans le noyau", "pourquoi les pointeurs intrusifs du noyau exigent pinned-init", "API pinned-init disponible depuis le kernel 6.4"]
cross_refs: [1770, 1772, 1776]
tags: ["2027"]
depends_on: [1770]
---

## 1771. 📌 pinned-init : initialisation épinglée en mémoire (Rust kernel)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Utiliser pinned-init (depuis kernel 6.4) pour garantir qu'un objet Rust initialisé garde une adresse fixe (Pin), obligatoire dès qu'il est embarqué dans une structure C à pointeurs intrusifs.

**Quand l'utiliser (triggers)** :
- mon objet Rust est embarque dans une struct C avec list_head
- le compilateur refuse : cannot move out of pinned field
- kernel 6.4+ : pinned-init disponible pour les nouveaux drivers

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es développeur noyau Rust. Tu declares les objets embarqués en struct avec Pin, tu utilises pinned_init! pour l'initialisation in-place, et tu ne déplaces jamais un objet pinne (self-referential). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La struct C hote (ex. list_head, device)
- Le kernel 6.4+
- La crate pinned-init du tree rust-for-linux

**Méthode** :
1. Identifier les objets Rust embarqués dans des structures C (listes, arbres, callbacks).
2. Declarer le champ comme Pin<&mut Self> ou utiliser pinned_init! pour construire in-place.
3. Ne jamais déplacer l'objet après initialisation (le borrow checker + Pin l'imposent).
4. Tester : build du module, load/unload du driver, pas de move detecte.

**Sorties attendues** :
- Le driver compile avec objets pinés correctement
- Aucun move d'objet pinne (erreur de compilation sinon)
- La note : pinned-init requis des que struct C hote

**Exemple de prompt** :
> « Driver Binder (1772) : chaque transaction embarque un objet Rust dans une struct C avec list_head — initialisation via pinned_init!, champ declare Pin, le noyau C peut chainee l'objet en sécurité. »

**Cas d'usage** : Base de tout driver Rust embarqué. S'articule avec skills 1770 (bilan), 1772 (Binder).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
