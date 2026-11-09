---
num: 1890
resume: "Combiner revue IA (résumé de PR, détection bugs/risques 1826 — Copilot 1741) et revue humaine ciblée (logique métier, sécurité, cas limites) avec une checklist (1401) et un SLA de revue inférieur à 4 h. Étape 1 : IA en premier : résumé de la PR + flags (bugs probables, risques sécu 1826, tests manquants 1885)."
date_ajout: "2026-11"
nom: "Revue de code assistée par IA + revue humaine ciblée"
emoji: "🤖"
domaine: "Développement"
signal: "Combiner revue de code IA (Copilot PR 1741, Cursor, etc. : résumé de la PR, détection de bugs/risques sécurité 1826, suggestions) et revue humaine ciblée (focus sur la logique métier, la sécurité, les cas limites — pas la syntaxe). Règles : l'IA en premier commentaire (rapide), l'humain relit ce que l'IA a signalé + la logique métier ; checklist de revue (1401). SLA de revue (ex. inférieur à 4 h ouvrées). N'utilise pas l'IA comme seul relecteur (hallucinations)."
mot_cle: "revue de code IA Copilot PR 1741 résumé détection bugs risques revue humaine ciblée logique métier checklist 1401 SLA revue hallucinations"
nom_court: "Revue IA+humaine"
branche: "D12"
synonymes: ["Copilot en revue de PR (1741) : résumé auto + détection de bugs/risques, puis humain sur la logique métier", "checklist de revue 1401 : sécurité 1826, perfs, cas limites, tests", "SLA revue inférieur à 4 h ouvrées : file de PR triée par ancienneté"]
cross_refs: [1741, 1401, 1826]
tags: ["2027"]
depends_on: [1741]
---

## 1890. 🤖 Revue de code assistée par IA + revue humaine ciblée

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Combiner revue IA (résumé de PR, détection bugs/risques 1826 — Copilot 1741) et revue humaine ciblée (logique métier, sécurité, cas limites) avec une checklist (1401) et un SLA de revue < 4 h.

**Quand l'utiliser (triggers)** :
- une PR de 800 lignes attend depuis 2 jours : résumé IA + revue humaine ciblée
- Copilot signale un risque sécurité (1826) dans la PR : le humain vérifie et corrige
- SLA : aucune PR en attente > 4 h ouvrées (tri par ancienneté)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es développeur / lead tech. Tu actives la revue IA sur les PR (résumé + risques), tu appliques la checklist (1401) en revue humaine (logique métier, sécurité, cas limites), et tu suis le SLA de revue. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La revue IA activée (1741)
- La checklist de revue (1401)
- Le SLA défini (ex. 4 h)

**Méthode** :
1. IA en premier : résumé de la PR + flags (bugs probables, risques sécu 1826, tests manquants 1885).
2. Humain : lit le résumé, vérifie les flags IA (pas de confiance aveugle), focus sur logique métier + cas limites + sécurité.
3. Checklist 1401 cochée avant merge ; quality gate 1885 vert.
4. SLA : file triée par ancienneté, alerte si > 4 h (1761).

**Sorties attendues** :
- Les PR relues (IA + humain) avec checklist cochée
- Le SLA de revue respecté (< 4 h)
- Les risques sécurité attrapés avant merge (1826)

**Exemple de prompt** :
> « PR de 800 lignes (refacto paiement) : Copilot (1741) résume + signale 2 risques (race condition, log de PII 1846) -> le humain vérifie ces 2 points + la logique métier des remises, corrige, merge en 3 h (SLA OK). »

**Cas d'usage** : Revue efficace. S'articule avec skills 1741, 1401, 1826, 1885, 1413.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
