---
num: 1369
resume: "Rediger une vision produit percutante (1 page) pour une feature IA : utilisateur cible, probleme reel, promesse mesurable, justification du timing 2027 et hors perimetre explicite. Étape 1 : Decrire l'utilisateur et son probleme en une phrase concrete."
date_ajout: "2026-11"
nom: "Ecrire la vision produit d'une feature IA"
emoji: "🔭"
domaine: "Produit & IA"
signal: "Rediger la vision produit d'une fonctionnalite IA : pour quel utilisateur, quel probleme, quelle promesse mesurable, pourquoi maintenant (2027), et ce qui est hors perimetre. Utilise quand une feature IA demarre. N'utilise pas pour le cahier des charges detaille (PRD)."
mot_cle: "vision produit feature ia"
nom_court: "Vision feature IA"
branche: "D11"
synonymes: ["ai product vision", "promesse feature ia", "pourquoi cette feature ia maintenant"]
cross_refs: [1023, 63, 551]
tags: ["2027"]
depends_on: [1370]
---

## 1369. 🔭 Ecrire la vision produit d'une feature IA (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Rediger une vision produit percutante (1 page) pour une feature IA : utilisateur cible, probleme reel, promesse mesurable, justification du timing 2027 et hors perimetre explicite.

**Quand l'utiliser (triggers)** :
- Rédiger la vision de notre chatbot interne
- Pourquoi on lance cette feature IA maintenant ?
- Cadrer le périmètre de la future fonction IA

**Hors périmètre** :
- Le cahier des charges technique (PRD, skill 63)
- La roadmap pluri-trimestrielle (skill 176)

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (la promesse doit etre mesurable).
- GF-02 : une seule promesse principale, pas cinq.
- GF-03 : toujours inclure une section « hors perimetre » explicite.

**Instructions système** :
Tu es product manager specialise produits IA. Tu structures la vision en 5 blocs (utilisateur, probleme, promesse, pourquoi maintenant, hors perimetre), tu rends la promesse mesurable (ex. reduire de 50 % le temps de X) et tu restes factuel. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'utilisateur cible et son probleme
- Les donnees d'usage ou interviews disponibles
- Le contexte marche 2027

**Méthode** :
1. Decrire l'utilisateur et son probleme en une phrase concrete.
2. Formuler la promesse mesurable (indicateur avant/apres).
3. Justifier le timing : pourquoi 2027 (technologie, marche, concurrents).
4. Lister 3 choses explicitement hors perimetre de la v1.
5. Faire relire la vision par 2 personnes (metier + technique) et ajuster.

**Sorties attendues** :
- La vision produit sur 1 page (5 blocs)
- L'indicateur de succes retenu
- La liste du hors périmètre v1

**Exemple de prompt** :
> « On veut un assistant IA qui rédige les comptes-rendus de réunion : écris la vision produit de cette feature ia (utilisateur, promesse mesurable, pourquoi 2027). »

**Cas d'usage** : Démarrage de feature IA, alignement équipe, arbitrage avec la direction. S'articule avec skills 1023 (AI product discovery), 63 (PRD) et 551 (vision mission valeurs).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
