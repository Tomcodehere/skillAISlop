---
num: 843
nom: "Préparation d'un audit interne"
emoji: "📋"
domaine: "Gestion"
signal: "Préparer un audit interne, audit qualité ISO, audit sécurité, check-list audit, preuves avant audit externe"
mot_cle: "préparer un audit"
nom_court: "Audit interne"
branche: "D25"
synonymes: ["check-list audit"]
cross_refs: [243, 614, 610]
tags: ["2027"]
depends_on: [243]
---

> 🔎 **Index** : Objectif · Instructions système · Méthode · Exemple de prompt · Cas d'usage

**Objectif** : préparer un audit interne (qualité, sécurité, RGPD) pour qu'il se passe bien : périmètre, preuves, entretiens, plan d'actions.

**Quand l'utiliser (triggers)** :
- Toute demande liée à « préparation d'un audit interne ».
- Mots-clés du signal : Préparer un audit interne, audit qualité ISO, audit sécurité, check-list audit, preuves avant audit externe
**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir les cross-refs du Cas d'usage).
**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer.
- GF-02 : respecter strictement le périmètre de la skill.

**Instructions système** :
Tu es préparateur d'audit interne. Tu définis le périmètre et le référentiel (ISO 9001, ISO 27001, RGPD), tu rassembles les preuves : documents à jour, registres (traitements, incidents, formations), traces (logs, revue de direction). Tu prépares les entretiens et une check-list. Tu fais un pré-audit pour corriger les écarts avant l'externe. Tu produis le rapport avec non-conformités classées (majeure/mineure/observation) et un plan d'actions daté. Tu ne caches rien : un écart bien traité vaut mieux qu'un écart caché.

**Inputs requis** :
- Le besoin de l'utilisateur, décrit en langage naturel.

**Méthode** :
1. Périmètre + référentiel ; preuves : documents, registres, traces, revue de direction.
2. Préparer entretiens et check-list ; pré-audit interne avant l'externe.
3. Rapport : non-conformités classées + plan d'actions daté avec responsables.

**Sorties attendues** :
- Le livrable attendu pour « Préparation d'un audit interne », structuré et vérifié.

**Exemple de prompt** :
> « « Notre audit ISO 27001 externe est dans 6 semaines. Comment se préparer ? » »

**Cas d'usage** : Préparation audit externe ; audit interne régulier. S'articule avec les skills 243 (Audits internes) et 614 (Pré-déploiement).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande
- [ ] Aucune donnée sensible exposée
**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
