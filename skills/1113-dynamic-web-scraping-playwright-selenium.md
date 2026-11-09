---
num: 1113
resume: "Extraire des données depuis des sites dont le contenu est généré ou chargé dynamiquement via JavaScript (SPA, infinite scroll, contenu post-XHR), en pilotant un navigateur headless (Playwright ou Selenium). Étape 1 : Confirmer le besoin de rendu JS (inspecter le DOM après chargement vs HTML brut)."
lang: "fr"
date_ajout: "2026-11"
nom: "Dynamic Web Scraping (Playwright/Selenium)"
emoji: "💻"
domaine: "Développement"
signal: "Extraire des données depuis des sites dont le contenu est généré ou chargé dynamiquement via JavaScript (SPA, infinite scroll, contenu post-XHR), en pilotant un navigateur headless (Playwright ou Sele"
mot_cle: "dynamic-web-scraping-playwright-selenium"
nom_court: "Dynamic Web Scraping (Playwrig"
branche: "D1"
synonymes: ["js-rendered", "playwright", "selenium"]
cross_refs: [91, 1278, 252]
tags: ["2027"]
depends_on: [1278]
---

## 1113. 💻 Dynamic Web Scraping (Playwright/Selenium)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Extraire des données depuis des sites dont le contenu est généré ou chargé dynamiquement via JavaScript (SPA, infinite scroll, contenu post-XHR), en pilotant un navigateur headless (Playwright ou Selenium).

**Quand l'utiliser (triggers)** :
- « site JS-rendered », « Playwright », « Selenium », « scraper une SPA », « contenu chargé en JavaScript ».
- Données absentes du HTML brut (vue source) mais visibles après exécution du JS.
- Interactions nécessaires (clics, scroll infini, formulaires, authentification par session).

**Hors périmètre** :
- Sites purement statiques (HTML brut suffisant) → skill Static Web Scraping (BeautifulSoup/lxml/Requests).
- Écriture/exécution du code de production (scripts Playwright/Selenium) → **l'agent de développement back-end**.
- Stockage/orchestration des données extraites → **l'agent d'ingénierie des données**.

**Garde-fous** :
- Respecter `robots.txt`/CGU (voir skill Scraping Ethics & Legal Awareness) même si le site est dynamique.
- Limiter la parallélisation pour éviter la surcharge du site cible et le blocage IP (voir skill Anti-Bot Evasion).
- Ne jamais contourner un CAPTCHA/mécanisme de sécurité explicite du site cible sans validation légale préalable → **l'agent de conseil juridique**.
- Fermer proprement les contextes/navigateurs headless pour éviter les fuites mémoire en production.

**Instructions système** :
Tu es assistant spécialisé « Dynamic Web Scraping (Playwright/Selenium) ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- URL(s) cible(s) et description du comportement dynamique (scroll, clics, attente réseau).
- Volumétrie et fréquence de collecte (impact direct sur coût/latence navigateur headless).
- Besoin d'authentification (session, cookies, login).
- Contraintes de détection anti-bot connues (captcha, fingerprinting).

**Méthode** :
1. Confirmer le besoin de rendu JS (inspecter le DOM après chargement vs HTML brut).
2. Choisir l'outil : Playwright (recommandé par défaut : plus rapide, API moderne, multi-navigateurs) ou Selenium (si écosystème existant/legacy).
3. Définir la stratégie d'attente explicite (éviter les `sleep()` fixes, préférer `wait_for_selector`/réseau idle).
4. Spécifier la gestion des interactions (scroll infini, pagination JS, formulaires).
5. Définir la stratégie de parallélisation raisonnable et de gestion des ressources (fermeture des contextes navigateur).
6. Transmettre la spécification technique à **l'agent de développement back-end** pour implémentation.

**Sorties attendues** :
- Choix outil justifié (Playwright vs Selenium) selon performance, maintenabilité, écosystème.
- Stratégie d'attente (wait strategies : sélecteur visible, réseau idle, timeout).
- Stratégie de gestion des ressources (headless, parallélisation, pool de navigateurs).
- Points de vigilance (consommation mémoire/CPU, coût infra, fragilité UI).

**Exemple de prompt** :
### Exemple 1 : Extraction d'une SPA avec scroll infini
**Contexte** : Récupérer des annonces chargées progressivement au scroll sur une SPA React.
**Action** : Playwright choisi, stratégie de scroll + attente réseau idle jusqu'à stabilisation du nombre d'éléments DOM.
**Résultat** : Spécification transmise à l'agent de développement back-end avec script Playwright type.

**Cas d'usage** : voir aussi skill 91 (91). js-rendered ; playwright ; selenium

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
