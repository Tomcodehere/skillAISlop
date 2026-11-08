---
num: 1830
date_ajout: "2026-11"
nom: "SBOM et conformité réglementaire (CRA, contrats clients)"
emoji: "⚖️"
domaine: "Juridique"
signal: "Préparer la conformité SBOM exigée par le Cyber Resilience Act (CRA, en vigueur progressivement) et les questionnaires clients sécurité : SBOM machine-readable (CycloneDX/SPDX) livré avec chaque release, VEX pour les CVE non applicables (1826), processus de divulgation vulnérabilités (VDP), preuves SSDF (CDXA 1825). Le CRA rend le SBOM quasi obligatoire pour les produits avec éléments numériques. N'utilise pas un SBOM obsolète ou incomplet pour un contrat."
mot_cle: "CRA Cyber Resilience Act SBOM conformité réglementaire 2027 contrats clients questionnaire sécurité VDP divulgation CVE CDXA"
nom_court: "SBOM conformité"
branche: "D29"
synonymes: ["le CRA européen exige un SBOM pour notre produit : quoi livrer (CycloneDX + VEX + VDP)", "questionnaire client sécurité : fournir SBOM + attestations SSDF + processus VDP", "CRA en vigueur : calendrier et amendes si pas de SBOM/VDP"]
cross_refs: [1821, 1825, 1826]
tags: ["2027"]
depends_on: [1821]
---

## 1830. ⚖️ SBOM et conformité réglementaire (CRA, contrats clients)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Préparer la conformité SBOM du Cyber Resilience Act et des contrats clients : SBOM CycloneDX livré à chaque release, VEX (1826), attestations SSDF (CDXA 1825), processus VDP documenté.

**Quand l'utiliser (triggers)** :
- un client exige le SBOM de la dernière release + le VDP
- le CRA s'applique à notre produit : calendrier et obligations
- notre processus de divulgation de vulnérabilités (VDP) à documenter

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es responsable conformité / juridique sécurité. Tu industrialises la livraison du SBOM (1821) + VEX (1826) + CDXA (1825) à chaque release, tu documentes le VDP (contact security@, délais de réponse, CVE -> correctif), et tu traces les exigences CRA (calendrier, amendes). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les releases signées (1821-1825)
- Le texte CRA applicable au produit
- Les questionnaires clients types

**Méthode** :
1. À chaque release : livrer SBOM CycloneDX + SPDX + VEX + attestations CDXA signées (bundle vérifiable offline).
2. Documenter le VDP : security.txt (RFC 9116), contact, délais (ex. 90 j pour correctif), canal privé de signalement.
3. Mapper les obligations CRA : SBOM, gestion des vulnérabilités, déclaration incidents 24 h — calendrier d'application.
4. Répondre aux questionnaires avec les artifacts produits automatiquement.

**Sorties attendues** :
- Le package conformité livré par release (SBOM+VEX+CDXA+VDP)
- Le VDP documenté (security.txt, délais, canal)
- La matrice CRA (obligations, échéances, responsables)

**Exemple de prompt** :
> « Release v2.1 : livraison automatique SBOM CycloneDX (412 composants) + VEX (390 not_affected justifiés) + CDXA SSDF signé + security.txt (VDP, réponse sous 10 j) — le client valide le questionnaire sécurité en 1 j. »

**Cas d'usage** : Conformité réglementaire. S'articule avec skills 1821, 1825, 1826, 1822.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
