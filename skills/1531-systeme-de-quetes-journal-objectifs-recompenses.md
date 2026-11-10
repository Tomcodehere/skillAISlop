---
num: 1531
resume: "Concevoir un système de quêtes en 2027 : journal (en cours/finies), objectifs avec compteur temps réel (tuer 5 rats → 3/5), quêtes principales chaînées + secondaires, récompenses (XP/gold/objet), validation au PNJ donneur. Étape 1 : Définir Quest en data (JSON/ScriptableObject) : objectifs (tuer X, ramasser Y, parler à Z, aller à), récompenses, quête suivante."
lang: "fr"
date_ajout: "2026-11"
nom: "Systeme de quetes : journal, objectifs, recompenses"
emoji: "📜"
domaine: "Game Dev"
signal: "Concevoir un système de quêtes en 2027 : journal de quêtes (en cours/terminées), objectifs traçables (tuer 5 rats → compteur 3/5), quêtes principales (chaînées) et secondaires, récompenses (XP 1530, gold 1529, objet 1528), échec si timer. Utilise pour tout RPG/aventure. N'utilise pas pour un jeu bac à sable pur."
mot_cle: "système de quêtes journal objectifs compteur récompenses chaînées"
nom_court: "Quêtes"
branche: "D22"
synonymes: ["journal de quêtes avec compteur 3/5", "quête principale chaînée quêtes secondaires", "récompense XP gold objet à la validation"]
cross_refs: [1530, 1532, 1528]
tags: ["2027"]
depends_on: [1530]
---

## 1531. 📜 Systeme de quetes : journal, objectifs, recompenses (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Concevoir un système de quêtes en 2027 : journal (en cours/finies), objectifs avec compteur temps réel (tuer 5 rats → 3/5), quêtes principales chaînées + secondaires, récompenses (XP/gold/objet), validation au PNJ donneur.

**Quand l'utiliser (triggers)** :
- Journal de quêtes avec objectifs cochés
- Compteur 'rats tués 3/5' en temps réel
- Quête principale qui enchaîne la suivante

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es game designer quêtes. Tu définis la structure Quest {id, titre, description, objectifs[{type, cible, actuel}], récompenses, donneur, suivante}, le suivi d'événements (kill rat → +1), et l'UI journal (liste + détails + objectifs cochés). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les quêtes (donneur PNJ, objectifs, récompenses)
- Les événements de jeu à écouter (kill, ramasser, parler)
- La chaîne principale

**Méthode** :
1. Définir Quest en data (JSON/ScriptableObject) : objectifs (tuer X, ramasser Y, parler à Z, aller à), récompenses, quête suivante.
2. Système de quêtes : accepter (PNJ), suivre (event bus écoute les actions du joueur, met à jour actuel), compléter (tous objectifs OK + retour donneur) → récompenses + suivante débloquée.
3. UI : journal (Touche J), onglets En cours/Terminées, détails avec objectifs [x] et récompenses, marqueur de quête sur la minimap (1570).
4. Timer optionnel (quête échouée si dépassé), échec possible (mort du PNJ donneur).

**Sorties attendues** :
- Le système de quêtes fonctionnel (data-driven)
- Le journal UI avec compteurs temps réel
- La chaîne principale + quêtes secondaires

**Exemple de prompt** :
> « Ajoute des quêtes à mon RPG : journal (J), objectifs traçables (5 rats → 3/5), récompenses (XP/gold/objet), chaîne principale 'le village → la grotte → le boss'. »

**Cas d'usage** : RPG, aventure, MMO. S'articule avec skills 1530 (XP), 1532 (dialogues) et 1528 (loot).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
