---
num: 1492
date_ajout: "2026-11"
nom: "Kill switch d'une feature IA (desactivation propre, 2027)"
emoji: "🔴"
domaine: "Produit & IA"
signal: "Prévoir le kill switch d'une feature IA en 2027 : flag global pour couper instantanément (sans déploiement), file d'attente vidée proprement, message utilisateur clair ('fonctionnalité temporairement indisponible'), données des sessions IA conservées, métriques d'incident, post-mortem (89). Utilise quand une feature IA est en prod. N'utilise pas pour une panne infra (256)."
mot_cle: "kill switch feature IA couper instantanément flag global propre"
nom_court: "Kill switch IA"
branche: "D14"
synonymes: ["couper une feature IA en 1 clic", "désactiver proprement une IA en prod", "message utilisateurs si IA down"]
cross_refs: [304, 1418, 89]
tags: ["2027"]
depends_on: [304]
---

## 1492. 🔴 Kill switch d'une feature IA (desactivation propre, 2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Prévoir le kill switch d'une feature IA en 2027 : flag global (couper en < 1 min sans déploiement), vidage propre des files, message clair aux utilisateurs, conservation des données, et post-mortem si coupure longue.

**Quand l'utiliser (triggers)** :
- L'IA déraille en prod, couper en 1 clic
- Flag kill switch sur notre feature IA
- Que dire aux users si l'IA est coupée ?

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es SRE feature IA. Tu mets un flag global (désactivation instantanée, testé), une page de statut/message in-app pré-rédigé, le vidage des files d'attente (319), la conservation des logs (1476), et la procédure de remise en route après analyse. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La feature IA en prod
- Le flag de kill switch (304)
- Le message de statut pré-rédigé

**Méthode** :
1. Flag 'ia_enabled' global (désactivation < 1 min, testé en staging).
2. Au kill : vider les files d'attente en cours, respuestas 'indisponible' aux requêtes entrantes.
3. Message in-app/status page pré-rédigé ('fonctionnalité temporairement indisponible, merci de votre patience').
4. Conserver logs et contexte des sessions coupées (1476) pour l'analyse.
5. Post-mortem (89) si > 30 min, décision de remise avec correctif + canary (1418).

**Sorties attendues** :
- Le kill switch testé et documenté
- Le message de statut et la procédure de vidage
- Le post-mortem et la remise en canary

**Exemple de prompt** :
> « Notre copilote IA hallucine sur certains cas en prod : mets un kill switch (flag off en 1 min, message users, logs conservés, post-mortem, remise en canary). »

**Cas d'usage** : Sécurité/fiabilité IA en prod, gestion d'incident. S'articule avec skills 304 (flags), 1418 (canary) et 89 (post-mortem).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
