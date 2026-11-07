---
num: 1465
date_ajout: "2026-11"
nom: "Anonymisation et pseudonymisation des donnees (RGPD, 2027)"
emoji: "🎭"
domaine: "Data"
signal: "Anonymiser/pseudonymiser un dataset en 2027 pour le RGPD : pseudonymisation (id hashé avec sel, réversible sur autorisation), k-anonymat (k supérieur ou égal à 5), généralisation (tranches d'âge, départements), suppression des quasi-identifiants, test de ré-identification. Utilise quand on partage/publie des données avec données perso. N'utilise pas pour le PII en direct dans les prompts (voir 1440)."
mot_cle: "anonymisation pseudonymisation k-anonymat RGPD dataset partager"
nom_court: "Anonymisation"
branche: "D15"
synonymes: ["k-anonymat k=5 dataset", "hash avec sel pseudonymisation", "test ré-identification risque"]
cross_refs: [1226, 189, 1440]
tags: ["2027"]
depends_on: [189]
---

## 1465. 🎭 Anonymisation et pseudonymisation des donnees (RGPD, 2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Anonymiser un dataset en 2027 pour le RGPD : pseudonymisation (hash salé) ou k-anonymat (k supérieur ou égal à 5) + généralisation des quasi-identifiants, avec un test de risque de ré-identification avant partage.

**Quand l'utiliser (triggers)** :
- Partager un dataset clients avec un partenaire, comment anonymiser ?
- k-anonymat ou pseudonymisation ?
- Risque de ré-identification : le mesurer

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es DPO data. Tu distingues pseudonymisation (réversible, reste des données perso) et anonymisation (irréversible, plus du RGPD), tu appliques k-anonymat (k supérieur ou égal à 5) + généralisation (tranches), et tu fais un test de ré-identification. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le dataset à partager et sa finalité
- Les quasi-identifiants (date naissance, CP, métier)
- Le niveau de risque acceptable (k et epsilon pour différentiel)

**Méthode** :
1. Identifier les identifiants directs (nom, email, tél) → supprimer ou hasher salé (pseudonymisation).
2. Quasi-identifiants (date naissance, CP, sexe, métier) → généraliser (tranches d'âge 10 ans, département, catégorie).
3. Appliquer k-anonymat : chaque combinaison de quasi-identifiants doit avoir k supérieur ou égal à 5 lignes.
4. Tester le risque de ré-identification (attaque par connaissance du contexte).
5. Documenter la méthode + registre (1226) ; si vraiment anonymisé, plus de RGPD.

**Sorties attendues** :
- Le dataset anonymisé/pseudonymisé
- Le rapport de risque de ré-identification (k)
- La doc méthode + registre des traitements

**Exemple de prompt** :
> « On partage notre dataset clients (200k lignes) avec un labo : anonymise-le (pseudonymisation hash salé + k-anonymat k=5 + généralisation CP/âge) et teste la ré-identification. »

**Cas d'usage** : Partage de données, open data, recherche, ML sur données perso. S'articule avec skills 1226 (flux données), 189 (RGPD) et 1440 (PII).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
