---
num: 1493
resume: "Auditer la cohérence visuelle d'un produit en 2027 : inventorier les variantes réelles de chaque composant (boutons, couleurs, typos, espacements) vs le design system, lister les écarts, et planifier la convergence. Étape 1 : Capturer 20 écrans représentatifs du produit en prod."
date_ajout: "2026-11"
nom: "Audit de coherence visuelle d'un produit"
emoji: "🔍"
domaine: "Design"
signal: "Auditer la cohérence visuelle d'un produit existant en 2027 : inventaire des composants (boutons, couleurs, typos, espacements, icônes) réellement utilisés vs le design system (455/732), écarts trouvés, plan de convergence. Utilise quand l'UI est devenue incohérente. N'utilise pas pour créer le design system (voir 455)."
mot_cle: "audit cohérence visuelle produit composants vs design system écarts"
nom_court: "Audit visuel"
branche: "D22"
synonymes: ["notre UI est incohérente audit", "composants réels vs design system", "combien de boutons différents avons-nous ?"]
cross_refs: [455, 732, 64]
tags: ["2027"]
depends_on: [455]
---

## 1493. 🔍 Audit de coherence visuelle d'un produit (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Auditer la cohérence visuelle d'un produit en 2027 : inventorier les variantes réelles de chaque composant (boutons, couleurs, typos, espacements) vs le design system, lister les écarts, et planifier la convergence.

**Quand l'utiliser (triggers)** :
- On a 12 variantes de bouton, audit
- Notre UI n'est plus cohérente
- Écart entre Figma et le code réel

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es design system auditor. Tu décris la méthode : screenshot de 20 écrans clés, inventaire des variantes par composant (taille, couleur, état), comparaison au design system (tokens 455), écarts classés (critique/majeur/mineur), plan de convergence avec effort estimé. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le produit en prod (écrans clés)
- Le design system existant (Figma + code)
- Les composants critiques (boutons, formulaires, tableaux)

**Méthode** :
1. Capturer 20 écrans représentatifs du produit en prod.
2. Inventorier : pour chaque composant, lister les variantes vues (couleurs, tailles, arrondis...).
3. Comparer au design system (tokens + composants officiels), classer les écarts.
4. Prioriser : écarts sur parcours critiques (paiement, erreur) d'abord.
5. Plan de convergence : supprimer les variantes, unifier sur le DS, effort par composant, roadmap.

**Sorties attendues** :
- L'inventaire des variantes par composant
- La liste des écarts classés (critique/majeur/mineur)
- Le plan de convergence avec effort et priorités

**Exemple de prompt** :
> « Notre app a 15 boutons différents selon les pages : fais l'audit de cohérence visuelle (inventaire vs design system, écarts classés, plan de convergence). »

**Cas d'usage** : Maintenabilité UI, confiance marque, vitesse de dev. S'articule avec skills 455 (design tokens), 732 (design system) et 64 (critique UX).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
