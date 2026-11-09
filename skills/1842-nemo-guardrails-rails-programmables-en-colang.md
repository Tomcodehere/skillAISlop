---
num: 1842
resume: "Programmer des rails de sécurité LLM avec NeMo Guardrails (Colang) : flux de dialogue contrôlés, détection jailbreak, self-check — en prenant en compte le disclaimer beta de NVIDIA (hardening + tests adversariaux requis). Étape 1 : Écrire les flows Colang : ex. define user ask about product -supérieur à bot respond product info ; tout le reste -supérieur à refuse poliment."
date_ajout: "2026-11"
nom: "NeMo Guardrails : rails programmables en Colang"
emoji: "🧨"
domaine: "Data & IA"
signal: "Utiliser NVIDIA NeMo Guardrails (Apache 2.0) pour des rails programmables en Colang (DSL) : définir les flux de dialogue autorisés, jailbreak heuristics, self-check, intégration LlamaGuard/Presidio. ATTENTION : NVIDIA déconseille la prod 'as-is' (beta) — hardening requis (rate limiting, isolation, tests adversariaux 1847). Telemetry : ping anonyme à NVIDIA (désactivable). N'utilise pas sans le disclaimer beta pris en compte."
mot_cle: "NeMo Guardrails NVIDIA Colang DSL rails programmables jailbreak self-check beta disclaimer prod hardening"
nom_court: "NeMo Guardrails"
branche: "D14"
synonymes: ["définir les flux de conversation autorisés en Colang (NeMo Guardrails)", "NeMo Guardrails est beta : NVIDIA déconseille la prod as-is (hardening requis)", "désactiver la télémétrie anonyme NeMo (ping NVIDIA)"]
cross_refs: [1841, 1844, 1846]
tags: ["2027"]
depends_on: [1841]
---

## 1842. 🧨 NeMo Guardrails : rails programmables en Colang

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Programmer des rails de sécurité LLM avec NeMo Guardrails (Colang) : flux de dialogue contrôlés, détection jailbreak, self-check — en prenant en compte le disclaimer beta de NVIDIA (hardening + tests adversariaux requis).

**Quand l'utiliser (triggers)** :
- définir en Colang : le bot ne répond que sur le support produit
- jailbreak heuristics + self-check output (NeMo)
- le disclaimer beta NVIDIA : quelles précautions avant la prod

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es ingénieur IA sécurité. Tu écris les rails en Colang (config.yml + .co flows), tu intègres LlamaGuard (1844) et Presidio (1846), et tu appliques le hardening obligatoire (rate limit, tests garak 1847) avant prod. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- NeMo Guardrails (pip install nemoguardrails)
- Le LLM à protéger
- Les flux métier autorisés

**Méthode** :
1. Écrire les flows Colang : ex. define user ask about product -> bot respond product info ; tout le reste -> refuse poliment.
2. Rails : input (jailbreak), dialog (flux), output (self-check + LlamaGuard 1844 + PII Presidio 1846).
3. Hardening prod : rate limiting, timeout, tests adversariaux (garak 1847), télémétrie désactivée.
4. Déployer derrière l'AI gateway (1800) pour le routing + budgets.

**Sorties attendues** :
- Les rails Colang déployés (dialog contrôlé)
- Le hardening appliqué (rate limit + tests 1847)
- La télémétrie désactivée

**Exemple de prompt** :
> « Bot support : Colang autorise uniquement les sujets produit/pricing ; un jailbreak 'ignore tes instructions' est bloqué par le rail input, le output self-check refuse la réponse hors sujet — testé avec 200 attaques garak (1847), 0 succès. »

**Cas d'usage** : Dialogue contrôlé. S'articule avec skills 1841, 1844, 1846, 1847.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
