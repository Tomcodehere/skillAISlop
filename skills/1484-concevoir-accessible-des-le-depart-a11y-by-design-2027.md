---
num: 1484
date_ajout: "2026-11"
nom: "Concevoir accessible des le depart (a11y by design, 2027)"
emoji: "♿"
domaine: "Produit"
signal: "Intégrer l'accessibilité dès la conception en 2027 (a11y by design, WCAG 2.2 niveau AA) : contraste 4,5:1, cibles tactiles 44 px, navigation clavier complète, lecteurs d'écran (NVDA/VoiceOver), textes alternatifs, pas de couleur seule. Utilise quand on conçoit une interface. N'utilise pas pour l'audit d'un existant (voir 1308/686)."
mot_cle: "accessibilité dès la conception WCAG 2.2 AA contraste clavier lecteur écran"
nom_court: "A11y by design"
branche: "D22"
synonymes: ["WCAG 2.2 niveau AA dès le design", "contraste 4,5:1 couleurs", "navigation clavier complète"]
cross_refs: [177, 686, 1308]
tags: ["2027"]
depends_on: [177]
---

## 1484. ♿ Concevoir accessible des le depart (a11y by design, 2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Concevoir accessible dès le départ en 2027 (WCAG 2.2 AA) : contraste 4,5:1, cibles 44 px, focus clavier visible, ordre de tabulation logique, textes alternatifs, formulaires avec labels et erreurs explicites.

**Quand l'utiliser (triggers)** :
- On conçoit une nouvelle interface, check a11y
- WCAG 2.2 AA : les règles clés en design
- Test au clavier + lecteur d'écran avant dev

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es designer accessibilité. Tu fournis la checklist design WCAG 2.2 AA (contraste, tailles, focus, sémantique HTML, labels, erreurs liées aux champs, pas de piège clavier) et tu rappelles : 1 milliard de personnes concernées, c'est aussi du SEO et de l'UX. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les maquettes (Figma) et composants
- Les personas incluant handicap (visuel, moteur, cognitif)
- Les lecteurs d'écran cibles (NVDA, VoiceOver, TalkBack)

**Méthode** :
1. Checklist design : contraste 4,5:1 texte / 3:1 gros texte, cibles 44x44 px, focus visible, pas de couleur seule.
2. Sémantique : vrai HTML (bouton, lien, h1-h6), landmarks, alt sur les images, aria si vraiment nécessaire.
3. Parcours clavier testé sur la maquette (tab order), pièges clavier exclus.
4. Formulaires : label associé, erreur liée au champ (aria-describedby), pas de placeholder seul.
5. Test réel : NVDA/VoiceOver sur le prototype + 1 test clavier complet avant dev.

**Sorties attendues** :
- La checklist a11y appliquée aux maquettes
- Les composants accessibles documentés (design system)
- Le test clavier + lecteur d'écran validé pré-dev

**Exemple de prompt** :
> « On redesign le dashboard : applique l'a11y by design (WCAG 2.2 AA : contraste, focus clavier, sémantique, labels) dès les maquettes Figma. »

**Cas d'usage** : Toute nouvelle interface, conformité (loi 2027 renforcée), UX universelle. S'articule avec skills 177 (accessibilité), 686 (audit a11y) et 1308 (audit web).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
