---
num: 1760
resume: "Mettre en place des SLO multi-niveaux (interne/externe, par parcours critique) avec une politique d'error budget explicite : seuils, conséquences (gel des livraisons, focus fiabilité), et revue mensuelle du budget consommé. Étape 1 : Identifier les 3-5 parcours critiques utilisateurs (paiement, auth, lecture)."
lang: "fr"
date_ajout: "2026-11"
nom: "SLO multi-niveaux et politique de budget d'erreur"
emoji: "🎯"
domaine: "Data"
signal: "Definir des SLO multi-niveaux en 2027 (ex. disponibilite 99,9 % interne, 99,5 % externe soit 3,6 h d'erreur/mois) avec une politique d'error budget ecrite : que fait-on quand le budget est consomme (gel des features, focus fiabilite). Utilise pour piloter la fiabilite sans sur-alerter. N'utilise pas un seul SLO global pour tout le produit."
mot_cle: "SLO multi-niveaux budget d'erreur 99,5 % 3,6 h par mois politique gel des features 2027"
nom_court: "SLO & error budget"
branche: "D17"
synonymes: ["99,5 % de disponibilite = 3,6 h de downtime autorisees par mois", "politique d'error budget : quoi faire quand le budget est grille", "SLO interne 99,9 % vs SLO externe 99,5 % deux niveaux"]
cross_refs: [1751, 1757, 1758]
tags: ["2027"]
depends_on: [1757]
---

## 1760. 🎯 SLO multi-niveaux et politique de budget d'erreur (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Mettre en place des SLO multi-niveaux (interne/externe, par parcours critique) avec une politique d'error budget explicite : seuils, conséquences (gel des livraisons, focus fiabilité), et revue mensuelle du budget consommé.

**Quand l'utiliser (triggers)** :
- un seul SLO 99,9 % couvre tout le produit indistinctement
- 99,5 % externe = 3,6 h d'indisponibilite par mois, qui decide du gel ?
- quand l'error budget est a 0, quelles features sont gelees ?

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es SRE / responsable fiabilité. Tu hierarchises les parcours (paiement, login, consultation) et tu mets un SLO par niveau avec un budget d'erreur chiffré, une politique écrite (gel, comm, priorisation) et une revue mensuelle du taux de consommation. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les parcours critiques du produit
- Les incidents passes et leur duree
- La politique de deploiement (frequence)

**Méthode** :
1. Identifier les 3-5 parcours critiques utilisateurs (paiement, auth, lecture).
2. Pour chacun : SLO externe (ex. 99,5 % = 3,6 h/mois) + SLO interne plus strict (99,9 %) pour anticiper.
3. Ecrire la politique d'error budget : seuils d'alerte (burn rate 1757), actions (gel features, cellules de crise), responsables.
4. Revoir mensuellement : budget consomme, decisions prises, ajuster les SLO si trop laches ou trop stricts.

**Sorties attendues** :
- 3-5 SLO documentés (parcours, seuil, fenetre)
- La politique d'error budget ecrite et validee
- Le tableau de suivi mensuel du budget consomme

**Exemple de prompt** :
> « SLO externe disponibilite 99,5 % (3,6 h/mois) sur le parcours paiement, SLO interne 99,9 % : si le budget externe est consomme a 50 % en 10 jours (burn rate 1757), gel des nouvelles features et focus fiabilite jusqu'a la fin du mois. »

**Cas d'usage** : Pilotage fiabilite par parcours. S'articule avec skills 1751 (SLO LLM), 1757 (burn rate), 1758 (incidents).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
