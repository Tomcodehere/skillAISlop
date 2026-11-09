---
num: 1431
resume: "Compacter automatiquement une conversation longue en 2027 : déclencher au seuil de tokens (ex. 80 % de la fenêtre), résumer en gardant décisions/code/préférences/tâches en cours, et réinjecter le résumé. Étape 1 : Fixer le seuil de déclenchement (ex. 80 % de la fenêtre, mesuré skill 326)."
lang: "fr"
date_ajout: "2026-11"
nom: "Compaction et resume de conversation"
emoji: "🗜️"
domaine: "IA / Prompting"
signal: "Compacter une longue conversation en 2027 : quand déclencher le résumé (seuil de tokens), quoi garder (décisions, code, préférences, tâches en cours), format du résumé, réinjection dans le contexte. Utilise quand une session dépasse la fenêtre. N'utilise pas pour archiver (voir mémoire persistante)."
mot_cle: "compaction conversation résumé seuil tokens"
nom_court: "Compaction"
branche: "D14"
synonymes: ["résumer une longue conversation LLM", "quand compacter le contexte", "garder décisions et code en cours"]
cross_refs: [236, 326, 714]
tags: ["2027"]
depends_on: [236]
---

## 1431. 🗜️ Compaction et resume de conversation (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Compacter automatiquement une conversation longue en 2027 : déclencher au seuil de tokens (ex. 80 % de la fenêtre), résumer en gardant décisions/code/préférences/tâches en cours, et réinjecter le résumé.

**Quand l'utiliser (triggers)** :
- Ma conversation dépasse 100k tokens, je compacter
- Quoi garder dans le résumé de session ?
- Seuil de compaction automatique

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte de compaction. Tu définis le seuil (80 % fenêtre), le prompt de résumé structuré (décisions prises, code en cours, préférences, TODO, blocages), et la réinjection en system/context condensé. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'historique de la conversation
- La fenêtre du modèle
- Les préférences utilisateur à préserver

**Méthode** :
1. Fixer le seuil de déclenchement (ex. 80 % de la fenêtre, mesuré skill 326).
2. Prompt de compaction : résume en gardant décisions, code, préférences, TODO, blocages.
3. Remplacer l'historique ancien par le résumé + les derniers N messages en clair.
4. Réinjecter le résumé au début du contexte (primauté).
5. Vérifier que la tâche en cours peut reprendre sans perte.

**Sorties attendues** :
- Le trigger de compaction configuré
- Le prompt de résumé structuré
- Une session longue poursuivie sans perte

**Exemple de prompt** :
> « Ma session fait 150k tokens et rame : mets en place la compaction auto (seuil 80 %, résumé structuré décisions/code/TODO, réinjection). »

**Cas d'usage** : Sessions longues (code, rédaction), agents au long cours. S'articule avec skills 236 (contexte), 326 (tokens) et 714 (mémoire persistante).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
