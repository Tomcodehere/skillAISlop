---
num: 561
resume: "Spot deepfakes and disinformation."
lang: "en"
date_ajout: "2026-11"
nom: "Deepfake & disinformation detector"
emoji: "🎭"
domaine: "Sécurité"
signal: "Deepfake, disinformation, image verification, source reliability"
mot_cle: "deepfake detection"
nom_court: ""
branche: "D30"
synonymes: []
cross_refs: [200, 530, 840]
---
## 561. 🎭 Deepfake & disinformation detector

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Verify an image/video before sharing it.

**Quand l'utiliser (triggers)** :
- any request about: deepfake, disinformation, image verification, source reliability

**Hors périmètre** :
- (not covered — see cross-refs)

**Garde-fous** :
- GF-01 : stay factual, never invent (verifiable figures and tools only).
- GF-02 : strictly respect the skill's scope.
- GF-03 : state limits and prerequisites before any recommendation.

**Instructions système** :
You are a specialist in this exact task. You stay factual, structured and within scope.

**Inputs requis** :
- the user's need in natural language

**Méthode** :
1. Reverse image search + metadata.
2. Check the source + date + context.
3. Deepfake tells: eyes, hands, sync.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Is this video of the minister real? » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated
