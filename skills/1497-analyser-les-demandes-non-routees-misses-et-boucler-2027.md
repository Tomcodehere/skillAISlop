---
num: 1497
date_ajout: "2026-11"
nom: "Analyser les demandes non routees (misses) et boucler (2027)"
emoji: "📊"
domaine: "Routage"
signal: "Analyser le journal des demandes non routées (exit 2, commande misses) en 2027 : motifs récurrents, suggestions auto (misses --suggest), ajouter synonymes ou créer la skill manquante, puis build + test. Utilise quand le routeur renvoie souvent exit 2. N'utilise pas pour choisir une skill manuellement (1372)."
mot_cle: "misses demandes non routées exit 2 suggestions boucler synonymes"
nom_court: "Analyser misses"
branche: "D26"
synonymes: ["exit 2 trop fréquent routeur", "demandes non routées récurrentes", "misses --suggest ajouter synonyme"]
cross_refs: [0, 250, 1372]
tags: ["2027"]
depends_on: [1372]
---

## 1497. 📊 Analyser les demandes non routees (misses) et boucler (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Analyser le journal des misses (exit 2) en 2027 : lancer misses --suggest, identifier les motifs récurrents (synonyme manquant vs vraie lacune), ajouter les synonymes ou créer la skill manquante, puis build + test + sonde.

**Quand l'utiliser (triggers)** :
- Le routeur renvoie exit 2 souvent
- Quelles demandes ne sont jamais routées ?
- Ajouter un synonyme après un miss

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es analyste du routeur de skills. Tu déroules le cycle : routage.py misses → misses --suggest (proximité trigrammes) → ajouter dans SYNONYMES (ou créer la skill 250) → build → test → sonde ; et tu mesures la baisse du taux d'exit 2. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le journal non_routees (après usage réel)
- Les suggestions automatiques (misses --suggest)
- La capacité à ajouter des synonymes/skills

**Méthode** :
1. Lancer python3 routage.py misses (liste des demandes non routées, fréquences).
2. misses --suggest : pour chaque, la skill la plus proche (recouvrement trigrammes).
3. Décider : synonyme à ajouter (demande couverte) ou vraie lacune (nouvelle skill via 250).
4. Ajouter dans SYNONYMES, puis build + lint + test + sonde.
5. Re-mesurer le taux d'exit 2 (objectif : tendre vers 0) et vider le journal (misses --clear).

**Sorties attendues** :
- Le rapport des misses avec motifs
- Les synonymes/skills ajoutés
- Le taux d'exit 2 avant/après

**Exemple de prompt** :
> « Depuis 2 semaines, 15 demandes/jour en exit 2 : analyse le journal misses --suggest, ajoute les synonymes manquants, rebuild, et vérifie que le taux d'exit 2 baisse. »

**Cas d'usage** : Amélioration continue du catalogue, couverture sonde 100 %. S'articule avec skills 0 (routeur), 250 (conservateur) et 1372 (dispatch manuel).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
