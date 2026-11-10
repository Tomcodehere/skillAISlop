---
num: 1649
resume: "Se mettre en conformité en 2027 avec NIS2 (déclaration incident 24 h, gestion des risques, responsabilité dirigeants), DORA (finance : résilience testée, registre ICT, contrats fournisseurs avec exit 1672) et CMMC (défense US). Étape 1 : Vérifier le scope : NIS2 (18 secteurs, seuils taille), DORA (banques, assurances, infrastructures de marché), CMMC (contrats défense US)."
lang: "fr"
date_ajout: "2026-11"
nom: "NIS2, DORA et CMMC actifs : obligations"
emoji: "⚖️"
domaine: "Sécurité"
signal: "Se mettre en conformité en 2027 avec les régulations cyber actives en 2026 : NIS2 (entités essentielles/importantes UE : gestion des risques, déclaration d'incidents 24 h, responsabilité des dirigeants), DORA (finance : tests de résilience, registres ICT, contrats fournisseurs testés 1672), CMMC (défense US). Utilise pour les secteurs concernés. N'utilise pas pour une TPE hors scope."
mot_cle: "NIS2 DORA CMMC 2027 conformité obligations déclaration incident 24h résilience financière DORA"
nom_court: "NIS2/DORA"
branche: "D23"
synonymes: ["NIS2 : déclarer un incident sous 24 h, responsabilité dirigeant", "DORA banque/assurance : tests de résilience + registres fournisseurs ICT", "CMMC défense US : certification niveau 2"]
cross_refs: [754, 1454, 1672]
tags: ["2027"]
depends_on: [754]
---

## 1649. ⚖️ NIS2, DORA et CMMC actifs en 2026-2027 : obligations (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Se mettre en conformité en 2027 avec NIS2 (déclaration incident 24 h, gestion des risques, responsabilité dirigeants), DORA (finance : résilience testée, registre ICT, contrats fournisseurs avec exit 1672) et CMMC (défense US).

**Quand l'utiliser (triggers)** :
- nous sommes entité essentielle NIS2 : quelles obligations en 2027 ?
- DORA : tester le PRA et les contrats fournisseurs ICT
- déclarer un incident de sécurité sous 24 h (NIS2)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es RSSI conformité. Tu fais le gap analysis : NIS2 (mesures de sécurité, incident 24 h, registre, amendes jusqu'à 10 M€ ou 2 % CA), DORA (RTO/RPO testés 1454, registre fournisseurs, contrats avec clauses exit 1672), CMMC (certification niveaux). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le secteur et la taille (dans le scope NIS2/DORA ?)
- Les politiques de sécurité existantes
- Les contrats fournisseurs ICT

**Méthode** :
1. Vérifier le scope : NIS2 (18 secteurs, seuils taille), DORA (banques, assurances, infrastructures de marché), CMMC (contrats défense US).
2. NIS2 : politique de sécurité, gestion des risques, déclaration incident 24 h (procédure testée 1454), registre des incidents, amendes.
3. DORA : identifier les fonctions ICT critiques, RTO/RPO, tests de résilience annuels (1454), registre des fournisseurs ICT, contrats avec exit (1672).
4. CMMC : niveau 2 (CUI) → auto-évaluation ou audit, 110 contrôles NIST 800-171.
5. Plan de remédiation + échéances + responsable conformité nommé.

**Sorties attendues** :
- Le gap analysis NIS2/DORA/CMMC avec plan de remédiation
- La procédure de déclaration d'incident 24 h testée (1454)
- Le registre des fournisseurs ICT (DORA) à jour

**Exemple de prompt** :
> « Nous sommes une banque (DORA) et entité essentielle NIS2 : gap analysis 2027 — déclaration incident 24 h testée (1454), RTO/RPO + tests de résilience, registre fournisseurs ICT avec exit (1672), plan de remédiation. »

**Cas d'usage** : Secteurs régulés. S'articule avec skills 754 (incidents), 1454 (tabletop), 1672 (exit cloud) et 1459 (ISO 27001).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
