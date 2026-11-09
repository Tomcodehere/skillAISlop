---
num: 1470
resume: "Versionner données et modèles ML en 2027 avec DVC (données/modèles versionnés, stockage S3) et MLflow (experiments tracés, model registry avec stages prod/staging, déploiement). Étape 1 : Mettre les données sous DVC (dvc init, .gitignore les fichiers, dvc push vers S3)."
date_ajout: "2026-11"
nom: "Versionner modeles et donnees avec DVC et MLflow"
emoji: "📂"
domaine: "Data & IA"
signal: "Versionner les modèles ML et leurs données en 2027 comme du code : DVC (données + modèles dans Git-like, stockage S3), MLflow (experiments, registry de modèles, déploiement), ou les deux. Utilise quand on entraîne des modèles en équipe. N'utilise pas pour le code applicatif (voir Git)."
mot_cle: "DVC MLflow versionner modèles données registry ML"
nom_court: "DVC/MLflow"
branche: "D14"
synonymes: ["versionner un modèle ML", "MLflow model registry 2027", "DVC données versionnées S3"]
cross_refs: [1193, 1194, 96]
tags: ["2027"]
depends_on: [1193]
---

## 1470. 📂 Versionner modeles et donnees avec DVC et MLflow (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Versionner données et modèles ML en 2027 avec DVC (données/modèles versionnés, stockage S3) et MLflow (experiments tracés, model registry avec stages prod/staging, déploiement).

**Quand l'utiliser (triggers)** :
- Quel modèle est en prod exactement ?
- Tracer les expériences ML (MLflow)
- Versionner les datasets d'entraînement (DVC)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es MLOps engineer. Tu montres le workflow : DVC pour data+modèles (dvc add, dvc push S3, tags git), MLflow Tracking pour les runs (params, métriques, artefacts), et le Model Registry (staging → prod) avec déploiement. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les datasets d'entraînement (taille, stockage)
- Les expériences ML à tracer
- Le registry cible (MLflow, S3, HuggingFace Hub)

**Méthode** :
1. Mettre les données sous DVC (dvc init, .gitignore les fichiers, dvc push vers S3).
2. Logger chaque run dans MLflow (params, métriques, modèle) avec autolog.
3. Promouvoir le meilleur modèle dans le registry (None → Staging → Production).
4. Reproduire un run : git checkout tag + dvc pull + mêmes hyperparams.
5. CI : test du modèle (skill 1395) avant promotion en prod.

**Sorties attendues** :
- DVC configuré (data versionnée sur S3)
- Le MLflow tracking + registry opérationnel
- La procédure de rollback de modèle (registry)

**Exemple de prompt** :
> « On ne sait plus quel modèle est en prod ni avec quelles données : mets DVC (datasets versionnés) + MLflow (runs tracés, registry staging/prod, rollback). »

**Cas d'usage** : ML en équipe, reproductibilité, audit. S'articule avec skills 1193 (MLOps), 1194 (pipeline ML) et 96 (datasets).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
