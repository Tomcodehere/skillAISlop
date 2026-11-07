---
num: 1746
date_ajout: "2026-11"
nom: "Documentation auto du code par IA : docstrings, README, ADR (2027)"
emoji: "📖"
domaine: "Développement"
signal: "Générer et maintenir la doc du code avec l'IA en 2027 : docstrings auto (Copilot/Cursor 1735), README (312) et ADR (88) générés depuis le code + les PR, changelog (1578) auto depuis les commits (68), doc des API (180/87 OpenAPI) générée depuis les handlers. Revue humaine obligatoire (1401) — l'IA hallucine (1155). N'utilise pas sans revue."
mot_cle: "doc code auto IA 2027 docstrings README 312 ADR 88 changelog 1578 OpenAPI 180 générés revue humaine 1401 hallucination 1155"
nom_court: "Doc auto IA"
branche: "D15"
synonymes: ["générer les docstrings de tout un module (IA) + revue (1401)", "README/ADR générés depuis le code et les PR (88) automatiquement", "changelog auto depuis les commits conventionnels (68) 2027"]
cross_refs: [312, 88, 1578]
tags: ["2027"]
depends_on: [312]
---

## 1746. 📖 Documentation auto du code par IA : docstrings, README, ADR (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Générer et maintenir la doc du code avec l'IA en 2027 : docstrings, README (312), ADR (88), changelog (1578) depuis les commits (68), doc API (180/87) depuis les handlers — TOUJOURS avec revue humaine (1401) car l'IA hallucine (1155).

**Quand l'utiliser (triggers)** :
- générer les docstrings de ce module (IA) puis relire (1401)
- changelog automatique depuis les commits conventionnels (68)
- générer la doc OpenAPI (87) depuis mes handlers FastAPI/Express

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es dev / tech writer. Tu fais générer par l'agent (Cursor 1740 / Copilot 1741 / Cody 1744) les docstrings/README/ADR/changelog, puis tu relis chaque ligne (1401) en vérifiant les faits (noms de fonctions, comportements) contre le code — l'IA invente parfois (1155). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le code à documenter
- L'agent IA (1735)
- La revue humaine (1401)

**Méthode** :
1. Docstrings : sélectionner le module, prompt 'documente chaque fonction publique (params, return, exceptions, exemple)' → appliquer, puis relire ligne par ligne vs le code (1401).
2. README (312) : généré depuis le repo (install, usage, archi) + relu ; ADR (88) pour les décisions d'archi détectées dans les PR.
3. Changelog (1578) : généré depuis les commits conventionnels (feat:/fix: 68) par PR/release — relu.
4. Doc API (87/180) : générée depuis les handlers (OpenAPI), testée (exemples exécutables 822), publiée (1406).
5. Règle : jamais de doc IA publiée sans revue humaine (1401) + vérification des faits (1155 grounding).
6. CI : check que la doc est à jour (doc modifiée si code changé, 1715).

**Sorties attendues** :
- Les docstrings/README/ADR/changelog générés + relus (1401)
- La doc API (87) générée et testée (822) publiée (1406)
- La règle 'revue humaine obligatoire' + check CI doc-à-jour (1715)

**Exemple de prompt** :
> « Ce module de 800 lignes n'a aucune doc : fais générer les docstrings + README + ADR (88) par l'IA (Cursor 1740), relis chaque ligne vs le code (1401, l'IA hallucine 1155), check CI doc-à-jour (1715), publie (1406). »

**Cas d'usage** : Documentation de code maintenue. S'articule avec skills 312 (README), 88 (ADR), 1578 (changelog), 87 (OpenAPI), 1401 (revue), 1155 (hallucination).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
