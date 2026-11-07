---
num: 1441
nom: "Cascade de modeles : router chaque tache au bon LLM (2027)"
emoji: "🔀"
domaine: "IA / Prompting"
signal: "Router chaque requête vers le bon modèle en 2027 (cascade) : tâche simple → petit modèle rapide/peu cher (SLM), tâche complexe → grand modèle, classification en amont (règles ou petit LLM), mesure du taux de routage. Utilise quand le coût/latence compte. N'utilise pas si un seul modèle suffit."
mot_cle: "cascade modèles router requête petit grand LLM coût"
nom_court: "Cascade LLM"
branche: "D14"
synonymes: ["petit modèle puis grand modèle", "router tâche au bon LLM", "réduire coût inférence cascade"]
cross_refs: [265, 694, 689]
tags: ["2027"]
depends_on: [689]
---

## 1441. 🔀 Cascade de modeles : router chaque tache au bon LLM (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Mettre en place une cascade de modèles en 2027 : classifier la requête (règles ou SLM) et la router vers le petit modèle (rapide, pas cher) ou le grand (complexe), avec mesure du taux et du coût économisé.

**Quand l'utiliser (triggers)** :
- Toutes mes requêtes vont sur GPT-4o, trop cher
- Router simple vers SLM, complexe vers gros modèle
- Cascade LLM : classifier en amont

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte d'inférence économique. Tu donnes le pattern (classificateur léger ou règles → SLM 3B pour 80 % des cas simples, fallback grand modèle), le calcul coût économisé (tokens × prix), et le taux de fallback à surveiller (< 20 %). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les types de requêtes et leur fréquence
- Les modèles disponibles (SLM local + cloud)
- Le budget et la latence cible

**Méthode** :
1. Classifier les requêtes : simples (résumé court, traduction) vs complexes (raisonnement, code).
2. Règles ou SLM en amont pour décider du modèle cible.
3. Envoyer 80 % vers le SLM (local ou API pas chère), fallback vers le grand modèle.
4. Mesurer : taux de fallback, coût total, latence p95, qualité (échantillon).
5. Ajuster les règles selon les erreurs du SLM.

**Sorties attendues** :
- Le routeur de modèles configuré
- Le calcul d'économie (avant/après)
- Le taux de fallback et la qualité constatée

**Exemple de prompt** :
> « Toutes nos requêtes partent sur le gros modèle (facture qui grimpe) : mets une cascade (SLM pour les tâches simples, fallback grand modèle, mesure le gain). »

**Cas d'usage** : Optimisation coût IA, latence, edge. S'articule avec skills 265 (coûts LLM), 694 (tokens) et 689 (choix LLM).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
