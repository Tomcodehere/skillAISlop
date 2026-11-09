---
num: 1409
resume: "Instrumenter une application en 2027 avec des logs structurés (JSON) : niveaux adaptés, request_id de corrélation, aucune PII en clair, et un moyen de les requêter. Étape 1 : Choisir la librairie de log structuré du langage."
lang: "fr"
date_ajout: "2026-11"
nom: "Logging structure et niveaux de log"
emoji: "📝"
domaine: "Développement"
signal: "Mettre en place un logging structuré en 2027 : niveaux (DEBUG/INFO/WARN/ERROR), logs JSON avec contexte (request_id), jamais de données perso en clair, corrélation de bout en bout. Utilise quand on instrumente une app. N'utilise pas pour les métriques."
mot_cle: "logging structuré JSON niveaux request_id"
nom_court: "Logging structuré"
branche: "D16"
synonymes: ["logs en JSON structurés", "niveaux de log debug info warn error", "correlation id log"]
cross_refs: [191, 1282, 1469]
tags: ["2027"]
depends_on: [1469]
---

## 1409. 📝 Logging structure et niveaux de log (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Instrumenter une application en 2027 avec des logs structurés (JSON) : niveaux adaptés, request_id de corrélation, aucune PII en clair, et un moyen de les requêter.

**Quand l'utiliser (triggers)** :
- Passer mes logs en JSON structuré
- Quels niveaux de log utiliser ?
- Ajouter un request_id pour tracer une requête

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es ingénieur observabilité (logs). Tu proposes le format JSON (level, msg, ts, service, request_id), la règle des niveaux (ERROR=action requise, WARN=à surveiller), et l'interdiction des PII en clair. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La stack (structlog, pino, zap)
- Les logs actuels (texte libre)
- Les besoins de debug vs conformité (rétention)

**Méthode** :
1. Choisir la librairie de log structuré du langage.
2. Définir le schéma JSON standard (level, msg, ts, service, request_id).
3. Ajouter le request_id à chaque requête (middleware).
4. Appliquer les niveaux : DEBUG dev, INFO jalons, WARN anomalie, ERROR incident.
5. Vérifier qu'aucune PII n'est loggée (revue + detect-private-key).

**Sorties attendues** :
- Le schéma de log JSON adopté
- Le middleware de corrélation (request_id)
- La règle des niveaux + conformité PII

**Exemple de prompt** :
> « On ne comprend rien aux logs en prod : mets en place un logging structuré JSON avec niveaux et request_id pour tracer les requêtes de bout en bout. »

**Cas d'usage** : Debug en prod, forensic, conformité. S'articule avec skills 191 (logs fraude), 1282 (monitoring) et 1469 (centralisation logs).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
