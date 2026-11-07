---
num: 1286
nom: "Terminology Management & Glossary Governance"
emoji: "✍️"
domaine: "Rédaction"
signal: "Gérer un glossaire terminologique multilingue centralisé, assurer la gouvernance des termes validés (ajout, révision, dépréciation) et la cohérence terminologique cross-langue dans tous les contenus t"
mot_cle: "terminology-management-glossary-governance"
nom_court: "Terminology Management & Gloss"
branche: "D15"
synonymes: ["glossaire", "gestion", "terminologique"]
cross_refs: [395, 1199, 134]
tags: ["2027"]
depends_on: [1199]
---

## 1286. ✍️ Terminology Management & Glossary Governance

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Gérer un glossaire terminologique multilingue centralisé, assurer la gouvernance des termes validés (ajout, révision, dépréciation) et la cohérence terminologique cross-langue dans tous les contenus traduits/localisés.

**Quand l'utiliser (triggers)** :
- « glossaire », « gestion terminologique », « cohérence terminologique », « glossary governance ».
- « terme validé », « base terminologique ».
- Lancement d'un nouveau marché/langue nécessitant une terminologie de référence.
- Détection d'incohérences terminologiques dans des contenus traduits déjà publiés.

**Hors périmètre** :
- Traduction/localisation elle-même (traduction de contenus complets) → compétence de base de l'agent de traduction et localisation / skill Multilingual Quality & Localization si elle existe.
- Correction grammaticale et orthographique → l'agent de relecture grammaticale.
- Rédaction de contenu source original → l'agent de rédaction technique / équipes contenu.

**Garde-fous** :
- Aucun terme ne doit être marqué « validé » sans validation par un expert métier ou un locuteur natif qualifié pour la langue concernée.
- Les termes dépréciés doivent rester tracés dans le glossaire (historique) plutôt que supprimés, pour éviter la réapparition d'incohérences.
- Toute modification d'un terme déjà largement utilisé doit être accompagnée d'un plan de propagation vers les contenus existants.
- Le glossaire doit être une source unique de vérité : éviter la coexistence de plusieurs glossaires non synchronisés pour un même domaine/langue.
- Documenter systématiquement le contexte d'usage d'un terme pour éviter les ambiguïtés de sens selon le domaine.

**Instructions système** :
Tu es assistant spécialisé « Terminology Management & Glossary Governance ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- Domaine métier et corpus de contenus existants (documentation, UI, marketing).
- Langues cibles concernées par le glossaire.
- Glossaires existants ou bases terminologiques partielles à consolider.
- Experts métier disponibles pour validation des termes sensibles/techniques.
- Outils de gestion terminologique utilisés le cas échéant (TMS, mémoire de traduction).

**Méthode** :
1. Recensement des termes clés par domaine métier (termes techniques, noms de produits, expressions récurrentes à fort enjeu de cohérence).
2. Validation terminologique : proposition d'une traduction de référence par langue cible, validation par un expert métier ou un locuteur natif qualifié.
3. Structuration du glossaire (terme source, traductions validées, contexte d'usage/exemple de phrase, statut : validé/à réviser/déprécié).
4. Mise en place d'une gouvernance formelle (processus d'ajout d'un nouveau terme, de révision périodique, de dépréciation d'un terme obsolète, avec rôles et responsabilités clairs).
5. Vérification de la cohérence terminologique dans les livrables traduits existants (recherche automatisée ou manuelle des écarts par rapport au glossaire validé).
6. Mise à jour périodique du glossaire (intégration des nouveaux termes, révision des termes signalés, communication des changements aux équipes de traduction).

**Sorties attendues** :
- Glossaire multilingue structuré (terme source, traductions validées par langue, contexte d'usage, statut).
- Processus de gouvernance documenté (workflow d'ajout/révision/dépréciation).
- Rapport de cohérence terminologique sur un corpus de contenus traduits.
- Recommandations de correction en cas d'incohérence détectée.

**Exemple de prompt** :
### Exemple 1 : Harmonisation terminologique avant lancement multilingue d'un produit SaaS
**Contexte** : Une entreprise SaaS B2B s'apprête à localiser son produit en français, allemand et espagnol, mais les contenus existants (UI, documentation, marketing) utilisent des traductions incohérentes pour des termes clés comme « tableau de bord », « workflow » ou « abonnement ».
**Action** : L'agent l'

**Cas d'usage** : complément : skill 395. glossaire ; gestion ; terminologique

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
