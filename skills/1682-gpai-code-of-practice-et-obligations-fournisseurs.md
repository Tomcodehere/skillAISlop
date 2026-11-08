---
num: 1682
date_ajout: "2026-11"
nom: "GPAI : Code of Practice et obligations fournisseurs"
emoji: "📋"
domaine: "Juridique"
signal: "Se conformer en 2027 aux obligations GPAI (modèles d'IA à usage général, en vigueur depuis 2 août 2025, enforcement + amendes depuis 2 août 2026) : documentation technique, résumé public du contenu d'entraînement (droit d'auteur Directive 2026), Code of Practice (20+ signataires août 2026) pour les fournisseurs, évaluations + déclaration d'incidents graves pour les modèles à risque systémique. Utilise si vous développez/fournissez un modèle GPAI. N'utilise pas si vous êtes simple utilisateur (déployer)."
mot_cle: "GPAI 2027 Code of Practice documentation résumé entraînement copyright risque systémique déclaration incidents 24h"
nom_court: "GPAI"
branche: "D29"
synonymes: ["nous fournissons un modèle GPAI : obligations 2027 (Code of Practice)", "résumé public du dataset d'entraînement (droit d'auteur 2026)", "modèle à risque systémique : évaluation + incident grave déclaré sous 24 h"]
cross_refs: [1681, 1683, 1018]
tags: ["2027"]
depends_on: [1681]
---

## 1682. 📋 GPAI : Code of Practice et obligations fournisseurs (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Se conformer en 2027 aux obligations GPAI (fournisseurs de modèles à usage général) : documentation technique, résumé public du contenu d'entraînement (droit d'auteur), Code of Practice (signé par 20+ fournisseurs), et pour les modèles à risque systémique : évaluations, mesures de mitigation, déclaration des incidents graves (24 h).

**Quand l'utiliser (triggers)** :
- on publie un modèle open weights en 2027 : obligations GPAI ?
- Code of Practice GPAI signé (conformité volontaire mais attendue)
- incident grave sur notre modèle systémique : déclarer sous 24 h à l'AI Office

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es juriste IA modèles. Tu appliques le Chapter V : art 53 (doc technique + résumé training data + conformité droit d'auteur), art 55 (risque systémique : evals, red-team 37, incidents 24 h, cybersécurité), Code of Practice (transparence, copyright, safety). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le modèle GPAI développé (risque systémique ? > 10^25 FLOP)
- La documentation technique
- L'AI Office (déclarations)

**Méthode** :
1. Art 53 : documentation technique complète (architecture, training, capacités) + résumé PUBLIC du contenu d'entraînement (conformité Directive droit d'auteur 2026) + politique de refus des plaintes copyright.
2. Code of Practice (juillet 2026, 20+ signataires) : transparence, copyright, safety & security — le signer accélère la conformité.
3. Si risque systémique (art 51) : évaluation du modèle (benchmarks capacité dangereuse), mesures de mitigation, cybersécurité, déclaration des incidents graves à l'AI Office sous 24 h (modèle de rapport publié 11/2025).
4. En aval : fournir aux déployeurs (art 53(2)) les infos pour leurs propres obligations (1681).

**Sorties attendues** :
- La doc technique + le résumé public du training data conformes
- Le Code of Practice signé (si applicable)
- La procédure d'incident grave (24 h, AI Office) testée

**Exemple de prompt** :
> « On publie notre LLM open weights en 2027 : obligations GPAI (art 53 doc technique + résumé public du dataset d'entraînement conforme droit d'auteur 2026, Code of Practice signé) ; si risque systémique : evals + déclaration incidents 24 h (art 55). »

**Cas d'usage** : Fournisseurs de modèles GPAI. S'articule avec skills 1681 (calendrier), 1683 (amendes), 37 (red-team) et 1018 (éthique).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
