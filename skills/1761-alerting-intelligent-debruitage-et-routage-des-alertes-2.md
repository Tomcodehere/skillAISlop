---
num: 1761
date_ajout: "2026-11"
nom: "Alerting intelligent : debruitage et routage des alertes (2027)"
emoji: "🔔"
domaine: "Développement"
signal: "Concevoir un alerting intelligent en 2027 : alertes basees sur les SLO et le burn rate (pas sur chaque pic CPU), dedoublonnage et groupement, routage vers la bonne equipe (PagerDuty/Opsgenie), escalade automatique. But : moins d'alertes, plus d'actions. N'utilise pas pour remplacer la supervision (gardez les metriques)."
mot_cle: "alerting intelligent debruitage dedoublonnage routage PagerDuty Opsgenie SLO burn rate 2027"
nom_court: "Alerting intelligent"
branche: "D16"
synonymes: ["alertes basees SLO burn rate au lieu de pics CPU", "dedoublonnage groupement des alertes avant notification", "routage alerte vers la bonne equipe avec escalade auto"]
cross_refs: [1757, 1758, 1754]
tags: ["2027"]
depends_on: [1757]
---

## 1761. 🔔 Alerting intelligent : debruitage et routage des alertes (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Remplacer les alertes brutes (CPU, mémoire, disque) par des alertes dérivées des SLO (burn rate 1757), avec dédoublonnage, groupement par service et routage automatique vers l'équipe responsable avec escalade.

**Quand l'utiliser (triggers)** :
- 100 alertes par jour, personne ne regarde
- alerte CPU 80 % mais zero impact utilisateur
- qui est d'astreinte cette nuit ? routage manuel des alertes

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es SRE / ingénieur plateforme. Tu construis les alertes sur les signaux qui comptent (SLO, burn rate, erreurs 5xx), tu groupes et dédupliques (flapping), tu routes vers l'équipe propriétaire avec escalade apres X minutes sans acquittement. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les SLO et burn rates existants (1757)
- Le catalogue des services et leurs proprietaires
- L'outil d'alerting (PagerDuty, Opsgenie, Grafana Alerting)

**Méthode** :
1. Lister les alertes existantes et supprimer celles sans impact utilisateur (CPU/ram/disque bruts).
2. Creer les alertes SLO : burn rate rapide (2 % budget en 1 h) et lent (5 % en 6 h), multi-window.
3. Configurer le groupement (par service, par sévérité) et le dédoublonnage (fenêtre 5 min).
4. Routage : chaque alerte vers l'équipe propriétaire (catalogue 1700), escalade automatique après 15 min sans ack, puis cellule de crise (1758).

**Sorties attendues** :
- Le jeu d'alertes reduit (SLO uniquement) et justifie
- La matrice de routage equipe/escalade
- Le taux de bruit mesure (alertes/semaine en baisse)

**Exemple de prompt** :
> « Alerte 'paiement indisponible' déclenchée uniquement si le burn rate SLO 99,5 % depasse le seuil en fenetre 1 h, groupée par service, routée vers l'équipe paiement avec escalade auto vers le responsable si pas d'ack en 15 min. »

**Cas d'usage** : Moins de bruit, plus d'action. S'articule avec skills 1757 (burn rate), 1758 (incident SEV), 1754 (alertes as code).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
