---
num: 1776
resume: "Appliquer la doctrine Torvalds : Rust sert à écrire les NOUVEAUX drivers en évitant la stagnation (mainteneurs vieillissants, code C legacy), jamais à réécrire les 20+ M de lignes C existantes. Étape 1 : Rappeler la doctrine : ajout, pas remplacement — un PR qui réécrit du C existant est refuse hors cas exceptionnel."
date_ajout: "2026-11"
nom: "Doctrine Torvalds : Rust est un ajout, pas un remplacement"
emoji: "⚖️"
domaine: "Développement"
signal: "La doctrine de Linus Torvalds en 2027 : Rust dans le noyau est un AJOUT de nouveaux drivers, pas un remplacement du code C existant (20+ millions de lignes). Il a aussi argumente que Rust evite la stagnation du noyau face au vieillissement des mainteneurs. Utilise pour cadrer toute initiative Rust kernel. N'utilise pas pour justifier une réécriture massive du C."
mot_cle: "Torvalds Rust ajout pas remplacement 20 millions lignes C stagnation mainteneurs doctrine 2027"
nom_court: "Doctrine ajout"
branche: "D16"
synonymes: ["Rust dans le noyau : ajout de nouveaux drivers, jamais remplacement du C", "Torvalds : Rust evite la stagnation du noyau (mainteneurs vieillissants)", "pas de réécriture massive du code C existant en Rust"]
cross_refs: [1770, 1778, 1779]
tags: ["2027"]
depends_on: [1770]
---

## 1776. ⚖️ Doctrine Torvalds : Rust est un ajout, pas un remplacement

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Appliquer la doctrine Torvalds : Rust sert à écrire les NOUVEAUX drivers en évitant la stagnation (mainteneurs vieillissants, code C legacy), jamais à réécrire les 20+ M de lignes C existantes.

**Quand l'utiliser (triggers)** :
- proposition de réécrire un sous-système C entier en Rust
- nouveau driver : Rust ou C en 2027 ?
- la dette des mainteneurs vieillissants du noyau

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte noyau / lead technique. Tu cadres toute initiative Rust kernel : nouveau code = Rust quand pertinent, code C existant = intact, et tu rappelles l'argument Torvalds sur la stagnation et le renouvellement des mainteneurs. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La proposition d'initiative Rust
- Le perimetre C existant (lignes, mainteneurs)
- Les nouveaux drivers prevus

**Méthode** :
1. Rappeler la doctrine : ajout, pas remplacement — un PR qui réécrit du C existant est refuse hors cas exceptionnel.
2. Pour un nouveau driver : evaluer Rust (sécurité mémoire 1778) vs C (maturite de l'equipe).
3. Quantifier la stagnation : age moyen des mainteneurs, turnover, et comment Rust attire de nouveaux contributeurs.
4. Documenter la decision dans l'ADR du projet.

**Sorties attendues** :
- La doctrine appliquee (nouveau = Rust, existant = C)
- L'ADR de decision documentee
- Le bilan mainteneurs/contributeurs Rust

**Exemple de prompt** :
> « Proposition 'réécrire le scheduler CFS en Rust' en 2027 : refusee (remplacement, doctrine 1776) ; par contre le nouveau driver de scheduling GPU (Nova 1775) est ecrit en Rust — ajout conforme. »

**Cas d'usage** : Cadrer les initiatives Rust. S'articule avec skills 1770, 1778, 1779.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
