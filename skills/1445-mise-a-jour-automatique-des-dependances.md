---
num: 1445
resume: "Automatiser les mises à jour de dépendances en 2027 avec Dependabot/Renovate : PR auto groupées par écosystème, CI verte requise, CVE/sécurité prioritaires (merge rapide), changelogs majeurs relus. Étape 1 : Activer Dependabot/Renovate avec config par écosystème (npm, pip...)."
lang: "fr"
date_ajout: "2026-11"
nom: "Mise a jour automatique des dependances"
emoji: "🔄"
domaine: "Sécurité"
signal: "Gérer les mises à jour de dépendances en sécurité en 2027 : Dependabot ou Renovate (PR auto, groupées, tests CI), revue des changelogs des versions majeures, correctifs de sécurité prioritaires (CVE). Utilise quand on maintient une app avec dépendances. N'utilise pas pour le scan de vulnérabilités lui-même (voir SBOM 267)."
mot_cle: "dependabot renovate mise à jour dépendances PR auto CVE"
nom_court: "MAJ dépendances"
branche: "D23"
synonymes: ["PR auto dépendances Dependabot", "renovate bot mises à jour", "CVE corriger en priorité"]
cross_refs: [267, 505, 308]
tags: ["2027"]
depends_on: [505]
---

## 1445. 🔄 Mise a jour automatique des dependances (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Automatiser les mises à jour de dépendances en 2027 avec Dependabot/Renovate : PR auto groupées par écosystème, CI verte requise, CVE/sécurité prioritaires (merge rapide), changelogs majeurs relus.

**Quand l'utiliser (triggers)** :
- Mettre en place Dependabot sur le repo
- PR auto pour les mises à jour de dépendances
- Comment gérer 40 PR de dépendances par semaine ?

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es responsable supply chain code. Tu configures Dependabot/Renovate (fréquence hebdo, groupement par écosystème, labels 'security' pour les CVE), la règle CI verte avant merge, et la revue des majors (changelog). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le gestionnaire de paquets (npm, pip, go, maven)
- La fréquence souhaitée (hebdo)
- La politique de merge auto (patch oui, major non)

**Méthode** :
1. Activer Dependabot/Renovate avec config par écosystème (npm, pip...).
2. Grouper les mises à jour mineures/patchs (1 PR/semaine/écosystème).
3. Label 'security' + merge prioritaire pour les CVE (505).
4. CI obligatoire : tests + lint + scan SCA avant merge.
5. Majors : relire le changelog, tester en staging, ne jamais auto-merger.

**Sorties attendues** :
- La config Dependabot/Renovate en place
- Le rythme de PR (ex. 3/semaine groupées)
- La règle CVE = merge rapide après CI

**Exemple de prompt** :
> « On a 40 PR de dépendances en attente et des CVE en retard : configure Dependabot/Renovate (groupées hebdo, CVE prioritaires, CI verte obligatoire). »

**Cas d'usage** : Sécurité continue, dette de dépendances, conformité. S'articule avec skills 267 (SBOM), 505 (correctifs CVE) et 308 (bench).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
