---
num: 1777
date_ajout: "2026-11"
nom: "Gouvernance du tree rust-for-linux et contribution"
emoji: "🏛️"
domaine: "Gestion"
signal: "Contribuer au Rust du noyau Linux en 2027 passe par le tree rust-for-linux maintenu par Miguel Ojeda : branches par sous-systeme, revues sur la mailing list rust-for-linux, intégration par Linus Torvalds. Processus : RFC si design nouveau, patchs petits et testés (KUnit), clippy + fmt obligatoires. N'utilise pas pour contribuer directement au tree principal sans passer par rust-for-linux."
mot_cle: "tree rust-for-linux Ojeda contribution mailing list RFC KUnit clippy fmt pull request 2027"
nom_court: "Contribuer Rust kernel"
branche: "D25"
synonymes: ["comment contribuer au Rust du noyau : tree rust-for-linux d'Ojeda", "RFC sur rust-for-linux avant tout design nouveau", "patchs petits testes KUnit + clippy + rustfmt obligatoires"]
cross_refs: [1770, 1776, 82]
tags: ["2027"]
depends_on: [1770]
---

## 1777. 🏛️ Gouvernance du tree rust-for-linux et contribution (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Contribuer au code Rust du noyau en 2027 via le tree rust-for-linux (Ojeda) : RFC pour les nouveaux designs, patchs petits et testés (KUnit), clippy/fmt, revue sur la mailing list.

**Quand l'utiliser (triggers)** :
- mon premier patch Rust pour le noyau, quelle procedure ?
- design nouveau : RFC obligatoire avant code
- quels checks CI : KUnit, clippy, rustfmt, KUnit kunit_tool ?

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es contributeur noyau Linux. Tu suis le processus rust-for-linux : branche par sous-système, RFC pour le design, patchs atomiques avec tests KUnit, passage clippy -D warnings et rustfmt, envoi sur la mailing list avec cover letter. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le tree rust-for-linux (clone, branches)
- La mailing list rust-for-linux
- Les outils : KUnit, clippy, rustfmt

**Méthode** :
1. Cloner rust-for-linux, choisir la branche du sous-système concerne (ex. binder, gpu).
2. Si design nouveau : ecrire la RFC sur la mailing list et attendre les retours avant de coder.
3. Coder en patchs petits (1 commit = 1 changement), chaque patch avec tests KUnit.
4. Passer clippy -- -D warnings et rustfmt, puis envoyer la serie (git send-email) avec cover letter sur la ML.

**Sorties attendues** :
- La RFC validee (si design nouveau)
- La serie de patchs conforme (KUnit + clippy + fmt)
- L'envoi sur la mailing list avec cover letter

**Exemple de prompt** :
> « Premier patch : ajout d'un helper Rust pour le driver Binder (1772) — RFC courte sur rust-for-linux, 1 patch de 40 lignes avec 3 tests KUnit, clippy/fmt OK, envoye avec git send-email, revue par Ojeda. »

**Cas d'usage** : Contribuer proprement. S'articule avec skills 1770, 1776, 82 (DevOps/git).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
