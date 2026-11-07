---
num: 1488
date_ajout: "2026-11"
nom: "Integrer un copilote IA dans son produit (in-app)"
emoji: "🤖"
domaine: "Produit & IA"
signal: "Intégrer un copilote IA directement dans son produit en 2027 (in-app) : panneau latéral contextuel (il voit l'écran courant), suggestions proactives pertinentes (pas intrusives), actions possibles (clic = exécution), feedback pouce haut/bas. Utilise quand on ajoute l'IA à une app existante. N'utilise pas pour un chatbot externe (66)."
mot_cle: "copilote IA in-app panneau latéral contextuel suggestions proactives"
nom_court: "Copilote in-app"
branche: "D11"
synonymes: ["ajouter un assistant IA dans mon app", "copilote contextuel voit l'écran", "suggestions IA non intrusives"]
cross_refs: [66, 823, 926]
tags: ["2027"]
depends_on: [1370]
---

## 1488. 🤖 Integrer un copilote IA dans son produit (in-app, 2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Intégrer un copilote IA in-app en 2027 : panneau latéral qui voit le contexte écran, propose 2-3 actions pertinentes (désactivable), exécute au clic, collecte le feedback pouce haut/bas pour s'améliorer.

**Quand l'utiliser (triggers)** :
- Ajouter un copilote IA dans notre app métier
- Le copilote voit l'écran courant et propose
- Feedback pouce haut/bas sur les suggestions IA

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es product manager IA in-app. Tu définis le pattern : contexte de l'écran envoyé au LLM (données visibles uniquement, jamais tout le compte), 2-3 suggestions max avec action au clic, opt-out par défaut respecté, feedback loggé (1371). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'app existante (web/mobile) et son contexte écran
- Les actions possibles (API internes)
- Les données visibles à l'écran (privacy : jamais tout le compte)

**Méthode** :
1. Choisir l'UX : panneau latéral docké, bouton '✨ Suggérer' sur les zones clés.
2. Envoyer au LLM le contexte de l'écran (titre, champs visibles, sélection) + les actions possibles.
3. LLM renvoie 2-3 suggestions avec action associée (ex. 'Pré-remplir ce devis').
4. L'utilisateur clique → l'action s'exécute (pré-remplissage, brouillon).
5. Feedback pouce haut/bas + 'ne plus suggérer ça' → fine-tuning des suggestions (1371).

**Sorties attendues** :
- Le copilote in-app déployé (panneau + suggestions contextuelles)
- Le contrat de privacy (données écran uniquement)
- Le taux d'adoption des suggestions (métrique)

**Exemple de prompt** :
> « Notre CRM : intègre un copilote in-app (panneau latéral, voit la fiche client ouverte, suggère 'rédiger le mail de relance' en 1 clic, feedback pouce). »

**Cas d'usage** : Productivité in-app, différenciation produit. S'articule avec skills 66 (chatbot), 823 (UX adaptative), 926 (intelligent UI) et 1370 (onboarding).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
