---
num: 1804
resume: "Ordonnancer les jobs distribués (ML multi-GPU, MPI, Ray) en gang via PodGroup/Workload (scheduling.k8s.io) : tous les pods démarrent ensemble ou aucun, sans deadlock de peers. Étape 1 : Créer le Workload (scheduling.k8s.io/v1beta1) avec minAvailable = N pods et la pod template."
date_ajout: "2026-11"
nom: "Gang scheduling : ordonnancer les jobs distribués en bloc"
emoji: "👥"
domaine: "Développement"
signal: "Utiliser le gang scheduling (PodGroup/Workload dans scheduling.k8s.io, alpha 1.35, beta 1.37) pour les jobs distribués (training ML multi-GPU, MPI, Ray) : tous les pods démarrent ensemble ou aucun (all-or-nothing), évitant les deadlocks où des pods attendent des peers jamais schedulés. N'utilise pas pour des services indépendants (ils scalent seuls)."
mot_cle: "gang scheduling PodGroup Workload scheduling.k8s.io all-or-nothing job ML distribué training multi-GPU"
nom_court: "Gang scheduling"
branche: "D16"
synonymes: ["tous les pods d'un job ML démarrent ensemble ou aucun (gang scheduling PodGroup)", "eviter le deadlock : des pods attendent des peers jamais schedulés", "PodGroup scheduling.k8s.io v1beta1 k8s 1.37 beta"]
cross_refs: [1802, 609, 1700]
tags: ["2027"]
depends_on: [1802]
---

## 1804. 👥 Gang scheduling : ordonnancer les jobs distribués en bloc

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Ordonnancer les jobs distribués (ML multi-GPU, MPI, Ray) en gang via PodGroup/Workload (scheduling.k8s.io) : tous les pods démarrent ensemble ou aucun, sans deadlock de peers.

**Quand l'utiliser (triggers)** :
- mon training distribué bloque : 3 pods sur 8 démarrés, les autres en pending
- all-or-nothing pour un job Ray de 16 pods GPU
- PodGroup vs simple Job : quand l'utiliser

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es ingénieur plateforme ML. Tu wrappe le Job distribué dans un Workload (scheduling.k8s.io) avec minAvailable = nombre de pods, et le scheduler réserve les ressources en bloc via DRA (1802) avant de lancer. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le job distribué (Ray, MPI, training framework)
- Le nombre de pods/GPU nécessaires
- k8s 1.35+ (alpha) / 1.37 (beta)

**Méthode** :
1. Créer le Workload (scheduling.k8s.io/v1beta1) avec minAvailable = N pods et la pod template.
2. Le scheduler réserve les N devices (DRA 1802) puis démarre tous les pods en même temps.
3. Si ressources insuffisantes : aucun pod ne démarre (pas de deadlock partiel).
4. Monitorer : temps d'attente en queue, taux de complétion du job.

**Sorties attendues** :
- Le Workload/PodGroup déployé avec minAvailable
- 0 deadlock partiel constaté
- Le temps en queue mesuré

**Exemple de prompt** :
> « Training LLM sur 8 GPU (8 pods) : Workload minAvailable=8, DRA réserve 8 GPU d'un coup — soit les 8 pods démarrent ensemble, soit le job attend en queue sans bloquer le cluster. »

**Cas d'usage** : Jobs ML distribués. S'articule avec skills 1802 (DRA), 609 (k8s), 1700 (IDP).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
