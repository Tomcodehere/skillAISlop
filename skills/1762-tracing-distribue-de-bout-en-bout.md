---
num: 1762
resume: "Instrumenter le tracing distribué (OpenTelemetry spans + contexte W3C traceparent propagé) pour visualiser le parcours complet d'une requête et identifier le service qui la ralentit, avec tail-based sampling pour garder les traces lentes. Étape 1 : Deployer le collecteur OTel avec récepteurs OTLP et export vers le backend de traces."
date_ajout: "2026-11"
nom: "Tracing distribué de bout en bout"
emoji: "🧵"
domaine: "Data"
signal: "Mettre en place le tracing distribué en 2027 : chaque requête utilisateur tracee de bout en bout (front, API, BDD, services externes) via OpenTelemetry et la propagation W3C traceparent, avec échantillonnage head-based et tail-based. Utilise pour comprendre la latence d'un parcours lent. N'utilise pas pour tracer 100 % des requêtes en prod (coût)."
mot_cle: "tracing distribué OpenTelemetry W3C traceparent head-based tail-based sampling 2027"
nom_court: "Tracing distribué"
branche: "D17"
synonymes: ["tracer une requete de bout en bout front API BDD", "propagation contexte W3C traceparent entre microservices", "tail-based sampling : garder les traces lentes automatiquement"]
cross_refs: [1750, 1753, 1752]
tags: ["2027"]
depends_on: [1750]
---

## 1762. 🧵 Tracing distribué de bout en bout (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Instrumenter le tracing distribué (OpenTelemetry spans + contexte W3C traceparent propagé) pour visualiser le parcours complet d'une requête et identifier le service qui la ralentit, avec tail-based sampling pour garder les traces lentes.

**Quand l'utiliser (triggers)** :
- une API met 3 s, on ne sait pas quel appel interne bloque
- latence p99 en hausse, quel microservice est en cause ?
- garder automatiquement les traces des requetes lentes (tail-based)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es ingénieur observabilité. Tu propages le contexte W3C (traceparent) a chaque appel, tu instruments les spans OTel aux frontières (HTTP, BDD, file), et tu configures le tail-based sampling pour ne conserver que les traces lentes ou en erreur. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les services à tracer et leurs appels internes
- Le collecteur OTel (1750)
- Le stockage des traces (Tempo, Jaeger, Datadog)

**Méthode** :
1. Deployer le collecteur OTel avec récepteurs OTLP et export vers le backend de traces.
2. Instrumenter chaque service : span par appel HTTP sortant, requête BDD, message consommé, avec propagation traceparent.
3. Head-based sampling a 10 % en prod + tail-based sampling : garder 100 % des traces avec erreur ou latence > p99.
4. Visualiser : waterfall d'une requête lente, identifier le span qui consomme 80 % du temps.

**Sorties attendues** :
- Le tracing de bout en bout actif sur les parcours critiques
- La politique de sampling (head 10 %, tail 100 % des lentes/erreurs)
- L'analyse d'une requête lente avec le span coupable identifie

**Exemple de prompt** :
> « Requête checkout en 3 s : trace OTel montre front 50 ms, API panier 200 ms, paiement 2,6 s (appel PSP externe) — le tail-based sampling a conservé la trace car latence > p99, diagnostic immédiat. »

**Cas d'usage** : Diagnostic latence multi-services. S'articule avec skills 1750 (OTel GenAI), 1753 (signaux), 1752 (coût cardinalité).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
