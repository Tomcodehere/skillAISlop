---
num: 1417
date_ajout: "2026-11"
nom: "Alerting sans bruit : alert fatigue (2027)"
emoji: "🔔"
domaine: "Développement"
signal: "Concevoir des alertes qui ne créent pas de fatigue (alert fatigue) en 2027 : alertes actionnables uniquement, seuils sur erreurs utilisateur/SLO (pas CPU), regroupement, runbook attaché à chaque alerte. Utilise quand on met en place l'alerting. N'utilise pas pour le monitoring lui-même."
mot_cle: "alerting sans bruit alert fatigue SLO runbook"
nom_court: "Alerting sain"
branche: "D16"
synonymes: ["alertes qui ne spamment pas", "réduire le bruit des alertes", "alert fatigue 2027"]
cross_refs: [1416, 256, 89]
tags: ["2027"]
depends_on: [1416]
---

## 1417. 🔔 Alerting sans bruit : alert fatigue (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Concevoir un alerting soutenable en 2027 : seules les alertes actionnables (erreur utilisateur, SLO menacé) déclenchent, avec runbook intégré, dédup/regroupement, et revue mensuelle.

**Quand l'utiliser (triggers)** :
- 40 alertes/jour, personne ne les lit
- Quelles alertes garder vraiment ?
- Runbook attaché à chaque alerte critique

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es SRE alerting. Tu appliques le principe 'alerte = action requise maintenant', tu remplaces les alertes ressources (CPU) par des symptômes (latence, erreurs), et chaque alerte a un runbook. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les alertes actuelles et leur fréquence
- Les SLO de l'application
- L'outil (Alertmanager, PagerDuty, Grafana)

**Méthode** :
1. Lister les alertes et compter les non actionnables.
2. Remplacer alertes ressources (CPU>80%) par symptômes (p99, 5xx).
3. Garder uniquement les alertes à action immédiate + runbook.
4. Grouping/dédup (Alertmanager) anti-spam.
5. Revue mensuelle : alertes déclenchées, faux positifs, ajustements.

**Sorties attendues** :
- La liste d'alertes réduites et justifiées
- Chaque alerte critique avec runbook
- La revue mensuelle instaurée

**Exemple de prompt** :
> « Notre équipe ignore les alertes (40/jour) : conçois un alerting sain (seuils SLO, symptômes pas ressources, runbook par alerte, revue mensuelle). »

**Cas d'usage** : On-call efficace, moins de fatigue, incidents traités plus vite. S'articule avec skills 1416 (monitoring), 256 (incidents) et 89 (post-mortem).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
