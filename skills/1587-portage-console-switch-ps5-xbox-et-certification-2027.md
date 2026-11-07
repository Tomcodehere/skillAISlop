---
num: 1587
nom: "Portage console : Switch, PS5, Xbox et certification (2027)"
emoji: "🎮"
domaine: "Game Dev"
signal: "Porter un jeu sur console en 2027 (Switch/PS5/Xbox) : kit de dev éditeur (demandeEarly), adapté l'UI à la manette (1571) et à la TV (distance 3 m, textes gros), perfs cibles (Switch 30/60 fps, PS5/Xbox 60), gestion mémoire (Switch 4 Go partagés), certification TRC/XR (checklist éditeur : pas de crash, sauvegardes OK 1539, succès console), délai 2-4 semaines. Utilise quand un éditeur est intéressé (1594). N'utilise pas pour PC/mobile."
mot_cle: "portage console Switch PS5 Xbox certification TRC XR kit de dev éditeur"
nom_court: "Portage console"
branche: "D21"
synonymes: ["demander le kit de dev Nintendo/Sony/Microsoft", "certification TRC (Nintendo) / XR (Xbox) : checklist 2 semaines", "Switch : 30 fps et 4 Go de RAM partagés, UI manette TV"]
cross_refs: [1585, 1571, 1594]
tags: ["2027"]
depends_on: [1585]
---

## 1587. 🎮 Portage console : Switch, PS5, Xbox et certification (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Porter un jeu sur console en 2027 : obtenir le kit de dev éditeur, adapter UI/manette (1571) et perfs (Switch 30 fps/4 Go, PS5-Xbox 60 fps), passer la certification (TRC/XR/PS : pas de crash, saves 1539 OK, succès console 1538), délai 2-4 semaines.

**Quand l'utiliser (triggers)** :
- Demander le devkit Nintendo/Sony/Microsoft (6-12 mois avant)
- Switch : diviser les textures (4 Go RAM partagés GPU)
- Certification : checklist TRC/XR, test 2 semaines, submission

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es programmeur portage console. Tu planifies : devkit demandé tôt (1594 pitch), portage technique (API spécifiques, manette 1571, perfs cibles), certification (checklist éditeur : stabilité 30 min, saves, succès 1538, pas de crash, logos), submission 2-4 semaines avant la date. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le jeu PC fini (1579) et un éditeur intéressé (1594)
- Les devkits (Switch/PS5/Xbox)
- Les cibles perfs par console (Switch 30 fps, PS5/Xbox 60 fps/4K)

**Méthode** :
1. Demander les devkits éditeur (Nintendo Switch, Sony PS5, Xbox) 6-12 mois avant la date visée (1594).
2. Portage : remplacer les API PC-specific, manette obligatoire (1571), UI TV (textes gros, lisible à 3 m), perfs : Switch (textures réduites 1585, 30 fps), PS5/Xbox (60 fps, 4K optionnel).
3. Certification : checklist TRC (Nintendo) / XR (Xbox) / PS : jeu stable 30 min sans crash, saves/resume OK (1539), succès débloquent (1538), pas de contenu non conforme, manette débranchée gérée.
4. Submission : build certifié uploadé, tests éditeur (2-4 semaines), correctifs, mise en ligne (store éditeur).
5. Coûts : devkit loué (~2k€/an), royalties 30 % store + éditeur.

**Sorties attendues** :
- Le jeu porté sur console (Switch/PS5/Xbox) avec devkits
- La certification passée (TRC/XR) et la mise en ligne console
- Le planning (devkit → portage → certif 2-4 sem → sortie)

**Exemple de prompt** :
> « Un éditeur veut le jeu sur Switch et PS5 : demande les devkits (1594), porte (manette 1571, UI TV, Switch 30 fps textures réduites 1585), passe la certif TRC/XR (stabilité 30 min, saves 1539, succès 1538), submission 3 semaines avant. »

**Cas d'usage** : Sortie console avec éditeur. S'articule avec skills 1585 (perf), 1571 (manette) et 1594 (pitch éditeur).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
