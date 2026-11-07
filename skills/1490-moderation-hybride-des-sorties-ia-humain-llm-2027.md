---
num: 1490
nom: "Moderation hybride des sorties IA (humain + LLM, 2027)"
emoji: "🛡"
domaine: "Produit & IA"
signal: "Modérer les contenus générés par IA en production en 2027 : filtre LLM en amont (classification toxicité/illicite/PII, seuils), file d'attente humaine pour les cas limites (taux cible inférieur à 2 %), modération a posteriori (signalements utilisateurs), audit régulier. Utilise quand un produit laisse les utilisateurs générer du contenu public. N'utilise pas pour la modération communautaire classique (192)."
mot_cle: "modération sorties IA hybride LLM file humaine seuils signalements"
nom_court: "Modération IA"
branche: "D14"
synonymes: ["modérer contenus générés IA en prod", "filtre LLM toxicité PII classification", "file de modération humaine cas limites"]
cross_refs: [192, 1440, 235]
tags: ["2027"]
depends_on: [192]
---

## 1490. 🛡 Moderation hybride des sorties IA (humain + LLM, 2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Modérer les sorties IA en production en 2027 (hybride) : classificateur LLM en amont (toxicité, illicite, PII, spam) avec seuils, file humaine pour les cas limites (< 2 % du trafic), signalements utilisateurs traités, audit mensuel.

**Quand l'utiliser (triggers)** :
- Nos users génèrent du contenu problématique via l'IA
- Filtrer les sorties IA avant publication
- Combien de modérateurs humains pour l'IA ?

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es responsable modération IA. Tu définis le pipeline : LLM classifie (catégories + score) → seuil auto-rejet / auto-accept / file humaine ; signalements utilisateurs prioritaires ; taux de revue humaine cible < 2 % ; audit mensuel (échantillon + taux d'erreur). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le contenu généré par IA (texte, image ?)
- Les catégories interdites (légales + charte)
- Le volume de générations/jour

**Méthode** :
1. Définir la charte de modération (catégories : haine, illicite, PII, spam, sexualisé mineur...).
2. Classifier par LLM (prompt few-shot 1426) avec score par catégorie + justification.
3. Seuils : score < 0,3 accept auto, > 0,8 rejet auto + notif user, entre les deux → file humaine.
4. File humaine : modérateurs voient le contenu + contexte + décision en < 2 h.
5. Signalements utilisateurs → traitement prioritaire +Apprentissage ; audit mensuel (échantillon 100, taux faux négatifs).

**Sorties attendues** :
- Le pipeline de modération hybride actif
- Les seuils et la file humaine dimensionnée
- L'audit mensuel + taux de faux négatifs

**Exemple de prompt** :
> « Notre app laisse les users générer des posts avec l'IA et on a des abus : mets une modération hybride (LLM auto + file humaine < 2 %, signalements, audit). »

**Cas d'usage** : UGC avec IA, conformité (DSA), confiance plateforme. S'articule avec skills 192 (modération), 1440 (PII) et 235 (crise).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
