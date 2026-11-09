---
num: 1846
resume: "Détecter et rédiger les PII (noms, emails, IBAN, CB) dans les flux LLM avec Presidio (Analyzer NER multilingue + Anonymizer) sur les rails input/output et en amont du RAG. Étape 1 : Presidio Analyzer : détecter les entités PII (PERSON, EMAIL, PHONE, IBAN, CREDIT_CARD...) avec score de confiance."
date_ajout: "2026-11"
nom: "Détection et redaction PII avec Microsoft Presidio"
emoji: "🕵️"
domaine: "Sécurité"
signal: "Détecter et rédiger les PII (noms, emails, téléphones, IBAN, cartes bancaires, adresses) dans les flux LLM avec Microsoft Presidio (open source) : Presidio Analyzer (NER + regex + contexte, multilingue FR) détecte, Presidio Anonymizer remplace par '[EMAIL]' ou masque partiel. Sur les rails input/output (1841) et en amont du RAG. Alternative : Llama Guard (1844) pour la classification globale. N'utilise pas de regex seules (faux négatifs sur les noms)."
mot_cle: "Presidio Microsoft détection PII redaction anonymizer NER regex multilingue email téléphone IBAN CB masque rails LLM RAG"
nom_court: "Presidio PII"
branche: "D23"
synonymes: ["détecter les emails/IBAN/cartes dans les prompts et réponses (Presidio Analyzer)", "rédiger : remplacer par [EMAIL] ou masquer partiel (Presidio Anonymizer)", "Presidio FR : NER français pour les noms/prénoms (pas que regex)"]
cross_refs: [1841, 1843, 1844]
tags: ["2027"]
depends_on: [1841]
---

## 1846. 🕵️ Détection et redaction PII avec Microsoft Presidio

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Détecter et rédiger les PII (noms, emails, IBAN, CB) dans les flux LLM avec Presidio (Analyzer NER multilingue + Anonymizer) sur les rails input/output et en amont du RAG.

**Quand l'utiliser (triggers)** :
- un utilisateur a collé son IBAN dans le chat : le détecter et rédiger
- RGPD : empêcher les PII d'entrer dans les logs LLM (1750 traces)
- Presidio Analyzer FR + Anonymizer (mask partiel) sur rail output 1841

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es ingénieur sécurité IA / DPO. Tu déploies Presidio (analyzer + anonymizer, modèle FR), tu branches sur les rails input/output (1841), et tu garantis que les traces OTel (1750) ne contiennent pas de PII. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Presidio (pip install presidio-analyzer/anonymizer)
- Le modèle de langue FR (spacy fr)
- Les rails LLM (1841)

**Méthode** :
1. Presidio Analyzer : détecter les entités PII (PERSON, EMAIL, PHONE, IBAN, CREDIT_CARD...) avec score de confiance.
2. Presidio Anonymizer : remplacer (REPLACE '[EMAIL]'), masquer (partial ****), ou hacher selon la politique (1839).
3. Brancher sur rail input (avant LLM) et output (avant retour utilisateur + avant logs 1750).
4. Tester : jeu de tests FR (noms composés, IBAN FR) avec précision/recall mesurés.

**Sorties attendues** :
- Les PII détectées/rédigées sur input et output
- Les logs/traces (1750) sans PII
- Le benchmark FR (précision/recall) documenté

**Exemple de prompt** :
> « Chatbot interne : un user colle 'mon IBAN FR76 3000...' — Presidio détecte IBAN (score 0.95), anonymise en 'FR76 ****' sur le rail output, et la trace OTel (1750) stocke la version rédactée — audit RGPD OK (1839). »

**Cas d'usage** : RGPD + LLM. S'articule avec skills 1841, 1843, 1844, 1440, 1839.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
