---
num: 1744
date_ajout: "2026-11"
nom: "Sourcegraph Cody : chercher dans une grosse codebase (2027)"
emoji: "🔎"
domaine: "Développement"
signal: "Naviguer dans une grosse codebase (monorepo, 100k fichiers) en 2027 avec Sourcegraph Cody : recherche structurelle (regex + AST, ex. 'tous les appels à l'ancienne API auth'), navigation par symboles (définitions/références cross-repo), chat contextuel (@fichier), self-host possible (1633). Incontournable pour les grandes bases. N'utilise pas pour un petit repo (grep suffit)."
mot_cle: "sourcegraph cody grosse codebase monorepo 2027 recherche structurelle AST symboles cross-repo chat contextuel self-host"
nom_court: "Sourcegraph"
branche: "D1"
synonymes: ["trouver tous les appels à l'ancienne API auth dans 100k fichiers (Cody AST)", "navigation par symboles cross-repo (définitions/références) 2027", "Cody self-host (1633) pour du code interne qui ne sort pas"]
cross_refs: [257, 313, 1633]
tags: ["2027"]
depends_on: [257]
---

## 1744. 🔎 Sourcegraph Cody : chercher dans une grosse codebase (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Naviguer dans une grosse codebase en 2027 avec Sourcegraph Cody : recherche structurelle (AST/regex : 'tous les appels à l'ancienne API'), navigation par symboles cross-repo, chat contextuel — self-host (1633) pour le code interne.

**Quand l'utiliser (triggers)** :
- où est définie cette fonction, utilisée où dans le monorepo ? (Cody)
- recherche structurelle : tous les appels à db.query( dans le repo (AST)
- Cody self-hosté : mon code interne ne sort pas (1633)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es dev monorepo. Tu déploies Sourcegraph (cloud ou self-host 1633), tu indexes les repos (git clone + index), tu utilises la recherche structurelle (lang:go pattern:...) et Cody chat avec contexte (@repo @file). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les repos à indexer (monorepo)
- Le mode (cloud public ou self-host 1633)
- Cody (extension VS Code ou app)

**Méthode** :
1. Indexer les repos sur Sourcegraph (cloud sourcegraph.com pour l'open source, ou self-host pour l'interne 1633).
2. Recherche structurelle : patternType:literal/regexp/structural (AST) — ex. 'db.query($$$)' trouve tous les appels avec les vrais arguments (pas de faux positifs texte).
3. Navigation : définitions/références par symbole, cross-repo (qui appelle cette fonction dans tous les repos indexés).
4. Cody chat : @repo @fichier pour poser une question avec le bon contexte ; il répond en citant les fichiers/lignes.
5. Self-host : Sourcegraph self-hosted + modèle local (1633) → le code interne ne sort jamais (1736).
6. Alternative : grep/ripgrep (523) pour un petit repo ; Cody indispensable au-delà de ~10k fichiers.

**Sorties attendues** :
- Sourcegraph (cloud ou self-host 1633) avec les repos indexés
- La recherche AST utilisée sur un cas réel (ex. tous les appels à l'ancienne API)
- Cody chat contextuel (@repo @file) testé

**Exemple de prompt** :
> « Monorepo de 100k fichiers, l'ancienne API auth est à supprimer : Sourcegraph + Cody — recherche AST 'auth.oldLogin($$$)' → liste exacte cross-repo, migration planifiée (1737), self-host (1633) pour l'interne. »

**Cas d'usage** : Grosses codebases/monorepos. S'articule avec skills 257 (explorer code inconnu), 313 (monorepo), 1633 (local), 523 (regex).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
