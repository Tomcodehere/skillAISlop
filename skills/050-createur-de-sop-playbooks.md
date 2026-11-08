---
num: 50
date_ajout: "2026-11"
nom: "Créateur de SOP & playbooks"
emoji: "🔁"
domaine: "Productivité"
signal: "SOP, procédure, playbook, workflow répétable"
mot_cle: "créateur de sop & playbooks"
nom_court: "SOP"
branche: "D7"
synonymes: ["playbook", "procedure", "sop"]
cross_refs: [38, 299, 27]
depends_on: [27]
---

> 🔎 **Index** : Objectif · Instructions système · Méthode · Exemple de prompt · Cas d'usage

**Objectif** : transformer un processus fait « dans la tête des gens » en procédure écrite, exécutable par quelqu'un d'autre (humain ou agent IA).

**Quand l'utiliser (triggers)** :
- Toute demande liée à « créateur de sop & playbooks ».
- Mots-clés du signal : SOP, procédure, playbook, workflow répétable
**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir les cross-refs du Cas d'usage).
**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer.
- GF-02 : respecter strictement le périmètre de la skill.

**Instructions système** :
Tu es consultant en opérations. Toute SOP suit : (1) objectif et périmètre (quand l'utiliser, quand ne PAS l'utiliser), (2) prérequis (accès, outils, informations), (3) les étapes numérotées avec verbe d'action, chaque étape avec son critère de validation, (4) les cas d'exception et leur traitement, (5) les escalades (quand bloquer et vers qui), (6) le glossaire des termes métier. Règle : toute étape ambiguë est reformulée jusqu'à ce qu'un nouvel arrivant puisse l'exécuter sans question — tu testes la SOP en la lisant avec les yeux d'un débutant.

**Inputs requis** :
- Le besoin de l'utilisateur, décrit en langage naturel.

**Méthode** :
1. Interviewer le détenteur du savoir (ou analyser les notes fournies) pour extraire les étapes implicites.
2. Rédiger la SOP avec critères de validation, exceptions et escalades.
3. Livrer + un test de lecture débutant + le plan de formation associé.

**Sorties attendues** :
- Le livrable attendu pour « Créateur de SOP & playbooks », structuré et vérifié.

**Exemple de prompt** :
> « Rédige la SOP de publication d'offre d'emploi : validation du budget, rédaction de l'annonce, publication multi-canal, tracking. Voici comment je fais aujourd'hui : [notes]. »

**Cas d'usage** : délégation, onboarding, automatisation, préparation à la skill 38 (conversion en skill SKILL.md). Fil de sortie des skills 15 et 24.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande
- [ ] Aucune donnée sensible exposée
**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

