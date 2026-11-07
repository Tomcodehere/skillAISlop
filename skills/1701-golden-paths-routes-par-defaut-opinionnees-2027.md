---
num: 1701
date_ajout: "2026-11"
nom: "Golden paths : routes par defaut opinionnees (2027)"
emoji: "🛤️"
domaine: "Développement"
signal: "Concevoir des golden paths en 2027 : chemins par défaut, opinionnés et supportés (ex. 'nouveau service Node+Postgres', 'nouvelle BDD managée') couvrant 80 % des cas, avec dérogation documentée pour le reste. Le but : réduire la charge cognitive, pas interdire. Utilise dans une IDP (1700). N'utilise pas comme seule option (laisser la sortie de secours)."
mot_cle: "golden paths routes par défaut opinionnées IDP 2027 80% des cas dérogation documentée"
nom_court: "Golden paths"
branche: "D16"
synonymes: ["golden path : nouveau service en 1 clic dans l'IDP", "couvrir 80 % des cas en golden paths, le reste en dérogation documentée", "réduire la charge cognitive des devs (Team Topologies)"]
cross_refs: [1700, 311, 50]
tags: ["2027"]
depends_on: [1700]
---

## 1701. 🛤️ Golden paths : routes par defaut opinionnees (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Concevoir des golden paths en 2027 : chemins par défaut opinionnés et supportés couvrant 80 % des cas courants (nouveau service, BDD, file de déploiement), avec une procédure de dérogation documentée pour les cas atypiques.

**Quand l'utiliser (triggers)** :
- tout le monde réinvente le service boilerplate
- golden path 'service Node+Postgres+CI+k8s' en 5 min
- 80 % des cas couverts, 20 % en dérogation documentée

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es platform engineer. Tu définis les golden paths à partir des demandes récurrentes (audit tickets), chaque path = template Scaffolder + CI + policies (Kyverno) + observabilité par défaut, et tu documentes la dérogation (quand sortir du path). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'audit des demandes récurrentes (top 3-5)
- L'IDP (1700) et ses templates
- La politique de dérogation

**Méthode** :
1. Lister les 3-5 tâches les plus fréquentes (nouveau service, BDD, déploiement, secret).
2. Pour chaque : golden path = template + pipeline + policies + observabilité, testé, versionné.
3. Mesurer : % de demandes sur golden path (objectif 80 %), temps moyen (minutes vs jours), tickets -70 %.
4. Dérogation documentée : comment sortir du path (qui valide, où ça se log).
5. Revue trimestrielle : ajuster les paths selon l'usage réel (analytics 1698).

**Sorties attendues** :
- 3-5 golden paths opérationnels (templates testés)
- Le taux d'adoption (80 %) et le temps moyen mesurés
- La procédure de dérogation documentée

**Exemple de prompt** :
> « Chaque équipe réinvente son boilerplate de service : crée 3 golden paths dans l'IDP (service Node+Postgres, BDD managée Crossplane, déploiement ArgoCD), objectif 80 % d'adoption et tickets -70 % mesurés. »

**Cas d'usage** : Dans toute IDP. S'articule avec skills 1700 (IDP), 311 (conventions), 50 (SOP) et 1698 (analytics).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
