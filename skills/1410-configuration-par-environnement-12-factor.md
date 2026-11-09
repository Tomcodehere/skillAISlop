---
num: 1410
resume: "Appliquer la méthode 12-factor à la configuration en 2027 : zero config dans le code, variables d'environnement par environnement, .env.example versionné, secrets jamais committés. Étape 1 : Sortir toute la config du code vers les variables d'environnement."
date_ajout: "2026-11"
nom: "Configuration par environnement (12-factor)"
emoji: "⚙️"
domaine: "Développement"
signal: "Gérer la configuration d'une app selon la méthode 12-factor en 2027 : jamais de config dans le code, variables d'environnement, .env par environnement, secrets hors du dépôt. Utilise quand on déploie sur plusieurs environnements. N'utilise pas pour les secrets eux-mêmes."
mot_cle: "configuration 12-factor variables environnement"
nom_court: "Config 12-factor"
branche: "D15"
synonymes: ["variables d'environnement app", "config par environnement dev prod", "12 factor app"]
cross_refs: [305, 306, 82]
tags: ["2027"]
depends_on: [306]
---

## 1410. ⚙️ Configuration par environnement (12-factor, 2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Appliquer la méthode 12-factor à la configuration en 2027 : zero config dans le code, variables d'environnement par environnement, .env.example versionné, secrets jamais committés.

**Quand l'utiliser (triggers)** :
- Où stocker la config de mon app ?
- .env dev/prod séparés en 2027
- 12-factor : variables d'environnement

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte 12-factor. Tu donnes la structure (.env.example versionné, .env gitignoré, pydantic-settings/dotenv), la règle config=environnement et code=dépôt, et la séparation des secrets (vault). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les environnements (dev, staging, prod)
- La config actuelle (dans le code ?)
- Les outils de secrets (vault, Doppler, SOPS)

**Méthode** :
1. Sortir toute la config du code vers les variables d'environnement.
2. Créer .env.example (clés + valeurs factices) versionné, .env dans .gitignore.
3. Charger via os.environ / pydantic-settings.
4. Un .env par environnement, jamais committé (detect-private-key).
5. Secrets via vault/Doppler/SOPS, jamais en clair.

**Sorties attendues** :
- Le .env.example propre et versionné
- La config chargée par environnement
- La séparation secrets en place

**Exemple de prompt** :
> « Ma config est éparpillée dans le code : applique la méthode 12-factor (variables d'environnement, .env par environnement, secrets hors du dépôt). »

**Cas d'usage** : Déploiement multi-env, onboarding, sécurité des clés. S'articule avec skills 305 (env reproductible), 306 (secrets) et 82 (DevOps).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
