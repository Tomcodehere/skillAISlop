---
num: 1494
resume: "Produire un prototype cliquable en 1 jour en 2027 avec v0/Lovable/Bolt (prompt → app fonctionnelle) ou Figma Make, pour tester une idée avec de vrais utilisateurs avant tout dev (test 1483). Étape 1 : Choisir l'outil (v0 pour UI, Lovable/Bolt pour full-stack avec 'backend' factice)."
date_ajout: "2026-11"
nom: "Prototype cliquable en 1 jour avec l'IA"
emoji: "⚡"
domaine: "Design"
signal: "Créer un prototype cliquable en 1 jour en 2027 avec l'IA : v0, Lovable, Bolt.new (prompt → app React fonctionnelle), ou Figma Make (maquette → interactif). Utilise pour tester une idée avant dev. N'utilise pas pour de la prod (code IA à revoir, 724)."
mot_cle: "prototype cliquable 1 jour v0 lovable bolt figma make IA"
nom_court: "Proto IA 1 jour"
branche: "D22"
synonymes: ["v0 ou lovable pour prototyper", "maquette en app cliquable en 1 jour", "tester une idée sans dev"]
cross_refs: [608, 540, 724]
tags: ["2027"]
depends_on: [608]
---

## 1494. ⚡ Prototype cliquable en 1 jour avec l'IA (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Produire un prototype cliquable en 1 jour en 2027 avec v0/Lovable/Bolt (prompt → app fonctionnelle) ou Figma Make, pour tester une idée avec de vrais utilisateurs avant tout dev (test 1483).

**Quand l'utiliser (triggers)** :
- Tester cette feature sans attendre les devs
- v0 vs Lovable vs Bolt en 2027
- prompter un prototype fonctionnel

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es product designer IA-first. Tu compares les outils (v0 = composants shadcn, Lovable = full-stack, Bolt = StackBlitz, Figma Make = maquette→code), et tu rappelles : c'est pour valider, le code généré n'est pas de la prod (revue 724). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'idée à prototyper (spec 1480, maquette Figma)
- Les données factices (mock)
- Les 2-3 parcours à rendre cliquables

**Méthode** :
1. Choisir l'outil (v0 pour UI, Lovable/Bolt pour full-stack avec 'backend' factice).
2. Prompter : rôle, écrans, parcours, données mock, style (design system existant).
3. Itérer 3-5 prompts jusqu'à un parcours cliquable satisfaisant.
4. Déployer (preview v0/Lovable) et partager le lien pour tests utilisateurs (1483).
5. Noter ce qui marche/rate pour la spec dev (1480), jeter le code après.

**Sorties attendues** :
- Le prototype cliquable en ligne (lien partageable)
- Les retours des 5 premiers testeurs
- La spec affinée pour le dev réel

**Exemple de prompt** :
> « On veut tester le nouveau parcours 'créer un projet en 3 étapes' avant dev : fais un prototype cliquable en 1 jour (Lovable, données mock, lien testable). »

**Cas d'usage** : Validation rapide d'idées, démo stakeholders, tests utilisateurs. S'articule avec skills 608 (design-to-code), 540 (vibe coding) et 724 (vérifiabilité code IA).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
