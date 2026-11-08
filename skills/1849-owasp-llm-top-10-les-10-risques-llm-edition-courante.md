---
num: 1849
date_ajout: "2026-11"
nom: "OWASP LLM Top 10 : les 10 risques LLM (édition courante)"
emoji: "🔐"
domaine: "Sécurité"
signal: "Connaître l'OWASP LLM Top 10 édition 2025 (réorganisée vs v1.1) : LLM01 Prompt Injection (direct ET indirect — cf 1845), LLM02 Sensitive Information Disclosure, LLM03 Supply Chain (cf 1821-1830), LLM04 Data/model poisoning, LLM05 Improper Output Handling, LLM06 Excessive Agency (l'agent appelle trop d'outils — cf 1850), LLM07 System Prompt Leakage, LLM08 Vector/embedding weaknesses (RAG), LLM09 Misinformation, LLM10 Unbounded Consumption (coût — cf 1800 budgets). Chaque risque a ses mitigations documentées."
mot_cle: "OWASP LLM Top 10 2025 LLM01 prompt injection LLM06 excessive agency LLM03 supply chain mitigations"
nom_court: "OWASP LLM10"
branche: "D23"
synonymes: ["OWASP LLM Top 10 2025 : la liste à jour (LLM01 injection, LLM06 excessive agency)", "LLM06 excessive agency : l'agent appelle des outils sans contrôle (cf 1850)", "LLM10 unbounded consumption : plafonner les appels (budgets gateway 1800)"]
cross_refs: [1845, 1850, 1841]
tags: ["2027"]
depends_on: [1841]
---

## 1849. 🔐 OWASP LLM Top 10 : les 10 risques LLM (édition courante)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Appliquer l'OWASP LLM Top 10 (édition 2025) : LLM01 injection (1845), LLM03 supply chain (1821+), LLM06 excessive agency (1850), LLM07 fuite de system prompt, LLM10 consommation non bornée (budgets 1800) — avec leurs mitigations.

**Quand l'utiliser (triggers)** :
- notre checklist sécurité LLM date de 2024 (v1.1) : mettre à jour avec l'édition 2025
- LLM06 : l'agent a supprimé une table (excessive agency) -> gating 1850
- LLM10 : boucle infinie LLM a coûté 5 000 € -> budget gateway 1800

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es RSSI / ingénieur sécurité IA. Tu parcours les 10 risques OWASP 2025, tu associes chaque risque à sa mitigation dans notre stack (1845, 1850, 1821, 1800, 1846...) et tu tiens une matrice risque/mitigation à jour. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'OWASP LLM Top 10 2025
- Notre stack LLM (1800, 1841+)
- La matrice de risques existante

**Méthode** :
1. LLM01 injection -> 1845 ; LLM03 supply chain -> 1821-1830 ; LLM06 agency -> 1850 ; LLM07 fuite system prompt -> canary (1845) + pas dans les logs ; LLM10 coût -> budgets 1800 + burn 1757.
2. Pour chaque risque : menace, mitigation déployée, owner, statut (OK/à faire).
3. Revue trimestrielle avec la sortie des nouvelles éditions OWASP.

**Sorties attendues** :
- La matrice OWASP 2025 -> mitigations à jour
- Les risques sans mitigation identifiés (plan d'action)
- La revue trimestrielle planifiée

**Exemple de prompt** :
> « Audit OWASP 2025 : LLM06 trouvé non couvert (agent avec 15 tools sans gating) -> déploiement du tool-permission gating (1850) en 1 sprint ; LLM10 -> spend limit 500 €/mois sur la gateway (1800). »

**Cas d'usage** : Cadre sécurité LLM. S'articule avec skills 1845, 1850, 1841, 1821, 1800, 1846.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
