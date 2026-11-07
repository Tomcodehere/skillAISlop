---
num: 1471
date_ajout: "2026-11"
nom: "Servir un LLM en API interne avec vLLM (2027)"
emoji: "⚡"
domaine: "Data & IA"
signal: "Déployer un LLM en API interne en 2027 avec vLLM (haut débit : continuous batching, PagedAttention, quantization AWQ/GPTQ) ou Ollama (simplicité) : endpoint /v1/chat/completions compatible OpenAI, load balancing, monitoring GPU, coûts. Utilise quand on self-host un modèle. N'utilise pas pour appeler un API cloud externe."
mot_cle: "vLLM servir LLM API interne self-host GPU PagedAttention"
nom_court: "vLLM self-host"
branche: "D14"
synonymes: ["déployer LLM interne vLLM 2027", "endpoint OpenAI compatible local", "Ollama vs vLLM débit"]
cross_refs: [1472, 903, 694]
tags: ["2027"]
depends_on: [1472]
---

## 1471. ⚡ Servir un LLM en API interne avec vLLM (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Déployer un LLM en API interne en 2027 avec vLLM (continuous batching, PagedAttention, quantization) : endpoint compatible OpenAI (/v1/chat/completions), monitoring GPU (latence, throughput, KV cache), et règles de coût.

**Quand l'utiliser (triggers)** :
- Self-hoster un LLM derrière une API OpenAI-compatible
- vLLM vs Ollama : débit et GPU
- monitorer le KV cache GPU vLLM

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es ML infra engineer. Tu donnes la commande de lancement vLLM (model, quantization, max-model-len, tensor-parallel), l'endpoint /v1/chat/completions, et le monitoring (GPU util, KV cache %, tokens/s, latence p95). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le modèle à servir (7B-70B, licence permissive)
- Le GPU disponible (VRAM)
- Le trafic attendu (requêtes/s)

**Méthode** :
1. Choisir le modèle (licence Apache/Mistral, taille vs VRAM) et la quantization (AWQ/GPTQ si besoin).
2. Lancer vLLM (docker) : --model, --quantization, --max-model-len, --tensor-parallel-size.
3. Tester l'endpoint /v1/chat/completions (compatible SDK OpenAI).
4. Bench : k6 (1415) sur l'API, mesurer tokens/s et p95.
5. Monitorer : GPU, KV cache, files d'attente, coûts électricité vs cloud.

**Sorties attendues** :
- L'API LLM interne vLLM opérationnelle
- Le benchmark (tokens/s, p95) vs cloud
- Le comparatif coût self-host vs API cloud

**Exemple de prompt** :
> « On paie 8k€/mois d'API cloud : déploie un LLM 13B en interne avec vLLM (endpoint OpenAI-compatible, bench tokens/s, comparatif coût). »

**Cas d'usage** : Self-hosting LLM, souveraineté, coûts à l'échelle. S'articule avec skills 1472 (GGUF local), 903 (SLM) et 694 (coût tokens).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
