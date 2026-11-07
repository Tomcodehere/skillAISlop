---
num: 1440
nom: "Detecter PII et donnees sensibles dans les prompts (2027)"
emoji: "🙈"
domaine: "IA / Prompting"
signal: "Détecter et bloquer les données personnelles (PII) avant envoi à un LLM externe en 2027 : NER/regex (email, téléphone, IBAN, CNI), masquage automatique, avertissement, journal, politique d'entreprise. Utilise quand des utilisateurs collent des données sensibles dans un chatbot. N'utilise pas pour l'anonymisation de datasets (voir Data)."
mot_cle: "détecter PII données personnelles prompt LLM masquage"
nom_court: "PII guardrail"
branche: "D14"
synonymes: ["bloquer données perso avant LLM", "masquer email IBAN CNI automatiquement", "guardrail PII entreprise 2027"]
cross_refs: [195, 1226, 189]
tags: ["2027"]
depends_on: [195]
---

## 1440. 🙈 Detecter PII et donnees sensibles dans les prompts (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Mettre en place un guardrail PII en 2027 : détecter (NER + regex : email, tél, IBAN, CNI, adresse) les données personnelles dans les prompts, les masquer ou bloquer, et journaliser sans stocker la PII.

**Quand l'utiliser (triggers)** :
- Un user colle son IBAN dans le chatbot
- Masquer automatiquement les données perso avant l'API LLM
- Politique PII entreprise sur les prompts

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es responsable protection des données (DP) technique. Tu proposes le pipeline (détection NER/presidio + regex FR, action : masquer/bloquer/avertir, log anonymisé), et tu rappelles le RGPD : minimisation + registre des traitements. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les types de PII à bloquer (RGPD : identité, coordonnées, bancaires, santé)
- Le point d'entrée (chatbot interne, API externe ?)
- La politique : masquer ou bloquer ?

**Méthode** :
1. Lister les PII à détecter (email, tél FR, IBAN, CNI, Sécu, adresse, IP).
2. Déployer la détection (Presidio/NER + regex) en entrée de prompt.
3. Action : masquer (****) + avertir l'utilisateur, ou bloquer si critique.
4. Journaliser l'incident sans stocker la PII (hash).
5. Revoir mensuellement les nouvelles tentatives (logs agrégés).

**Sorties attendues** :
- Le guardrail PII actif en entrée
- La liste des patterns de détection
- Le log d'incidents anonymisé + revue mensuelle

**Exemple de prompt** :
> « Nos users collent des IBAN/CNI dans le support IA externe : mets un guardrail PII (détection, masquage auto, alerte, log anonymisé RGPD). »

**Cas d'usage** : Chatbots internes/externes, conformité RGPD, DPO. S'articule avec skills 195 (anti-injection), 1226 (flux données personnels) et 189 (RGPD).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
