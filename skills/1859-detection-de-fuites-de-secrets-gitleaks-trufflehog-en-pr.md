---
num: 1859
resume: "Détecter les fuites de secrets (clés cloud, tokens, clés privées) avec gitleaks/trufflehog en pre-commit (1403) et CI (scan historique 1413) — et en cas de fuite : révoquer (1855) + purger l'historique git. Étape 1 : Pre-commit : gitleaks protect --staged (bloque le commit si secret détecté)."
date_ajout: "2026-11"
nom: "Détection de fuites de secrets (gitleaks, trufflehog) en pre-commit et CI"
emoji: "🕵️"
domaine: "Sécurité"
signal: "Détecter les secrets commités par erreur : gitleaks ou trufflehog en pre-commit (1403) ET en CI (1413, scan historique complet) : détectent clés AWS, tokens GitHub, clés privées, mots de passe (regex + entropie + validateurs officiels des providers). Si fuite détectée : bloquer le commit/PR + RÉVOQUER immédiatement le secret (rotation 1855) + purger l'historique git (BFG/filter-repo). N'utilise pas 'ça n'arrive qu'aux autres'."
mot_cle: "gitleaks trufflehog détection fuite secrets pre-commit CI scan historique entropie clés AWS tokens GitHub révocation rotation purge historique BFG filter-repo"
nom_court: "Détection fuites"
branche: "D23"
synonymes: ["gitleaks en pre-commit (1403) : bloque un commit avec une clé AWS", "trufflehog en CI : scan de tout l'historique git (pas que le dernier commit)", "fuite détectée : révoquer le secret immédiatement (1855) + purger l'historique (BFG)"]
cross_refs: [1403, 1413, 1855]
tags: ["2027"]
depends_on: [1413]
---

## 1859. 🕵️ Détection de fuites de secrets (gitleaks, trufflehog) en pre-commit et CI

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Détecter les fuites de secrets (clés cloud, tokens, clés privées) avec gitleaks/trufflehog en pre-commit (1403) et CI (scan historique 1413) — et en cas de fuite : révoquer (1855) + purger l'historique git.

**Quand l'utiliser (triggers)** :
- une clé AWS a été committée par erreur : gitleaks la bloque en pre-commit
- scan historique complet en CI (trufflehog) : trouver les fuites des 2 ans passés
- procédure fuite : révoquer -> notifier -> purger historique (BFG) -> postmortem 1768

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es responsable sécurité DevSecOps. Tu installes gitleaks en pre-commit (config .gitleaks.toml) et trufflehog en CI sur tout l'historique, et tu documentes la procédure d'urgence (révoquer + purger + postmortem 1768). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- gitleaks/trufflehog
- Le pre-commit (1403) + CI (1413)
- La procédure d'urgence documentée

**Méthode** :
1. Pre-commit : gitleaks protect --staged (bloque le commit si secret détecté).
2. CI : trufflehog git file://. --since-commit=... ou scan complet hebdo (historique).
3. Règles custom : patterns internes (clés internes sk-...), allowlist pour les faux positifs (ex. exemples de docs).
4. Procédure fuite : 1) révoquer le secret (1855), 2) notifier RSSI/DPO si PII (1839), 3) purger l'historique (git filter-repo/BFG), 4) postmortem blameless (1768).

**Sorties attendues** :
- gitleaks en pre-commit + trufflehog en CI actifs
- 0 secret dans l'historique (scan clean)
- La procédure de fuite documentée et testée (tabletop 1769)

**Exemple de prompt** :
> « Dev commit une clé AWS AKIA... : gitleaks pre-commit bloque ('AWS key detected'), le dev la retire, met le secret dans Vault (1852) + ESO (1854) ; scan hebdo trufflehog : historique clean (la clé a été révoquée dans l'heure). »

**Cas d'usage** : Prévention fuites. S'articule avec skills 1403, 1413, 1855, 1857, 1852.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
