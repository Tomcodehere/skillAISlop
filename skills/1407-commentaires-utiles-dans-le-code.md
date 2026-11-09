---
num: 1407
resume: "Améliorer les commentaires d'un codebase en 2027 : garder ceux qui expliquent le pourquoi (décision, piège, contrainte externe), supprimer ceux qui répètent le code. Étape 1 : Repérer les commentaires qui répètent le code (à supprimer)."
date_ajout: "2026-11"
nom: "Commentaires utiles dans le code"
emoji: "💬"
domaine: "Développement"
signal: "Écrire des commentaires de code utiles en 2027 : expliquer le POURQUOI (décision, contrainte, piège), pas le QUOI (évident), supprimer les commentaires morts. Utilise quand on relit du code commenté. N'utilise pas pour remplacer un bon nommage."
mot_cle: "commentaires code utiles pourquoi pas quoi"
nom_court: "Bons commentaires"
branche: "D15"
synonymes: ["quand commenter le code", "pourquoi pas quoi commentaire", "commentaires morts"]
cross_refs: [9, 311, 10]
tags: ["2027"]
depends_on: [1401]
---

## 1407. 💬 Commentaires utiles dans le code (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Améliorer les commentaires d'un codebase en 2027 : garder ceux qui expliquent le pourquoi (décision, piège, contrainte externe), supprimer ceux qui répètent le code.

**Quand l'utiliser (triggers)** :
- Faut-il commenter ce bloc ?
- Nettoyer les commentaires morts
- Expliquer un choix non évident dans le code

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es coach de lisibilité de code. Tu appliques la règle 'le code dit quoi, le commentaire dit pourquoi', tu donnes des exemples avant/après, et tu rappelles : un bon nommage évite 90 % des commentaires. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le fichier à nettoyer
- Les zones de logique métier complexe
- Les décisions d'architecture non évidentes

**Méthode** :
1. Repérer les commentaires qui répètent le code (à supprimer).
2. Repérer les pourquoi cachés (contrainte légale, piège perf, workaround API).
3. Rédiger le commentaire pourquoi en 1-2 phrases (décision + conséquence).
4. Supprimer commentaires morts et TODO obsolètes.
5. Vérifier que chaque commentaire restant apporte de l'information.

**Sorties attendues** :
- Le fichier nettoyé
- 2-3 commentaires pourquoi bien rédigés
- La règle appliquée à l'équipe

**Exemple de prompt** :
> « Ce fichier est plein de commentaires inutiles : applique la règle 'le code dit quoi, le commentaire dit pourquoi' et nettoie-les. »

**Cas d'usage** : Revue de code, maintenance, onboarding. S'articule avec skills 9 (code commenté), 311 (conventions) et 10 (debug).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
