---
num: 1769
resume: "Préparer l'équipe aux incidents par des game days trimestriels (simulation réaliste : panne BDD, AZ, fuite de secrets) testant les runbooks et la communication de crise, en complement des exercices tabletop (1454). Étape 1 : Choisir le scenario du trimestre (AZ down, BDD primaire KO, fuite de secret, ransomware) et annoncer 'game day' a l'astreinte."
lang: "fr"
date_ajout: "2026-11"
nom: "Game days et exercices d'incident réguliers"
emoji: "🎮"
domaine: "Gestion"
signal: "Organiser en 2027 des game days réguliers (tous les trimestres) : simuler un incident (panne BDD, fuite de secrets, panne d'AZ) en production contrôlée ou en environnement de recette, avec l'équipe d'astreinte, pour tester les runbooks (1764) et la communication de crise. Variante 'tabletop' (1454) : discussion à froid sans toucher au système. N'utilise pas pour bloquer la prod en heures de pointe."
mot_cle: "game day exercice incident trimestriel simulation panne BDD AZ test runbooks crise 2027"
nom_court: "Game days"
branche: "D25"
synonymes: ["simuler une panne de BDD primaire en prod controlee pour tester le failover", "game day trimestriel avec l'equipe d'astreinte et les runbooks 1764", "tabletop 1454 sans toucher au systeme vs game day live"]
cross_refs: [1758, 1764, 1759]
tags: ["2027"]
depends_on: [1758]
---

## 1769. 🎮 Game days et exercices d'incident réguliers (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Préparer l'équipe aux incidents par des game days trimestriels (simulation réaliste : panne BDD, AZ, fuite de secrets) testant les runbooks et la communication de crise, en complement des exercices tabletop (1454).

**Quand l'utiliser (triggers)** :
- dernier vrai incident SEV1 : personne ne savait quoi faire
- tester le failover BDD en conditions reelles (fenetre de maintenance)
- la communication de crise n'a jamais ete testee

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es responsable fiabilité / SRE lead. Tu choisis un scénario réaliste (panne AZ, BDD primaire down, fuite de clé), tu le joues en heures creuses avec l'astreinte, tu mesures le temps de détection/résolution vs le MTTR cible, et tu produis un rapport avec les écarts des runbooks. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les runbooks (1764) et la procédure d'incident (1758)
- Une fenetre hors pointe pour le game day live
- Le scénario validé par le management

**Méthode** :
1. Choisir le scenario du trimestre (AZ down, BDD primaire KO, fuite de secret, ransomware) et annoncer 'game day' a l'astreinte.
2. Jouer le scenario en live (ou tabletop 1454) : detection, annonce crise, application des runbooks, remédiation.
3. Mesurer : temps de detection, temps de resolution, respect des SLO (1760), qualite de la communication.
4. Rapport blameless (1768) : écarts constates, runbooks a corriger, prochaine date.

**Sorties attendues** :
- Le scenario joue et le chronometrage (detection, resolution)
- Le rapport avec écarts vs runbooks et MTTR cible
- Les corrections de runbooks et la prochaine date de game day

**Exemple de prompt** :
> « Game day T3 : panne simulee de l'AZ primaire, failover BDD en 4 min (runbook 1764), alerte clients communiquee en 10 min, rapport : 2 écarts de runbook corriges, prochain game day T4 sur fuite de secrets. »

**Cas d'usage** : Équipe prête avant la vraie crise. S'articule avec skills 1758 (incidents), 1764 (runbooks), 1759 (chaos), 1454 (tabletop).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
