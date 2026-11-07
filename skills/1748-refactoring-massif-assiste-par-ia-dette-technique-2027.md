---
num: 1748
date_ajout: "2026-11"
nom: "Refactoring massif assisté par IA : dette technique (2027)"
emoji: "🧹"
domaine: "Développement"
signal: "S'attaquer à la dette technique en 2027 avec l'IA : identifier la dette (duplications, god objects, TODO 606), puis refactorer par petits lots testés (1405) avec l'agent (Claude Code 1737 plan mode, Cursor 1740 Composer) : un module par semaine, tests auto (1747) avant/après, couverture maintenue, revue (1401). Ne pas tout réécrire d'un coup. N'utilise pas sans tests (1747) et sans plan (1405)."
mot_cle: "dette technique 2027 refactoring massif IA petits lots testés 1405 Claude Code plan Cursor Composer tests 1747 revue 1401"
nom_court: "Dette IA"
branche: "D12"
synonymes: ["refactorer un god object de 3000 lignes avec Claude Code (plan mode 1737)", "1 module de dette par semaine, tests auto (1747) avant/après, jamais tout d'un coup", "détecter les duplications dans le code (IA) pour la dette (606)"]
cross_refs: [606, 1405, 1747]
tags: ["2027"]
depends_on: [1405]
---

## 1748. 🧹 Refactoring massif assisté par IA : dette technique (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Réduire la dette technique en 2027 avec l'IA : identifier (duplications, god objects, TODO 606), refactorer par petits lots testés (1405) avec l'agent (plan mode 1737/Composer 1740), tests auto avant/après (1747), revue (1401), 1 module/semaine.

**Quand l'utiliser (triggers)** :
- ce fichier de 3000 lignes est un god object, par où commencer ?
- 1 module de dette par semaine avec l'agent IA + tests (1747)
- ne JAMAIS tout réécrire d'un coup (1405 petits pas)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es tech lead dette. Tu fais un plan de dette (top 10 modules par criticité × effort 606), chaque semaine 1 module : tests auto d'abord (1747), puis l'agent refactor en plan mode (1737), diffs validés (1401), tests après, couverture maintenue (1658). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La dette identifiée (606)
- L'agent (1737/1740)
- Les tests auto (1747) et la revue (1401)

**Méthode** :
1. Inventaire dette : duplications (détection IA/Cody 1744), god objects (taille + complexité cyclomatique 308), TODO/FIXME, code mort — scoré par criticité × effort (606).
2. Plan : top 10 modules, 1 par semaine, ordre : plus critique d'abord.
3. Par module : (1) tests auto de caractérisation (1747, golden 1405), (2) l'agent propose le plan de refacto (1737 plan mode), (3) exécution par petits lots (extract method/rename 1405), (4) tests après = mêmes résultats + couverture maintenue (1658), (5) revue PR (1401), merge.
4. Jamais de big bang : si le plan dépasse 1 semaine, découper.
5. Métriques : dette restante (score 606), couverture (stable ou up), bugs post-refacto (objectif 0, 256).

**Sorties attendues** :
- Le plan de dette 2027 (top 10 modules, 1/semaine) avec métriques
- Un module refactoré proprement (tests 1747 avant/après, couverture 1658, revue 1401)
- Les métriques : dette restante, 0 bug post-refacto (256)

**Exemple de prompt** :
> « God object de 3000 lignes dans le paiement : plan dette 2027 (1 module/semaine) — tests auto de caractérisation (1747), Claude Code plan mode (1737) découpe en services, petits lots (1405), tests après (1658), revue (1401), 0 bug (256). »

**Cas d'usage** : Dette technique à grande échelle. S'articule avec skills 606 (sprint dette), 1405 (refacto sûr), 1747 (tests auto), 1737 (Claude Code), 1401 (revue).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
