---
num: 1485
resume: "Préparer un produit au multilingue en 2027 : i18n (clés de traduction externalisées, gestion pluriels/genre, formats date/nombre/devise par locale, support RTL) puis l10n (traductions humaines avec contexte). Étape 1 : i18n : externaliser toutes les chaînes (clés, pas de texte en dur), utiliser ICU MessageFormat (pluriels/genre)."
date_ajout: "2026-11"
nom: "Preparer son produit au multilingue (i18n/l10n)"
emoji: "🌐"
domaine: "Produit"
signal: "Préparer un produit au multilingue en 2027 : i18n (internationalisation : clés de traduction, pluriels, dates/nombres/devise par locale, RTL pour arabe/hébreu) puis l10n (traductions humaines + contextuelles, pas mot à mot). Utilise quand on vise l'international (voir aussi export 1383). N'utilise pas pour la traduction de documents ponctuels (skill 7)."
mot_cle: "i18n l10n multilingue produit clés traduction pluriels RTL locale"
nom_court: "i18n produit"
branche: "D22"
synonymes: ["préparer mon app au multilingue", "pluriels et dates par locale", "RTL arabe hébreu support"]
cross_refs: [280, 1094, 1383]
tags: ["2027"]
depends_on: [280]
---

## 1485. 🌐 Preparer son produit au multilingue (i18n/l10n, 2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Préparer un produit au multilingue en 2027 : i18n (clés de traduction externalisées, gestion pluriels/genre, formats date/nombre/devise par locale, support RTL) puis l10n (traductions humaines avec contexte).

**Quand l'utiliser (triggers)** :
- On lance en Allemagne/UK en 2027 : i18n d'abord
- Gérer pluriels et genre dans les traductions
- Format date devise par pays (de-DE, en-US)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es product manager international. Tu décris l'i18n technique (librairie i18next/next-intl, fichiers JSON par locale, ICU pour pluriels, Intl API pour dates/devises, dir=rtl) et la l10n (traducteurs pros avec contexte écran, glossaire, revue in-context). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les locales cibles (2-5 langues prioritaires)
- Le framework (React/Next, iOS, Android)
- Le volume de chaînes (~500 ?)

**Méthode** :
1. i18n : externaliser toutes les chaînes (clés, pas de texte en dur), utiliser ICU MessageFormat (pluriels/genre).
2. Formats : Intl.DateTimeFormat/NumberFormat/Currency par locale, fuseaux horaires.
3. RTL : tester dir=rtl (arabe/hébreu) sur les maquettes (miroir des icônes, marges).
4. l10n : envoyer aux traducteurs avec contexte (capture d'écran, longueur max, glossaire).
5. QA : pseudo-localisation (accents allongés) pour détecter les oublis, revue in-context par natif.

**Sorties attendues** :
- Le produit i18n-ready (clés externalisées, locales testées)
- Le glossaire + fichiers de traduction organisés
- Le plan l10n (traducteurs, revue, QA RTL)

**Exemple de prompt** :
> « On se lance en Allemagne et au Japon en 2027 : prépare le produit au multilingue (i18n clés+pluriels+dates/devises, support RTL, plan l10n avec traducteurs). »

**Cas d'usage** : Internationalisation produit, conformité locale. S'articule avec skills 280 (i18n), 1094 (cross-locale) et 1383 (export).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
