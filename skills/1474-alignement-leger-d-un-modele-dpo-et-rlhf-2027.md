---
num: 1474
date_ajout: "2026-11"
nom: "Alignement leger d'un modele : DPO et RLHF (2027)"
emoji: "🧭"
domaine: "Data & IA"
signal: "Aligner un modèle sur des préférences humaines en 2027 sans RLHF lourd : DPO (Direct Preference Optimization, plus simple, 2 étapes : SFT puis paires préférées/non préférées), ou RLHF classique (reward model + PPO). Utilise quand un modèle répond mal au ton/sécurité. N'utilise pas si le fine-tuning métier suffit (1479)."
mot_cle: "DPO RLHF alignement modèle préférences humaines 2027"
nom_court: "Alignement DPO"
branche: "D14"
synonymes: ["DPO vs RLHF choisir 2027", "paires préférées non préférées", "aligner un modèle sur le ton sécurité"]
cross_refs: [691, 1479, 1473]
tags: ["2027"]
depends_on: [1479]
---

## 1474. 🧭 Alignement leger d'un modele : DPO et RLHF (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Aligner un LLM en 2027 avec DPO (plus simple que RLHF) : après le SFT, collecter des paires (réponse préférée vs rejetée) par des annotateurs, entraîner DPO, et évaluer (sécurité, ton, refus) sur un golden set.

**Quand l'utiliser (triggers)** :
- Le modèle est trop verbeux ou pas assez sûr
- DPO ou RLHF en 2027 ?
- Créer des paires de préférences pour aligner

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es chercheur alignement. Tu expliques DPO (fonction de perte sur paires préférées, pas de reward model séparé, donc plus stable/cheap que RLHF-PPO), la collecte de 1-10k paires (annotateurs ou IA + humain), et l'eval (win rate vs le modèle de base). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le modèle post-SFT
- Les critères d'alignement (ton, sécurité, concision, refus)
- Les annotateurs (humains ou IA supervisée)

**Méthode** :
1. Définir les critères d'alignement (ex. refuse les demandes dangereuses, ton professionnel).
2. SFT de base (1479) puis collecter 1-10k paires (réponse A préférée à B) avec justification.
3. Entraîner DPO (loss sur les paires, beta ~0.1) quelques époques.
4. Évaluer : win rate vs base sur 200 cas + evals sécurité (1395).
5. Itérer : si le modèle refuse trop (over-refusal), ajuster le mix de paires.

**Sorties attendues** :
- Le dataset de paires de préférences
- Le modèle aligné DPO
- Le win rate vs base + evals sécurité

**Exemple de prompt** :
> « Notre modèle fine-tuné répond parfois de façon dangereuse : aligne-le avec DPO (5k paires préférées annotées, eval sécurité avant/après). »

**Cas d'usage** : Alignement sécurité/ton, modèles open weights. S'articule avec skills 691 (FT), 1479 (LoRA), 1473 (distillation).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
