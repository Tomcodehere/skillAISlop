---
num: 1843
date_ajout: "2026-11"
nom: "Guardrails AI : validators composables en Python"
emoji: "🧩"
domaine: "Data & IA"
signal: "Composer des guardrails avec Guardrails AI (Apache 2.0) : bibliothèque de validators réutilisables en Python sur input ET output — validation JSON schema (1427), détection PII/redaction, toxicité, vérification de faits, regex. S'exécute dans le code (pas de LLM judge à chaque requête = pas de latence +400 ms). N'utilise pas pour la logique conversationnelle multi-tours (voir NeMo 1842)."
mot_cle: "Guardrails AI validators Python composables JSON schema PII redaction toxicité vérification faits sans LLM judge latence"
nom_court: "Guardrails AI"
branche: "D14"
synonymes: ["valider la sortie JSON de mon LLM avec un schéma (Guardrails AI, pas de LLM judge)", "redacter les PII dans la réponse (validator Guardrails AI)", "guardrails sans latence +400 ms : validators en code, pas de LLM judge"]
cross_refs: [1841, 1427, 1846]
tags: ["2027"]
depends_on: [1841]
---

## 1843. 🧩 Guardrails AI : validators composables en Python

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Composer des guardrails avec Guardrails AI (validators Python réutilisables sur input/output : JSON schema, PII, toxicité, faits) — sans LLM judge à chaque requête, donc sans latence ajoutée.

**Quand l'utiliser (triggers)** :
- la sortie du LLM doit être un JSON valide (schéma) : validator Guardrails AI
- redacter automatiquement les emails/téléphones dans la réponse
- éviter le LLM judge (+400-1200 ms) : validators déterministes en code

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es ingénieur IA. Tu sélectionnes les validators adaptés (json_schema, pii, toxicity, similar_to_document), tu les chaînes sur input et/ou output, et tu mesures la latence (ms, pas de LLM judge). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Guardrails AI (pip)
- Les validators nécessaires
- Les points d'application (input/output)

**Méthode** :
1. Choisir les validators : input (pii, jailbreak regex), output (json_schema 1427, toxicity, pii redaction 1846).
2. Les chaîner : guard = Guard() + validators, appelée dans le code avant/après l'appel LLM.
3. Rework on fail : si validation échoue, re-prompt ou fallback (pas de réponse invalide).
4. Mesurer la latence ajoutée (ms) et le taux de blocage.

**Sorties attendues** :
- Les validators déployés (input/output)
- La latence ajoutée mesurée (ms)
- Le taux de blocage/rework

**Exemple de prompt** :
> « API qui retourne du JSON : validator json_schema sur la sortie — si le LLM renvoie du texte libre, rework automatique (re-prompt avec le schéma), 0 réponse invalide livrée, latence +12 ms seulement. »

**Cas d'usage** : Validation déterministe. S'articule avec skills 1841, 1427, 1846, 1844.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
