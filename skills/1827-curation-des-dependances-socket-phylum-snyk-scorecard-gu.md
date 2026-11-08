---
num: 1827
date_ajout: "2026-11"
nom: "Curation des dépendances : Socket, Phylum, Snyk, Scorecard, GUAC"
emoji: "🧹"
domaine: "Sécurité"
signal: "Curer les dépendances AVANT le merge (shift-left) : Socket.dev / Phylum analysent le comportement du paquet (typosquatting, install scripts malveillants, exfiltration) ; Snyk/Endor pour vulnérabilités + licences ; OpenSSF Scorecard évalue la santé du projet (branch protection, SAST, signed releases) ; GUAC agrège SBOM+SLSA+VEX en graphe. Bloquer le merge si score faible ou comportement malveillant. N'utilise pas qu'un scanner de CVE (il voit après coup)."
mot_cle: "curation dépendances Socket Phylum Snyk Endor OpenSSF Scorecard GUAC typosquatting install scripts merge bloqué"
nom_court: "Curation deps"
branche: "D23"
synonymes: ["bloquer un paquet malveillant avant le merge (Socket/Phylum comportement)", "OpenSSF Scorecard : santé du projet (signed releases, SAST, branch protection)", "GUAC : graphe SBOM + SLSA + VEX pour savoir si on est affecté"]
cross_refs: [1413, 1826, 1821]
tags: ["2027"]
depends_on: [1413]
---

## 1827. 🧹 Curation des dépendances : Socket, Phylum, Snyk, Scorecard, GUAC

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Curer les dépendances avant le merge : Socket/Phylum (comportement malveillant, typosquatting), Snyk/Endor (CVE/licences), OpenSSF Scorecard (santé du projet), GUAC (graphe d'impact) — bloquer le PR si risque.

**Quand l'utiliser (triggers)** :
- un paquet populaire a été remplacé par un typosquat (npm)
- bloquer le merge si le nouveau paquet a un install script qui exfiltre
- Scorecard < 5 sur un projet critique : ne pas l'adopter

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es responsable sécurité DevSecOps. Tu ajoutes un check CI (1413) sur les PR modifiant package.json/Cargo.toml/requirements : Socket ou Phylum en gate (block si comportement malveillant), Scorecard pour les nouvelles dépendances majeures. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les fichiers de dépendances
- Socket/Phylum/Snyk en CI
- La politique de score minimum

**Méthode** :
1. PR modifiant les deps : lancer socket scan / phylum analyze -> bloque si install script suspect, typosquat, ou CVE critique (1826).
2. Nouvelle dépendance majeure : OpenSSF Scorecard (api.scorecard.dev) — score < 5 = revue sécurité obligatoire.
3. GUAC en interne : graphe SBOM+provenance pour répondre 'sommes-nous affectés par la CVE X ?' en 1 requête.

**Sorties attendues** :
- Le gate CI sur les dépendances (block si malveillant)
- Les scores Scorecard des deps critiques documentés
- Le graphe GUAC pour l'impact analysis

**Exemple de prompt** :
> « PR ajoute left-pad2 (typosquat de left-pad) : Socket bloque le merge (comportement : install script qui poste des env vars) — 0 incident, revue sécurité faite avant. »

**Cas d'usage** : Shift-left sécurité deps. S'articule avec skills 1413, 1826, 1821, 1884 (Renovate).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
