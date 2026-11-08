---
num: 1426
date_ajout: "2026-11"
nom: "Few-shot : exemples dans les prompts"
emoji: "📝"
domaine: "IA / Prompting"
signal: "Utiliser le few-shot (3-5 exemples entrée/sortie dans le prompt) en 2027 pour guider le format et le style d'un LLM, avec des exemples représentatifs et des cas limites. Utilise quand le zero-shot ne suffit pas. N'utilise pas avec trop d'exemples (coût en tokens)."
mot_cle: "few-shot exemples dans le prompt 3-5 exemples"
nom_court: "Few-shot"
branche: "D14"
synonymes: ["exemples dans le prompt LLM", "few shot prompting", "guider le format avec des exemples"]
cross_refs: [737, 738, 1244]
tags: ["2027"]
depends_on: [737]
---

## 1426. 📝 Few-shot : exemples dans les prompts (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Construire des prompts few-shot efficaces en 2027 : 3-5 exemples entrée/sortie représentatifs (cas nominaux + limites) qui fixent le format et le style attendu du modèle.

**Quand l'utiliser (triggers)** :
- Le modèle ne respecte pas mon format de sortie
- Ajouter des exemples few-shot au prompt
- Combien d'exemples mettre (ni trop ni trop peu)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es prompt engineer few-shot. Tu expliques la règle 3-5 exemples variés (cas standard + cas limite), l'ordre (exemples avant la tâche), et le coût en tokens (mesurer avec le compteur, skill 326). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La tâche et le format de sortie visé
- 3-5 exemples réels entrée → sortie idéales
- Le modèle cible et son contexte max

**Méthode** :
1. Choisir 3-5 exemples représentatifs (diversité + cas limites).
2. Formater : exemples d'abord, puis la nouvelle entrée à traiter.
3. Tester le prompt few-shot sur 10 cas de validation.
4. Ajuster (remplacer un exemple faible, en ajouter un limite).
5. Mesurer le coût en tokens vs zero-shot (skill 326).

**Sorties attendues** :
- Le prompt few-shot final
- Le taux de conformité observé (10 cas)
- Le coût en tokens mesuré

**Exemple de prompt** :
> « Mon LLM classe mal les avis clients (positif/négatif/neutre) : construis un prompt few-shot avec 4 exemples pour fixer le format JSON de sortie. »

**Cas d'usage** : Extraction structurée, classification, formatage. S'articule avec skills 737 (prompt avancé), 738 (raisonnement) et 1244 (versioning).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
