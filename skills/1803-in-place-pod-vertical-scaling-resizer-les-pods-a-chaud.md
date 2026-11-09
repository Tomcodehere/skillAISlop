---
num: 1803
resume: "Activer InPlacePodVerticalScaling (GA 1.35, init containers GA 1.37) pour redimensionner CPU/mémoire des pods à chaud, sans recréation ni perte de session, piloté par le VPA en mode Recommandation. Étape 1 : Activer InPlacePodVerticalScaling (feature gate on par défaut en 1.35+)."
lang: "fr"
date_ajout: "2026-11"
nom: "In-Place Pod Vertical Scaling : resizer les pods à chaud"
emoji: "⚡"
domaine: "Développement"
signal: "Redimensionner CPU/mémoire d'un pod SANS le recréer grâce à InPlacePodVerticalScaling (GA dans k8s 1.35 pour les workloads stateful, init containers couverts en GA dans 1.37) : le kubelet applique la nouvelle request, pas de restart, pas de perte de session. À combiner avec le VPA (recommandation) ou le KEDA. N'utilise pas si l'app ne supporte pas le changement à chaud (relire la doc de l'app)."
mot_cle: "InPlacePodVerticalScaling resize pod à chaud VPA sans restart stateful k8s GA 1.35"
nom_court: "InPlace resize"
branche: "D16"
synonymes: ["changer les requests CPU d'un pod sans le recréer (in-place resize)", "VPA recommande des ressources mais le pod n'est pas resizé : activer InPlacePodVerticalScaling", "stateful pod resizé à chaud : pas de perte de session"]
cross_refs: [609, 1862, 1873]
tags: ["2027"]
depends_on: [609]
---

## 1803. ⚡ In-Place Pod Vertical Scaling : resizer les pods à chaud

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Activer InPlacePodVerticalScaling (GA 1.35, init containers GA 1.37) pour redimensionner CPU/mémoire des pods à chaud, sans recréation ni perte de session, piloté par le VPA en mode Recommandation.

**Quand l'utiliser (triggers)** :
- mon pod est sous-dimensionné mais je ne veux pas le restart
- VPA en mode Auto ne fait rien : activer le resize in-place
- stateful (BDD, cache) : resize sans perdre les connexions

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es SRE / ingénieur plateforme. Tu actives la feature gate InPlacePodVerticalScaling, tu mets le VPA en mode Recommandation puis Auto quand stable, et tu vérifies que l'app tolère le resize (sinon garder le restart classique). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le cluster k8s 1.35+
- Le VPA installé
- La tolérance au resize de chaque app

**Méthode** :
1. Activer InPlacePodVerticalScaling (feature gate on par défaut en 1.35+).
2. VPA en mode Recommandation : lire les recommandations dans le VPA CR. Passer en Auto : le kubelet applique in-place (requests modifiés, pas de restart).
3. Vérifier : pas de pod recréé (uptime conservée), métriques 1416 stables, pas d'OOMKill.
4. Apps non compatibles : les exclure du VPA Auto (garder UpdateMode Off).

**Sorties attendues** :
- Le resize in-place actif (VPA Auto) sur les apps compatibles
- La liste des apps exclues (non compatibles)
- Le suivi : 0 restart, uptime conservé, coûts en baisse (1862)

**Exemple de prompt** :
> « API burst à 2h : VPA recommande 4 CPU, InPlacePodVerticalScaling applique in-place en 30 s — le pod garde son uptime (pas de restart), les requêtes en cours continuent, puis scale down la nuit. »

**Cas d'usage** : Workloads stateful ou à sessions longues. S'articule avec skills 609, 1862 (coût), 1873 (KEDA), 1416 (monitoring).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
