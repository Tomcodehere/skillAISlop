---
num: 1764
resume: "Documenter un runbook par alerte récurrente (diagnostic, commandes, remédiation, critère d'escalade) versionné avec le code, et automatiser les remédiations sûres et réversibles (redémarrage, scale, purge de cache). Étape 1 : Lister les 10 dernieres alertes/incidents recurrents et ecrire le runbook de chacun (symptome, diagnostic, commandes, remédiation, escalade)."
date_ajout: "2026-11"
nom: "Runbooks et auto-remédiation des incidents"
emoji: "📖"
domaine: "Développement"
signal: "Rediger des runbooks en 2027 : pour chaque alerte recurrente, une procédure pas a pas (diagnostic, commandes, remédiation, escalade) stockee avec le code (docs/runbooks) et versionnee. Aller vers l'auto-remédiation : actions sûres automatisees (redémarrer un pod, vider un cache, scaler +2 replicas) déclenchées automatiquement. N'utilise pas pour automatiser une action non réversible sans validation humaine."
mot_cle: "runbooks procedures incident auto-remediation automatiser redemarrage pod scaling 2027"
nom_court: "Runbooks & auto-remédiation"
branche: "D16"
synonymes: ["runbook pour l'alerte disque plein : etapes commandes escalade", "auto-remediation : redemarrer le pod tout seul sans reveil humain", "action automatique sure vs action destructive qui demande validation"]
cross_refs: [1758, 1761, 1754]
tags: ["2027"]
depends_on: [1758]
---

## 1764. 📖 Runbooks et auto-remédiation des incidents (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Documenter un runbook par alerte récurrente (diagnostic, commandes, remédiation, critère d'escalade) versionné avec le code, et automatiser les remédiations sûres et réversibles (redémarrage, scale, purge de cache).

**Quand l'utiliser (triggers)** :
- incident 3 h du matin : on réinvente la procédure
- alerte pod en CrashLoopBackOff toutes les nuits
- automatiser le scale +2 replicas quand la file depasse 1000 messages

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es SRE / ingénieur plateforme. Tu ecris chaque runbook en 5 sections (symptôme, diagnostic, remédiation, escalade, prévention), tu le lies a l'alerte (1761), et tu automatises uniquement les actions sûres et réversibles avec un log d'audit. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'historique des incidents (1758)
- Les alertes récurrentes (1761)
- Les actions sûres candidates a l'automatisation

**Méthode** :
1. Lister les 10 dernieres alertes/incidents recurrents et ecrire le runbook de chacun (symptome, diagnostic, commandes, remédiation, escalade).
2. Versionner les runbooks avec le code (docs/runbooks) et lier chaque alerte a son runbook.
3. Automatiser les actions sûres : redémarrer un pod, vider un cache, scaler +2 replicas — avec log et possibilité de rollback.
4. Interdire l'automatisation des actions destructives (suppression de données, rollback de BDD) sans validation humaine.

**Sorties attendues** :
- 10 runbooks ecrits et lies aux alertes
- 3-5 auto-remédiations en production avec log d'audit
- La regle : jamais d'action destructive automatisee sans humain

**Exemple de prompt** :
> « Alerte 'file Kafka en retard de 10 000 messages' : runbook diagnostic (consumer lag, partitions), auto-remédiation scale consumers +2 replicas, log dans l'audit, escalade si lag persiste 30 min (1758). »

**Cas d'usage** : MTTR en baisse. S'articule avec skills 1758 (incidents), 1761 (alerting), 1754 (as code).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
