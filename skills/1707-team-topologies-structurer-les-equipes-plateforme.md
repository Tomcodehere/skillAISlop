---
num: 1707
date_ajout: "2026-11"
nom: "Team Topologies : structurer les équipes plateforme"
emoji: "👥"
domaine: "Gestion"
signal: "Organiser les équipes engineering avec Team Topologies (2027) : 4 types d'équipes — stream-aligned (produit, autonome), platform (IDP 1700, réduit la charge cognitive), enabling (expertise ponctuelle : sécurité, perf), complicated-subsystem (composant complexe : paiement, moteur). + charge cognitive mesurée (enquêtes). Utilise pour réorganiser une org tech. N'utilise pas pour une équipe de 3."
mot_cle: "team topologies 2027 stream-aligned platform enabling complicated-subsystem charge cognitive"
nom_court: "Team Topologies"
branche: "D25"
synonymes: ["équipe platform dédiée à l'IDP (Team Topologies)", "stream-aligned : équipe produit autonome de bout en bout", "charge cognitive : enquête interne sur la complexité perçue"]
cross_refs: [1700, 210, 72]
tags: ["2027"]
depends_on: [1700]
---

## 1707. 👥 Team Topologies : structurer les équipes plateforme (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Structurer une org tech en 2027 avec Team Topologies : équipes stream-aligned (produit, autonomes), platform (l'IDP 1700), enabling (expertise sécurité/perf), complicated-subsystem (composant complexe), en mesurant la charge cognitive par enquête.

**Quand l'utiliser (triggers)** :
- tout le monde attend l'équipe 'infra' (goulot)
- créer une équipe platform dédiée à l'IDP (Team Topologies)
- mesurer la charge cognitive des devs (enquête interne)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es engineering manager. Tu classes chaque équipe dans les 4 types, tu définis les interactions (X-as-a-Service pour la platform, collaboration temporaire pour enabling, facilitation pour subsystem), et tu mesures la charge cognitive (enquête 2x/an). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'org actuelle (équipes, dépendances)
- Les flux de valeur (produits)
- L'IDP (1700) si dispo

**Méthode** :
1. Identifier les flux de valeur (chaque produit = 1 équipe stream-aligned autonome : build, run, own).
2. Équipe platform : construit l'IDP (1700), traite les équipes produit comme des clients (NPS interne).
3. Équipes enabling : sécurité (1646), performance (1618), data (1660) — aident ponctuellement, ne font pas à la place.
4. Complicated-subsystem : paiement, moteur de règles, ML — expertise profonde, interface claire (API 526).
5. Charge cognitive : enquête 2x/an (trop de contexte ? trop d'interruptions ?), objectif baisse.
6. Revue annuelle de la topologie (les équipes évoluent).

**Sorties attendues** :
- L'org redessinée en 4 types d'équipes avec interactions claires
- L'équipe platform en place servant l'IDP (1700)
- L'enquête de charge cognitive (baseline + baisse visée)

**Exemple de prompt** :
> « Toute l'orga attend l'équipe infra (goulot) : applique Team Topologies 2027 — équipes stream-aligned autonomes par produit, équipe platform dédiée à l'IDP (1700), enabling sécurité/perf, mesure de la charge cognitive 2x/an. »

**Cas d'usage** : Réorganisation org tech > 20 pers. S'articule avec skills 1700 (IDP), 210 (décisions équipe), 72 (semaine) et 1698 (analytics).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
