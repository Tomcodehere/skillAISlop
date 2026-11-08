---
num: 1496
date_ajout: "2026-11"
nom: "Thematisation produit : light, dark, high-contrast"
emoji: "🌓"
domaine: "Design"
signal: "Mettre en place la thématisation d'un produit en 2027 : thème clair/sombre (dark) via les design tokens sémantiques (pas de couleurs en dur), thème high-contrast (WCAG AAA 7:1) pour malvoyants, détection du réglage OS (prefers-color-scheme), persistance du choix utilisateur. Utilise quand on conçoit un design system (455). N'utilise pas pour un site vitrine one-page."
mot_cle: "dark mode light high-contrast thematisation design tokens sémantiques"
nom_court: "Thématisation"
branche: "D22"
synonymes: ["dark mode produit 2027", "high contrast WCAG AAA 7:1", "prefers-color-scheme détecter OS"]
cross_refs: [455, 149, 1484]
tags: ["2027"]
depends_on: [455]
---

## 1496. 🌓 Thematisation produit : light, dark, high-contrast (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Mettre en place la thématisation en 2027 : dark + light + high-contrast (7:1) via des design tokens sémantiques (surface/texte, jamais de couleurs en dur), détection prefers-color-scheme, persistance du choix utilisateur.

**Quand l'utiliser (triggers)** :
- Ajouter le dark mode à notre app
- Thème high-contrast pour malvoyants
- couleurs en dur partout, passer en tokens

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es design system engineer. Tu expliques les tokens sémantiques (--surface, --text, --primary, pas --blue-500 en dur), CSS variables + prefers-color-scheme, le high-contrast via forced-colors ou thème dédié (contraste 7:1), et le test des 3 thèmes sur les écrans clés. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le design system existant (tokens 455)
- Les écrans/component clés à vérifier
- Les 3 thèmes cibles (light/dark/high-contrast)

**Méthode** :
1. Définir les tokens sémantiques par thème (light/dark/high-contrast) en CSS variables.
2. Supprimer les couleurs en dur du code (remplacer par var(--surface) etc.).
3. Détecter le thème OS (prefers-color-scheme) + persistance du choix user (localStorage).
4. High-contrast : vérifier le ratio 7:1 (WCAG AAA) sur texte/focus/boutons.
5. Tester les 3 thèmes sur 10 écrans clés + lecteur d'écran (VoiceOver dark mode).

**Sorties attendues** :
- Les 3 thèmes opérationnels (tokens sémantiques)
- Le sélecteur de thème + détection OS
- Le test de contraste 7:1 validé

**Exemple de prompt** :
> « Notre app n'a que du light avec des couleurs en dur : mets en place la thématisation (tokens sémantiques, dark auto via prefers-color-scheme, high-contrast 7:1). »

**Cas d'usage** : Design system moderne, accessibilité, préférence utilisateur. S'articule avec skills 455 (tokens), 149 (palettes) et 1484 (a11y).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
