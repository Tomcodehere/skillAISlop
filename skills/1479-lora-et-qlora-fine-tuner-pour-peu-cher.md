---
num: 1479
resume: "Fine-tuner un LLM à bas coût en 2027 avec LoRA (r=8-16, ~1 % des params entraînés) ou QLoRA (modèle Q4 en mémoire + LoRA : un 70B tient sur 24 Go de VRAM), avec eval avant/après. Étape 1 : Préparer le dataset propre (1396) et le modèle (GGUF/hub)."
lang: "fr"
date_ajout: "2026-11"
nom: "LoRA et QLoRA : fine-tuner pour peu cher"
emoji: "💰"
domaine: "Data & IA"
signal: "Fine-tuner un LLM à bas coût en 2027 avec LoRA (on n'entraîne que des matrices de rang faible, ~1 % des paramètres, le reste gelé) ou QLoRA (modèle quantizé Q4 en mémoire + LoRA, tient sur 1 GPU 24 Go pour un 70B). Utilise quand un fine-tuning complet est trop cher. N'utilise pas pour l'alignement de préférences (voir DPO 1474)."
mot_cle: "LoRA QLoRA fine-tuning pas cher rang faible quantizé"
nom_court: "LoRA/QLoRA"
branche: "D14"
synonymes: ["fine-tuner 70B sur 1 GPU 24 Go", "LoRA rang 8 ou 16", "QLoRA Q4 + LoRA mémoire"]
cross_refs: [691, 1396, 1470]
tags: ["2027"]
depends_on: [1396]
---

## 1479. 💰 LoRA et QLoRA : fine-tuner pour peu cher (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Fine-tuner un LLM à bas coût en 2027 avec LoRA (r=8-16, ~1 % des params entraînés) ou QLoRA (modèle Q4 en mémoire + LoRA : un 70B tient sur 24 Go de VRAM), avec eval avant/après.

**Quand l'utiliser (triggers)** :
- Un fine-tuning complet de 70B coûte trop cher
- QLoRA : 70B sur une RTX 4090
- LoRA r=8 ou r=16 ? quelle différence

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es ML engineer efficacité. Tu expliques LoRA (W = W0 + B·A, rang r, alpha), QLoRA (4-bit NF4 + LoRA + double quant), les réglages (r=16, alpha=32, lr=2e-4, target modules q/k/v/o), et l'eval obligatoire avant/après (golden set 1395). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le modèle de base (licence permissive)
- Le dataset propre (1396)
- Le GPU et la VRAM disponibles

**Méthode** :
1. Préparer le dataset propre (1396) et le modèle (GGUF/hub).
2. Configurer LoRA : r=16, lora_alpha=32, target q_proj/v_proj, lr 2e-4, 1-3 époques.
3. QLoRA si VRAM limitée : quantization 4-bit NF4 + LoRA (bitsandbytes).
4. Entraîner (monitoring loss, early stop) et merger ou garder l'adaptateur.
5. Évaluer vs base sur golden set (1395) : viser +10 pts sans régression générale.

**Sorties attendues** :
- L'adaptateur LoRA entraîné (ou modèle mergé)
- Les hyperparams retenus (r, alpha, lr)
- L'eval avant/après (golden set)

**Exemple de prompt** :
> « Fine-tuner un 70B pour notre domaine coûte 20k€ en full FT : fais-le en QLoRA (Q4 + LoRA r=16 sur 1 GPU 24 Go) et évalue vs base. »

**Cas d'usage** : Spécialisation métier à coût maîtrisé. S'articule avec skills 691 (fine-tuning), 1396 (dataset), 1470 (versioning) et 1395 (evals).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
