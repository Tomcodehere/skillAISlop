---
num: 1844
resume: "Self-hoster un classifieur de sécurité LLM avec Llama Guard 3 (Meta, 1B/8B) : labelise input et output (injection, contenu dangereux) en local — pas d'API externe, pas de fuite de données, latence contrôlée. Étape 1 : Déployer Llama Guard 3 8B via vLLM (GPU) ou ollama (CPU, 1B)."
lang: "fr"
date_ajout: "2026-11"
nom: "Llama Guard 3 : classifieur judge self-hosté"
emoji: "🦸️"
domaine: "Data & IA"
signal: "Self-hoster un classifieur judge avec Llama Guard 3 (Meta, open weights, 1B ou 8B) : il labelise input/output selon une taxonomie de sécurité (violence, hate, sexuel, prompt injection...) — remplace les API de modération externes (coût, latence, confidentialité des données). S'exécute en local sur GPU ou CPU (1B). Le meilleur score AILuminate 2027. N'utilise pas le 1B pour des cas critiques (prendre le 8B)."
mot_cle: "Llama Guard 3 Meta classifieur judge self-hosté 1B 8B open weights labels sécurité input output AILuminate local GPU confidentialité"
nom_court: "Llama Guard"
branche: "D14"
synonymes: ["classifier les entrées/sorties LLM en local (Llama Guard 3 8B) sans API externe", "pas de données envoyées à une API de modération externe : Llama Guard self-hosté", "Llama Guard 3 1B rapide vs 8B précis : lequel selon le risque"]
cross_refs: [1841, 1843, 1845]
tags: ["2027"]
depends_on: [1841]
---

## 1844. 🦸️ Llama Guard 3 : classifieur judge self-hosté

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Self-hoster un classifieur de sécurité LLM avec Llama Guard 3 (Meta, 1B/8B) : labelise input et output (injection, contenu dangereux) en local — pas d'API externe, pas de fuite de données, latence contrôlée.

**Quand l'utiliser (triggers)** :
- classer les prompts/réponses en local sans API externe (Llama Guard 8B)
- données sensibles : pas d'appel à l'API OpenAI Moderation (fuite)
- 1B pour la latence, 8B pour la précision critique

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es ingénieur IA sécurité. Tu déploies Llama Guard (vLLM/ollama sur GPU), tu choisis 1B (latence) ou 8B (précision critique), et tu branches le verdict sur le rail input/output (1841). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Un GPU (ou CPU pour le 1B)
- vLLM/ollama
- La taxonomie de labels souhaitée

**Méthode** :
1. Déployer Llama Guard 3 8B via vLLM (GPU) ou ollama (CPU, 1B).
2. Appeler avant le LLM (input) et après (output) : le modèle renvoie des labels S1-S14 + 'safe'.
3. Décision : si label unsafe -> blocage (sync, rail input/output 1841) ou rework.
4. Benchmark : précision/recall sur un dataset adversarial (1847) avant prod.

**Sorties attendues** :
- Le judge déployé en local (1B ou 8B)
- Les verdicts branchés sur les rails (1841)
- Le benchmark précision/recall documenté

**Exemple de prompt** :
> « Chatbot interne avec données RH : Llama Guard 3 8B self-hosté labelise chaque échange (aucune donnée ne sort vers une API externe) — 0,4 % bloqués (injection/PII), latence +120 ms sur GPU. »

**Cas d'usage** : Modération locale/confidentielle. S'articule avec skills 1841, 1843, 1845, 1842.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
