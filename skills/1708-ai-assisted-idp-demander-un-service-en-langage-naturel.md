---
num: 1708
resume: "Intégrer l'IA dans l'IDP en 2027 (92 % des CIO) : demande en langage naturel ('service Node + Postgres + observabilité') → l'IDP génère repo + manifests + pipeline depuis un golden path (1701), et un humain valide la PR (1401) avant merge. Étape 1 : Chat dans le portail : 'nouveau service Node + Postgres + observabilité en prod'."
lang: "fr"
date_ajout: "2026-11"
nom: "AI-assisted IDP : demander un service en langage naturel"
emoji: "🤖"
domaine: "Produit & IA"
signal: "Intégrer l'IA dans l'IDP en 2027 (92 % des CIO prévoient d'y intégrer l'IA) : un dev demande en langage naturel 'je veux un service Node connecté à Postgres avec observabilité', l'IDP génère le repo, les manifests et le pipeline depuis un golden path (1701). L'humain valide la PR (1401) avant merge. N'utilise pas pour supprimer la revue humaine."
mot_cle: "IDP assisté par IA 2027 demande en langage naturel génère repo manifests pipeline golden path 92% CIO"
nom_court: "IDP+IA"
branche: "D14"
synonymes: ["demander un service en langage naturel dans l'IDP (92 % des CIO 2027)", "l'IDP génère repo + CI + k8s depuis un golden path", "l'IA génère, l'humain valide la PR (1401) avant merge"]
cross_refs: [1700, 1701, 1627]
tags: ["2027"]
depends_on: [1700]
---

## 1708. 🤖 AI-assisted IDP : demander un service en langage naturel (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Intégrer l'IA dans l'IDP en 2027 (92 % des CIO) : demande en langage naturel ('service Node + Postgres + observabilité') → l'IDP génère repo + manifests + pipeline depuis un golden path (1701), et un humain valide la PR (1401) avant merge.

**Quand l'utiliser (triggers)** :
- 'je veux un service Node connecté à Postgres' en langage naturel dans le portail
- l'IDP génère le repo+CI+manifests depuis le golden path
- l'humain valide la PR avant merge (jamais auto-merge)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es platform engineer IA. Tu connectes un LLM au portail (Backstage plugin ou chat interne 66), le prompt mappe la demande vers le golden path le plus proche, génère la PR, et la revue humaine (1401) + les checks CI (1413) restent obligatoires avant merge. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'IDP (1700) et ses golden paths (1701)
- Le LLM (API ou local 1633)
- La politique : revue humaine obligatoire

**Méthode** :
1. Chat dans le portail : 'nouveau service Node + Postgres + observabilité en prod'.
2. LLM → choix du golden path le plus proche (1701) + génération du repo (code + CI 1413 + manifests k8s + claim Crossplane 1703) + PR.
3. Humains : revue de la PR (1401) + checks CI obligatoires (tests, SAST 1646, policies 1705) avant merge — jamais auto-merge.
4. Feedback : le dev note la qualité de la génération → améliore le template (golden path).
5. Métriques : temps demande→PR (objectif minutes), taux de merge après review, satisfaction (1698).

**Sorties attendues** :
- Le chat IDP+IA opérationnel (demande LN → PR golden path)
- La PR générée avec revue humaine (1401) + CI (1413) obligatoires
- Les métriques (temps demande→PR en minutes, taux merge)

**Exemple de prompt** :
> « Les devs demandent 'un service Node+Postgres' dans le portail : connecte un LLM à Backstage (92 % des CIO en 2027) — demande en langage naturel → PR générée depuis le golden path (1701), revue humaine (1401) + CI (1413) avant merge, objectif minutes. »

**Cas d'usage** : IDP mature. S'articule avec skills 1700 (IDP), 1701 (golden paths), 1627 (BC agent) et 1401 (review).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
