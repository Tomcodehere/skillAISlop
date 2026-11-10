---
num: 1438
resume: "Déployer un SLM quantizé (GGUF Q4) en local sur mobile/edge en 2027 (llama.cpp, MediaPipe, MLX) : fonctionnement offline total, latence inférieur à 2 s, impact batterie mesuré, privacy totale. Étape 1 : Choisir le modèle SLM (3-8B params) et le format GGUF quantizé Q4."
lang: "fr"
date_ajout: "2026-11"
nom: "Deployer un SLM on-device (mobile/edge)"
emoji: "📱"
domaine: "IA / Prompting"
signal: "Déployer un petit modèle (SLM) directement sur mobile/edge en 2027 : modèle quantizé (GGUF/Q4), runtime local (llama.cpp, MediaPipe, MLX sur Mac), offline total, latence mesurée, batterie. Utilise quand la privacy ou l'offline est critique. N'utilise pas pour les grosses tâches cloud."
mot_cle: "SLM on-device mobile edge quantizé GGUF llama.cpp offline"
nom_court: "SLM on-device"
branche: "D14"
synonymes: ["modèle local téléphone 2027", "llama.cpp mobile offline", "quantization GGUF Q4 batterie"]
cross_refs: [903, 943, 331]
tags: ["2027"]
depends_on: [903]
---

## 1438. 📱 Deployer un SLM on-device (mobile/edge, 2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Déployer un SLM quantizé (GGUF Q4) en local sur mobile/edge en 2027 (llama.cpp, MediaPipe, MLX) : fonctionnement offline total, latence < 2 s, impact batterie mesuré, privacy totale.

**Quand l'utiliser (triggers)** :
- Faire tourner un LLM sur mon téléphone en offline
- llama.cpp ou MediaPipe sur mobile ?
- Modèle quantizé Q4 vs Q8 : latence/batterie

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es ingénieur IA embarquée. Tu compares les runtimes (llama.cpp Android/iOS, MediaPipe LLM Inference, MLX Mac), la quantization (Q4_K_M = bon compromis), et tu mesures latence + conso batterie sur l'appareil cible. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'appareil cible (Android/iOS/Mac/edge)
- Le cas d'usage offline (résumé, classification, assistant)
- La taille max du modèle (ex. < 4 Go)

**Méthode** :
1. Choisir le modèle SLM (3-8B params) et le format GGUF quantizé Q4.
2. Choisir le runtime adapté à l'appareil (llama.cpp, MediaPipe, MLX).
3. Intégrer dans l'app (chargement lazy, cache du modèle).
4. Mesurer : latence tokens/s, RAM, batterie sur 100 requêtes.
5. Valider la qualité vs le cloud sur 20 cas (acceptable ?).

**Sorties attendues** :
- Le SLM déployé offline sur l'appareil
- Les perfs mesurées (latence, RAM, batterie)
- Le comparatif qualité local vs cloud

**Exemple de prompt** :
> « Je veux un assistant qui marche dans le métro (offline) sur Android : déploie un SLM quantizé Q4 avec llama.cpp (latence et batterie mesurées). »

**Cas d'usage** : Privacy (données sensibles), offline, coûts. S'articule avec skills 903 (SLM PME), 943 (IA on-device) et 331 (modèles légers).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
