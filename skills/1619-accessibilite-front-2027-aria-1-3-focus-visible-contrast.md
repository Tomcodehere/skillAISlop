---
num: 1619
nom: "Accessibilite front 2027 : ARIA 1.3, focus-visible, contraste auto (2027)"
emoji: "♿"
domaine: "Design"
signal: "Rendre un front accessible en 2027 (WCAG 2.2 AA + au-delà) : ARIA 1.3 (attributs nouveaux), :focus-visible (focus clavier uniquement, pas au clic), contraste automatique (prefers-contrast: more), réduction de mouvement forcée (1495), lecteurs d'écran testés (NVDA/VoiceOver). Utilise sur tout nouveau composant. N'utilise pas pour l'audit d'un existant (1308/686)."
mot_cle: "accessibilité front 2027 ARIA 1.3 focus-visible prefers-contrast WCAG 2.2"
nom_court: "A11y front"
branche: "D22"
synonymes: ["focus clavier visible uniquement :focus-visible", "contraste automatique prefers-contrast more", "ARIA 1.3 nouveaux attributs 2027"]
cross_refs: [1484, 1495, 1308]
tags: ["2027"]
depends_on: [1484]
---

## 1619. ♿ Accessibilite front 2027 : ARIA 1.3, focus-visible, contraste auto (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Rendre un front accessible en 2027 (WCAG 2.2 AA+) : :focus-visible (focus clavier, pas clic), prefers-contrast:more (contraste renforcé auto), ARIA 1.3, réduction de mouvement (1495), tests NVDA/VoiceOver sur chaque composant.

**Quand l'utiliser (triggers)** :
- le focus apparaît aussi au clic souris, gênant
- :focus-visible uniquement au clavier
- prefers-contrast more pour malvoyants

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es dev front a11y. Tu appliques : :focus-visible pour l'anneau de focus (pas :focus), media prefers-contrast:more (contraste 7:1), prefers-reduced-motion (1495), ARIA 1.3 (aria-description, etc.), et tu testes au clavier + NVDA/VoiceOver. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les composants du design system
- Les lecteurs d'écran cibles (NVDA, VoiceOver, TalkBack)
- Les préférences OS (contraste, mouvement)

**Méthode** :
1. Focus : remplacer :focus par :focus-visible (anneau clavier seul), outline clair (2-3 px, offset).
2. Contraste : @media (prefers-contrast: more) → ratio 7:1 (AAA) sur textes/boutons.
3. Mouvement : @media (prefers-reduced-motion: reduce) → désactiver (1495).
4. ARIA 1.3 : aria-description, attributs de drag, etc. ; jamais d'ARIA si HTML sémantique suffit.
5. Tests : clavier seul (tab complet), NVDA (formes, tableaux, modales avec focus trap), VoiceOver mobile.

**Sorties attendues** :
- Le design system a11y 2027 (:focus-visible, prefers-contrast, ARIA 1.3)
- Les tests clavier + lecteur d'écran documentés
- Le contraste 7:1 en mode high-contrast validé

**Exemple de prompt** :
> « Notre design system a un focus au clic souris et un contraste 4,5:1 fixe : passe en :focus-visible, ajoute prefers-contrast:more (7:1), ARIA 1.3 sur les composants custom, tests NVDA/VoiceOver. »

**Cas d'usage** : Tout front moderne, conformité EAA 2027. S'articule avec skills 1484 (a11y design), 1495 (animations) et 1308 (audit).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
