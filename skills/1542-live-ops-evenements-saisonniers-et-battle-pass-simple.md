---
num: 1542
resume: "Organiser des événements saisonniers en 2027 : event temporaire (2 semaines, skins/quêtes/niveau dédiés activés par remote config), battle pass 30 paliers (gratuit + payant), annonce in-game, métriques de l'event (1540), rotation mensuelle. Étape 1 : Planifier l'année : 1 event/mois (Halloween, Noël, été...), durée 2 semaines, contenu dédié (skins 1585, quêtes 1531, niveau temporaire)."
lang: "fr"
date_ajout: "2026-11"
nom: "Live ops : evenements saisonniers et battle pass simple"
emoji: "🌟"
domaine: "Game Dev"
signal: "Organiser des événements saisonniers en 2027 : event temporaire (Halloween 2 semaines) avec contenu dédié (skins, niveau, quêtes 1531), battle pass simple (30 paliers, récompenses gratuites/payantes 1585), annonce in-game + mail, analytics de l'event (1540), rotation mensuelle. Utilise pour la rétention long terme. N'utilise pas pour le contenu permanent."
mot_cle: "live ops événement saisonnier Halloween battle pass 30 paliers rotation"
nom_court: "Live ops"
branche: "D22"
synonymes: ["organiser un event Halloween 2 semaines skins niveau temporaire", "battle pass 30 paliers gratuit payant", "rotation mensuelle des events avec analytics"]
cross_refs: [1541, 1540, 1531]
tags: ["2027"]
depends_on: [1541]
---

## 1542. 🌟 Live ops : evenements saisonniers et battle pass simple (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Organiser des événements saisonniers en 2027 : event temporaire (2 semaines, skins/quêtes/niveau dédiés activés par remote config), battle pass 30 paliers (gratuit + payant), annonce in-game, métriques de l'event (1540), rotation mensuelle.

**Quand l'utiliser (triggers)** :
- Lancer un event Halloween (skins + niveau temporaire) 2 semaines
- Battle pass 30 paliers récompenses gratuites et payantes
- Mesurer si l'event augmente la rétention D7

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es game designer live ops. Tu active l'event par remote config (sans mise à jour), contenu dédié (skins, quêtes 1531, niveau), battle pass (XP event → paliers, récompenses), annonce (bannière + mail), et tu mesures rétention/revenus vs période normale (1540/1541). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le calendrier des events (mensuel)
- Le contenu de l'event (skins, quêtes, niveau)
- Le battle pass (30 paliers, prix)

**Méthode** :
1. Planifier l'année : 1 event/mois (Halloween, Noël, été...), durée 2 semaines, contenu dédié (skins 1585, quêtes 1531, niveau temporaire).
2. Activer par remote config (dates de début/fin) → zéro déploiement pour lancer/arrêter.
3. Battle pass : 30 paliers, track gratuit (récompenses basiques) + track payant 9,99 € (1585), XP event gagnée en jouant.
4. Annoncer : bannière in-game, mail, push, page event avec compte à rebours.
5. Mesurer : rétention D7, revenus, participation (1540), ajuster l'an prochain.

**Sorties attendues** :
- L'event saisonnier déployé (remote config)
- Le battle pass 30 paliers (gratuit/payant)
- Les métriques de l'event vs normale

**Exemple de prompt** :
> « Lance l'event Halloween 2027 : 2 semaines, 10 skins citrouille, niveau hanté temporaire, quêtes dédiées (1531), battle pass 30 paliers (9,99 €), remote config, analytics rétention D7. »

**Cas d'usage** : Rétention long terme, revenus saisonniers. S'articule avec skills 1541 (A/B), 1540 (analytics) et 1531 (quêtes).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
