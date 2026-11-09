---
num: 1620
resume: "Industrialiser les design tokens en 2027 : JSON unique (Style Dictionary / Tokens Studio) générant CSS variables, Tailwind, Swift, Kotlin — une seule source de vérité pour web + iOS + Android. Étape 1 : Modéliser en 3 niveaux : primitifs (blue-500), sémantiques (--color-primary, --surface), composants (bouton primaire)."
lang: "fr"
date_ajout: "2026-11"
nom: "Design tokens multi-plateformes : Style Dictionary, Tokens Studio"
emoji: "🎨"
domaine: "Design"
signal: "Industrialiser les design tokens en 2027 : tokens en JSON (Style Dictionary) ou Figma Tokens Studio, générés en CSS variables, Swift (iOS), Kotlin (Android), Tailwind config — une seule source, toutes les plateformes. Utilise pour un design system multi-plateforme. N'utilise pas pour un one-page."
mot_cle: "design tokens multi-plateformes style dictionary tokens studio JSON CSS Swift Kotlin 2027"
nom_court: "Design tokens"
branche: "D22"
synonymes: ["une source de tokens pour web iOS Android", "style dictionary génère CSS Swift Kotlin", "tokens studio synchronisé avec Figma"]
cross_refs: [455, 732, 1496]
tags: ["2027"]
depends_on: [455]
---

## 1620. 🎨 Design tokens multi-plateformes : Style Dictionary, Tokens Studio (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Industrialiser les design tokens en 2027 : JSON unique (Style Dictionary / Tokens Studio) générant CSS variables, Tailwind, Swift, Kotlin — une seule source de vérité pour web + iOS + Android.

**Quand l'utiliser (triggers)** :
- nos couleurs sont dupliquées dans Figma, le CSS, iOS, Android
- style dictionary : tokens JSON → CSS Swift Kotlin
- tokens studio plugin Figma synchro 2027

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es design system engineer. Tu définis la pyramide : tokens primitifs (couleur 500) → sémantiques (surface, text) → composants, exportés par Style Dictionary vers toutes les plateformes, avec CI qui vérifie que tout est généré (pas d'édition manuelle). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le Figma existant (Tokens Studio) ou un JSON de départ
- Les plateformes cibles (web, iOS, Android)
- Les catégories (couleur, espacement, typo, radius, ombre)

**Méthode** :
1. Modéliser en 3 niveaux : primitifs (blue-500), sémantiques (--color-primary, --surface), composants (bouton primaire).
2. Exporter via Tokens Studio (Figma) ou écrire le JSON, versionné dans Git.
3. Style Dictionary : config par plateforme (css/variables, swift, kotlin, tailwind), build dans la CI.
4. Consommer : web en var(--…), iOS/UIColor, Android Compose — jamais de valeur en dur.
5. CI : fail si un fichier généré est modifié à la main ou si un token manque.

**Sorties attendues** :
- La source de tokens unique (JSON/Figma) versionnée
- Les sorties générées (CSS, Swift, Kotlin, Tailwind) en CI
- La règle « jamais de valeur en dur » appliquée

**Exemple de prompt** :
> « Nos couleurs sont en dur dans Figma + CSS + iOS + Android (4 endroits, déjà divergé) : mets des design tokens (Tokens Studio → JSON → Style Dictionary → CSS/Swift/Kotlin/Tailwind), CI qui bloque les modifs manuelles. »

**Cas d'usage** : Design systems multi-plateformes. S'articule avec skills 455 (tokens), 732 (design system) et 1496 (thématisation).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
