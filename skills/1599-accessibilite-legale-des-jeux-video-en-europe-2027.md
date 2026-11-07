---
num: 1599
date_ajout: "2026-11"
nom: "Accessibilite legale des jeux video en Europe (2027)"
emoji: "⚖️"
domaine: "Game Dev"
signal: "Se mettre en conformité accessibilité des jeux en Europe en 2027 (European Accessibility Act, en vigueur juin 2025, jeux concernés) : jeux utilisables par des personnes handicapées (visuel 1575 filtres daltonisme, moteur 1571 clavier/manette complet, cognitif : tutoriel skippable 1572, temps ajustable, pas d'info par couleur seule), rapport d'accessibilité publié, CVAA-like. Utilise pour tout jeu vendu en UE. N'utilise pas pour un prototype interne."
mot_cle: "European Accessibility Act 2027 jeux vidéo conformité accessibilité rapport CVAA"
nom_court: "A11y légale UE"
branche: "D23"
synonymes: ["European Accessibility Act en vigueur juin 2025 pour les jeux (UE)", "rapport d'accessibilité publié avec le jeu", "jeu jouable au clavier seul (1571) et avec lecteur d'écran"]
cross_refs: [1575, 1571, 1484]
tags: ["2027"]
depends_on: [1575]
---

## 1599. ⚖️ Accessibilite legale des jeux video en Europe (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Se mettre en conformité avec l'European Accessibility Act (2027) pour un jeu vendu en UE : jouable clavier/manette seuls (1571), options visuelles (daltonisme 1575), cognitives (tutoriel skippable 1572, pas de timer strict), rapport d'accessibilité publié, et conformité CVAA-like vérifiée.

**Quand l'utiliser (triggers)** :
- L'European Accessibility Act s'applique aux jeux depuis juin 2025
- Rapport d'accessibilité à publier avec le jeu
- Le jeu doit être jouable au clavier seul (1571)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es responsable conformité accessibilité. Tu appliques l'EAA (en vigueur 28 juin 2025, jeux vidéo couverts) : fonctionnalités d'accessibilité (1575), information d'accessibilité sur la page store (1581), rapport de conformité, et processus interne (formation équipe, tests 1598 avec joueurs handicapés). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le jeu vendu en UE (Steam 1579)
- Les options d'accessibilité existantes (1575, 1571, 1572)
- La page store (1581) et le rapport de conformité

**Méthode** :
1. Vérifier le périmètre EAA : jeu vendu en UE après juin 2025 → couvert (services de jeux vidéo).
2. Fonctionnalités requises : jouable clavier/manette seuls (1571), options visuelles (contraste 1575, daltonisme, taille 1575), cognitives (pas de timer strict, tutoriel skippable 1572, pause), audio (sous-titres 1569, volume séparé 1574).
3. Information : page store avec section accessibilité (fonctionnalités + contact), rapport de conformité (format UE) publié.
4. Processus : checklists dans le QA (1591/1598 avec joueurs handicapés), formation équipe, accessibilité dans le GDD (1596... non).
5. Sanctions : amende possible par État membre si non conforme → audit interne annuel.

**Sorties attendues** :
- Le jeu conforme EAA 2027 (fonctionnalités + info store + rapport)
- Le rapport de conformité publié (format UE)
- Le processus QA incluant l'accessibilité (1598)

**Exemple de prompt** :
> « Le jeu sort en UE sur Steam (1579) : conforme à l'European Accessibility Act 2027 (clavier/manette seuls 1571, options visuelles 1575, sous-titres 1569, rapport de conformité publié, section accessibilité sur la page store 1581, QA avec joueurs handicapés 1598). »

**Cas d'usage** : Conformité légale UE. S'articule avec skills 1575 (accessibilité jeu), 1571 (menus) et 1484 (a11y design).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
