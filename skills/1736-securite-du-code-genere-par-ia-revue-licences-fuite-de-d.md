---
num: 1736
date_ajout: "2026-11"
nom: "Securite du code genere par IA : revue, licences, fuite de donnees"
emoji: "🛡"
domaine: "Sécurité"
signal: "Sécuriser le code généré par IA en 2027 (92 % des devs utilisent un assistant, blindspot n°1 OWASP 2026 1646) : revue humaine systématique des PR IA (1401), SAST en CI (1658), jamais de secrets/données perso dans les prompts (1440), licence du code généré vérifiée (1177), outil choisi selon la résidence du code (Windsurf/Devin HIPAA-FedRAMP, DeepSeek self-host 1633, autres = serveurs tiers), pas d'upload de code propriétaire sur des outils gratuits. N'utilise pas l'IA pour du code critique sans revue."
mot_cle: "sécurité code généré IA 2027 revue PR 1401 SAST CI 1658 secrets prompts 1440 licence 1177 résidence code HIPAA self-host"
nom_court: "Code IA sûr"
branche: "D23"
synonymes: ["mon code part sur les serveurs de l'outil IA gratuit (fuite)", "revue systématique des PR générées par IA (1401) + SAST (1658)", "licence du code généré (1177) + pas de secrets dans les prompts (1440)"]
cross_refs: [1646, 1401, 1658]
tags: ["2027"]
depends_on: [1646]
---

## 1736. 🛡 Securite du code genere par IA : revue, licences, fuite de donnees (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Sécuriser le code généré par IA en 2027 (92 % des devs concernés, blindspot OWASP n°1) : revue humaine des PR IA (1401) + SAST en CI (1658), jamais de secrets/données perso dans les prompts (1440), licence vérifiée (1177), outil choisi selon la résidence du code (HIPAA/self-host 1633), pas de code proprio sur les outils gratuits.

**Quand l'utiliser (triggers)** :
- mon collègue a collé notre code interne dans ChatGPT gratuit
- revue de PR générée par IA : quoi vérifier (1401 + SAST 1658)
- outil IA conforme HIPAA/FedRAMP (Windsurf/Devin) pour le code sensible

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es RSSI / tech lead. Tu écris la politique : outil autorisé par classe de code (public → gratuit OK ; interne → outil entreprise ; sensible/régulé → HIPAA/self-host 1633), jamais de secrets/PII dans les prompts (1440), revue humaine + SAST (1658) obligatoires, licence du code généré (1177). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les classes de code (public/interne/sensible)
- Les outils autorisés par classe
- La CI (SAST 1658)

**Méthode** :
1. Politique : code public → outils gratuits OK ; code interne → outil entreprise (Copilot Business, contrat DPA 189) ; code sensible/régulé → Windsurf/Devin (HIPAA/FedRAMP) ou self-host (DeepSeek 1633, vLLM 1471) ; jamais de code proprio sur un outil gratuit grand public.
2. Prompts : jamais de secrets, clés API, données perso clients dans les prompts (DLP 1440, masque auto).
3. Revue : toute PR avec code IA est taguée, revue humaine obligatoire (1401) + SAST semgrep (1658) + SCA (1645) en CI, bloquant.
4. Licence : le code généré hérite des licences du training data — vérifier avec le juridique (1177), préférer les outils avec indemnisation (Copilot Business).
5. Métriques : % de PR IA relues, vulnérabilités trouvées en SAST, incidents fuite (objectif 0).

**Sorties attendues** :
- La politique 'outil IA par classe de code' publiée et appliquée
- Les PR IA taguées + revue (1401) + SAST/SCA bloquants (1658/1645)
- Le dashboard : % PR IA relues, vulnérabilités, 0 incident fuite

**Exemple de prompt** :
> « Un dev a collé du code interne dans ChatGPT gratuit : publie la politique 2027 (outil selon classe de code : public→gratuit OK, interne→Copilot Business DPA, sensible→HIPAA/self-host 1633), jamais de secrets dans les prompts (1440), PR IA = revue 1401 + SAST 1658 bloquant, licence vérifiée (1177). »

**Cas d'usage** : Toute équipe utilisant l'IA pour coder. S'articule avec skills 1646 (OWASP 2026), 1401 (review), 1658 (DevSecOps), 1440 (PII), 1177 (licences).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
