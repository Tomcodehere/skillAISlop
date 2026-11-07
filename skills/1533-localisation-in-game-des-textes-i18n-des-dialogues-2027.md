---
num: 1533
nom: "Localisation in-game des textes (i18n des dialogues, 2027)"
emoji: "🌐"
domaine: "Game Dev"
signal: "Localiser les textes d'un jeu en 2027 : clés de traduction (ui.title, quest.rats.desc) dans des fichiers par langue (JSON/CSV/PO), pluriels et genre (ICU), noms propres inchangés, longueur max par UI, test de pseudo-localisation (accents allongés) pour détecter les débordements. Utilise quand on sort un jeu à l'international. N'utilise pas pour la traduction de docs (skill 7)."
mot_cle: "localisation jeu i18n clés traduction pluriels ICU pseudo-localisation"
nom_court: "Loca in-game"
branche: "D22"
synonymes: ["traduire les textes du jeu en 5 langues", "clés ui.title quest.desc par langue JSON", "pseudo-localisation détecter débordements UI"]
cross_refs: [1485, 1094, 1532]
tags: ["2027"]
depends_on: [1485]
---

## 1533. 🌐 Localisation in-game des textes (i18n des dialogues, 2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Localiser un jeu en 2027 : toutes les chaînes sous forme de clés (ui.title, quest.x.desc) dans des fichiers par langue, ICU pour pluriels/genre, longueur max, pseudo-localisation pour tester les débordements d'UI avant traduction.

**Quand l'utiliser (triggers)** :
- Tous les textes du jeu en 5 langues (FR/EN/DE/ES/JA)
- Pluriels : '1 rat' vs '5 rats' selon la langue
- Pseudo-localisation : détecter les textes trop longs pour l'UI

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es localization engineer. Tu structures : clés stables (jamais le texte FR comme clé), fichiers fr.json/en.json..., ICU MessageFormat pour pluriels, champ maxLen par clé pour l'UI, et pseudo-loc (à targuer : 'Šéñţéñçé' allongée) en dev. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les textes du jeu (UI, dialogues 1532, quêtes 1531)
- Les langues cibles (5)
- Les contraintes d'UI (longueur max par composant)

**Méthode** :
1. Externaliser : chaque texte → clé (quest.rats.desc) + valeur par langue (JSON/PO/CSV selon moteur).
2. ICU pour pluriels/genre : '{count, plural, one {# rat} other {# rats}}'.
3. maxLen par clé UI (bouton 12 car.) ; le moteur tronque ou shrink la fonte.
4. Pseudo-localisation en dev : remplacer les voyelles par des accentuées allongées (detecte débordements).
5. QA : relecture in-game par natif, captures d'écran des 5 langues, glossaire (noms propres).

**Sorties attendues** :
- Les 5 langues prêtes (fichiers + ICU pluriels)
- La pseudo-localisation validée (pas de débordement)
- Le glossaire et la QA par natif

**Exemple de prompt** :
> « On sort le jeu en FR/EN/DE/ES/JA : externalise tous les textes en clés + 5 fichiers de langue, ICU pour les pluriels, pseudo-loc pour détecter les débordements de boutons. »

**Cas d'usage** : Sortie internationale d'un jeu. S'articule avec skills 1485 (i18n produit), 1094 (cross-locale) et 1532 (dialogues).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
