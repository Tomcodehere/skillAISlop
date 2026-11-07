---
num: 1749
date_ajout: "2026-11"
nom: "Vibe coding responsable : quand l'IA code, quand l'humain code (2027)"
emoji: "⚖️"
domaine: "Développement"
signal: "Définir en 2027 ce que l'IA code et ce que l'humain garde : l'IA gère le boilerplate, les tests (1747), la doc (1746), les migrations mécaniques (1737) ; l'humain garde l'archi (88), la sécurité critique (1646), la revue (1401), le choix des algos sensibles (84), et la responsabilité légale. Règle : tout code IA = code relu (1401) + testé (1747) + SAST (1658), responsabilité humaine inchangée. N'utilise pas l'IA pour du code critique sans ces garde-fous."
mot_cle: "vibe coding responsable 2027 frontière IA/humain archi 88 sécurité 1646 revue 1401 tests 1747 SAST 1658 responsabilité humaine"
nom_court: "Vibe resp."
branche: "D1"
synonymes: ["qu'est-ce que l'IA peut coder en 2027 et qu'est-ce que je garde ?", "l'IA fait le boilerplate, moi l'archi (88) et la sécurité (1646)", "tout code IA = relu (1401) + testé (1747) + SAST (1658), responsabilité humaine"]
cross_refs: [540, 88, 1401]
tags: ["2027"]
depends_on: [540]
---

## 1749. ⚖️ Vibe coding responsable : quand l'IA code, quand l'humain code (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Définir la frontière IA/humain en 2027 (vibe coding responsable) : l'IA gère boilerplate, tests (1747), doc (1746), migrations (1737) ; l'humain garde l'architecture (88), la sécurité critique (1646), la revue (1401), la responsabilité — et tout code IA est relu+testé+SAST (1401/1747/1658).

**Quand l'utiliser (triggers)** :
- jusqu'où laisser l'IA coder en 2027 ?
- l'IA a introduit une faille de sécurité (code IA non relu 1401)
- qui est responsable du code IA en prod ? (l'humain, toujours)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es tech lead. Tu écris la charte : ce que l'IA fait (boilerplate, tests 1747, doc 1746, migrations 1737) vs ce que l'humain garde (archi 88, sécurité 1646, perfs 1618, revue 1401), et les 3 garde-fous obligatoires sur tout code IA (revue 1401, tests 1747, SAST 1658). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les pratiques actuelles (540 vibe coding)
- Les risques (1646 OWASP code IA)
- La politique entreprise (1736)

**Méthode** :
1. IA fait : boilerplate, CRUD, tests (1747), doc (1746), migrations mécaniques (1737), POC (1745) — toujours avec revue (1401).
2. Humain garde : architecture et choix tech (88 ADR), sécurité (auth 501, crypto 506, 1646), perfs (1618), correctness des algos métier (84), données perso (1440/1584), responsabilité légale.
3. 3 garde-fous sur 100 % du code IA : revue humaine (1401), tests auto + couverture CI (1747/1658), SAST/SCA bloquant (1658/1645).
4. Jamais d'IA sur : secrets (306), clés (1446), code de paiement critique sans double revue (1636 HITL), données perso (1440).
5. Formation équipe (201) : prompt engineering pour le code (737), limites des modèles (336 biais 1155).
6. Métriques : % code IA, bugs par source (IA vs humain 256), temps de revue (1401) — revue trimestrielle de la charte.

**Sorties attendues** :
- La charte vibe-coding responsable 2027 publiée (frontière IA/humain + 3 garde-fous)
- La formation équipe faite (201) + métriques (% code IA, bugs 256)
- La règle 'responsabilité humaine inchangée' dans le règlement interne

**Exemple de prompt** :
> « L'IA a introduit une faille (code non relu) : publie la charte 2027 — IA = boilerplate/tests/doc/migrations (1747/1746/1737), humain = archi (88)/sécurité (1646)/revue (1401) ; 3 garde-fous sur tout code IA (1401+1747+1658) ; jamais d'IA sur secrets (306) ou données perso (1440). »

**Cas d'usage** : Gouvernance du codage IA. S'articule avec skills 540 (vibe coding), 88 (ADR), 1646 (OWASP), 1401 (revue), 1747 (tests), 1658 (SAST).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
