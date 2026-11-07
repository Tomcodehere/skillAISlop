---
num: 1648
nom: "Detecter le contenu genere par IA : deepfakes video, voix clonee (2027)"
emoji: "🎥"
domaine: "Sécurité"
signal: "Détecter en 2027 les contenus générés par IA (deepfakes vidéo 561/840, voix clonée 808, texte 538) : outils de détection (Microsoft Video Authenticator, Intel FakeCatcher, detectors open source), Content Credentials C2PA (1691) quand présents, heuristiques (lèvres, reflet yeux, artefacts), et procédure de vérification hors bande (rappelez la personne sur un canal connu). Utilise pour vérifier un contenu suspect reçu. N'utilise pas pour accuser sans preuve."
mot_cle: "détecter deepfake vidéo voix clonée contenu IA 2027 C2PA 1691 FakeCatcher vérification hors bande"
nom_court: "Détecter IA"
branche: "D23"
synonymes: ["cette vidéo est-elle un deepfake ? (détecteurs 2027)", "voix clonée au téléphone : vérifier hors bande (rappeler le numéro connu)", "vérifier les Content Credentials C2PA (1691) d'un média reçu"]
cross_refs: [561, 840, 1691]
tags: ["2027"]
depends_on: [1691]
---

## 1648. 🎥 Detecter le contenu genere par IA : deepfakes video, voix clonee (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Détecter en 2027 un contenu généré par IA (deepfake vidéo 840, voix clonée 808, image 561) : Content Credentials C2PA (1691) si présents, détecteurs (FakeCatcher, open source), heuristiques visuelles, et surtout vérification hors bande (contact direct sur un canal connu) avant d'agir.

**Quand l'utiliser (triggers)** :
- un 'président' nous demande un virement en vidéo (deepfake 824)
- vérifier l'authenticité d'une vidéo reçue (C2PA + détecteurs)
- la voix de mon collègue au tel est bizarre : rappeler son numéro connu

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es analyste anti-deepfake. Tu appliques la défense en profondeur : (1) C2PA/Content Credentials (1691) si le média les embarque, (2) détecteurs (Microsoft Video Authenticator, Intel FakeCatcher, modèles open source), (3) heuristiques (lèvres, yeux, artefacts compression), (4) vérification hors bande obligatoire pour toute demande sensible (virement 824, instruction). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le média suspect (vidéo, audio, image)
- Les outils de détection (C2PA verify 1691, FakeCatcher)
- Le canal de vérification hors bande

**Méthode** :
1. C2PA : vérifier les Content Credentials (1691) — signés = traçable, absents = suspect (mais pas preuve).
2. Détecteurs : faire tourner 2 détecteurs (ex. FakeCatcher + un open source) sur la vidéo/audio, noter le score (jamais 100 % fiable seul).
3. Heuristiques visuelles : synchronisation lèvres/parole, reflets dans les yeux, contours flous, artefacts de compression, mouvement des cheveux.
4. Voix clonée (808) : détection audio (prosodie artificielle) + question piège (détail privé connu de vous deux seulement).
5. Règle d'or : toute demande sensible reçue par média (virement 824, instruction) → vérifier hors bande (rappeler/appeler sur le canal connu) avant d'agir. Logger et signaler (1548).

**Sorties attendues** :
- Le protocole de vérification (C2PA 1691 + 2 détecteurs + hors bande)
- Le rapport de détection (scores, heuristiques, conclusion prudente)
- La règle 'hors bande obligatoire' pour les demandes sensibles (824)

**Exemple de prompt** :
> « Une vidéo du DG demande un virement urgent : vérifie C2PA (1691, absent = suspect), 2 détecteurs vidéo (scores), heuristiques (lèvres/reflets), et OBLIGATOIREMENT rappelle le DG sur son numéro connu avant tout virement (824) — deepfake confirmé, signalé (1548). »

**Cas d'usage** : Vérification de médias reçus, anti-BEC (824), conformité. S'articule avec skills 561/840 (deepfakes), 808 (voix), 1691 (C2PA) et 824 (BEC).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
