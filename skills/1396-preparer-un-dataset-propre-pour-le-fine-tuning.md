---
num: 1396
date_ajout: "2026-11"
nom: "Preparer un dataset propre pour le fine-tuning"
emoji: "🧹"
domaine: "Data & IA"
signal: "Preparer un dataset de fine-tuning propre en 2027 : collecte de couples instruction/reponse de qualite, nettoyage (doublons, toxicite, donnees perso RGPD), formatage (JSONL, chat template), repartition train/val/test, et controle de fuite (pas de test dans le train). Utilise quand on fine-tune un modele. N'utilise pas pour l'evaluation seule (voir golden set, skill 1395)."
mot_cle: "préparer dataset propre fine-tuning jsonl"
nom_court: "Dataset fine-tuning"
branche: "D14"
synonymes: ["nettoyer données entraînement llm", "format jsonl chat template 2027", "détecter les fuites train test"]
cross_refs: [691, 238, 92]
tags: ["2027"]
depends_on: [691]
---

## 1396. 🧹 Preparer un dataset propre pour le fine-tuning (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Produire un dataset de fine-tuning propre et conforme en 2027 : 1 000-10 000 exemples de qualité au format JSONL, nettoyé (doublons, données perso, toxicité), réparti train/val/test sans fuite.

**Quand l'utiliser (triggers)** :
- Préparer mes données pour fine-tuner un LLM en 2027 (format JSONL)
- Nettoyer un dataset d'entraînement : doublons, RGPD, fuite train/test
- Combien d'exemples faut-il pour un fine-tuning efficace ?

**Hors périmètre** :
- L'entraînement lui-même (GPU, orchestration)
- L'évaluation du modèle fine-tuné (skill 1395)

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (ordres de grandeur : quelques milliers d'exemples de qualité suffisent souvent).
- GF-02 : AUCUNE donnée personnelle dans le dataset (RGPD) — anonymisation systématique.
- GF-03 : split train/val/test aleatoire avec vérification de non-chevauchement (fuite).

**Instructions système** :
Tu es data engineer specialise préparation LLM. Tu appliques le pipeline : collecte → nettoyage (doublons exacts/near, longueur, langue, toxicité, PII) → formatage JSONL selon le chat template du modèle → split 90/5/5 → contrôle de fuite, et tu restes factuel. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les données brutes (conversations, documents, Q/R)
- Le modèle cible et son chat template
- Les exigences métier (style, format de sortie)

**Méthode** :
1. Collecter/curater les exemples instruction → réponse (qualité > quantité).
2. Nettoyer : supprimer doublons (hash + fuzzy), PII (regex + NER), toxicité, exemples trop longs/courts.
3. Formater en JSONL conforme au chat template du modèle (messages system/user/assistant).
4. Split aléatoire 90/5/5 (train/val/test) et vérifier l'absence de fuite (similarité train vs test).
5. Valider : faire lire 20 exemples au modèle de base, garder la version du dataset (vX).

**Sorties attendues** :
- Le dataset JSONL nettoyé et versionné
- Le rapport de nettoyage (nb supprimés et pourquoi)
- Le split train/val/test avec preuve de non-fuite

**Exemple de prompt** :
> « Je fine-tune Mistral sur notre support client : prépare un dataset propre de 5 000 tickets (JSONL, nettoyage RGPD, split train/test sans fuite). »

**Cas d'usage** : Fine-tuning de LLM/SLM, spécialisation métier, distillation. S'articule avec skills 691 (fine-tuning), 238 (annotation), 92 (nettoyage données), 96 (datasets) et 1234 (contrats de données).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
