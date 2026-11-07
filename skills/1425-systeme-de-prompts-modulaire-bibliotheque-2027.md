---
num: 1425
date_ajout: "2026-11"
nom: "Systeme de prompts modulaire (bibliotheque, 2027)"
emoji: "🧩"
domaine: "IA / Prompting"
signal: "Organiser ses prompts en bibliothèque modulaire en 2027 : composants réutilisables (rôle, format de sortie, exemples), assemblés par tâche, versionnés comme du code (Git, tags), testés. Utilise quand on maintient plusieurs prompts en prod. N'utilise pas pour un prompt one-shot."
mot_cle: "bibliothèque prompts modulaires composants réutilisables"
nom_court: "Prompts modulaires"
branche: "D14"
synonymes: ["organiser ses prompts", "composants de prompt réutilisables", "prompts versionnés git"]
cross_refs: [1244, 737, 17]
tags: ["2027"]
depends_on: [1244]
---

## 1425. 🧩 Systeme de prompts modulaire (bibliotheque, 2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Construire une bibliothèque de prompts modulaires en 2027 : composants réutilisables (rôle, contraintes, format de sortie, few-shot), assemblés par tâche, versionnés dans Git et testés.

**Quand l'utiliser (triggers)** :
- J'ai 30 prompts éparpillés, comment les organiser ?
- Composants de prompt réutilisables
- Versionner mes prompts dans git

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte de prompts. Tu proposes une structure (dossier /prompts avec composants _role, _output, _examples + templates par tâche), le versionning Git (tag par release), et un test rapide par prompt. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les prompts existants (fichiers, inline dans le code)
- Les tâches couvertes
- L'équipe qui les maintient

**Méthode** :
1. Inventorier tous les prompts utilisés (grep, fichiers).
2. Extraire les composants communs (rôle système, format JSON, exemples few-shot).
3. Créer /prompts avec composants + templates assemblés par tâche.
4. Versionner dans Git, taguer par release (v1.2.0).
5. Ajouter un test par template (exécution sur un cas de test).

**Sorties attendues** :
- La bibliothèque /prompts structurée
- Le versioning Git + tags
- Un test par template

**Exemple de prompt** :
> « Nos prompts sont copiés-collés partout : crée une bibliothèque modulaire (composants rôle/format/exemples, templates par tâche, git + tests). »

**Cas d'usage** : Équipes produit/IA, cohérence des sorties, maintenance. S'articule avec skills 1244 (versioning prompts), 737 (prompt avancé) et 17 (meta-prompting).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
