---
num: 1686
nom: "Gaia-X niveau 3 : souveraineté pleine vs CLOUD Act (2027)"
emoji: "🇪🇺"
domaine: "Juridique"
signal: "Choisir un fournisseur Gaia-X niveau 3 en 2027 pour la souveraineté pleine : siège dans l'UE, opéré sous droit européen, à l'abri des prétentions extraterritoriales (CLOUD Act US) — niveaux 1-3 (3 = pleine souveraineté), 180+ espaces de données sectoriels en 2026, certification via le Digital Clearing House (GXDCH). Utilise pour les données sensibles (santé, industrie, admin) en UE. N'utilise pas pour des données publiques."
mot_cle: "Gaia-X niveau 3 souveraineté pleine siège UE droit européen CLOUD Act 2027 certification GXDCH"
nom_court: "Gaia-X N3"
branche: "D29"
synonymes: ["fournisseur Gaia-X niveau 3 = siège UE, droit UE, hors CLOUD Act", "180 espaces de données sectoriels Gaia-X en 2026 (santé, auto, énergie)", "certification via le Digital Clearing House (GXDCH) 2027"]
cross_refs: [1685, 924, 722]
tags: ["2027"]
depends_on: [1685]
---

## 1686. 🇪🇺 Gaia-X niveau 3 : souveraineté pleine vs CLOUD Act (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Choisir un fournisseur certifié Gaia-X niveau 3 en 2027 (siège UE, opéré sous droit européen, hors CLOUD Act US) pour les données sensibles : vérifier le niveau via le Digital Clearing House (GXDCH), rejoindre un espace de données sectoriel (180+ en 2026 : santé, auto, énergie).

**Quand l'utiliser (triggers)** :
- notre fournisseur a un label Gaia-X mais est soumis au CLOUD Act (niveau 1-2)
- vérifier le niveau 3 réel via le GXDCH avant contrat
- rejoindre l'espace de données santé Gaia-X en 2027

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es juriste souveraineté. Tu expliques les 3 niveaux Gaia-X (1: adhésion, 2: conformité renforcée + contrôles, 3: siège UE + droit UE + immunité extraterritoriale), la certification GXDCH, et le piège : un acteur US avec label Gaia-X reste soumis au CLOUD Act (vérifier le niveau 3). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les fournisseurs candidats et leur niveau Gaia-X
- Les données (sensibles = niveau 3 requis)
- Le secteur (espace de données sectoriel)

**Méthode** :
1. Vérifier le niveau du fournisseur sur le registre GXDCH (pas juste le logo) : niveau 3 = siège UE + droit UE + pas de CLOUD Act.
2. Données sensibles (santé 1668? non — 1584 RGPD, industrie, admin) → niveau 3 obligatoire (CADA 1685).
3. Rejoindre l'espace de données sectoriel Gaia-X du domaine (santé, énergie, mobilité : 180+ en 2026) pour l'interopérabilité.
4. Contrat : niveau 3 exigé + audit annuel + exit (Data Act 1671) + chiffrement clés client (1650? non 506).
5. Veille : Gaia-X a des retards (2026) mais le cadre juridique (Data Act, CADA) progresse.

**Sorties attendues** :
- Le fournisseur niveau 3 vérifié (GXDCH) pour les données sensibles
- L'espace de données sectoriel rejoint (interopérabilité)
- Le contrat avec niveau 3 + audit + exit (1671)

**Exemple de prompt** :
> « Notre hébergeur a un logo Gaia-X mais est une filiale US (CLOUD Act) : vérifie le niveau réel au GXDCH (besoin niveau 3), sinon passe chez un acteur purement UE (OVHcloud niveau 3) pour nos données santé, contrat avec audit + exit (1671). »

**Cas d'usage** : Données sensibles UE, marchés publics. S'articule avec skills 1685 (CADA), 924 (hébergement UE), 722 (souveraineté IA) et 1671 (Data Act).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
