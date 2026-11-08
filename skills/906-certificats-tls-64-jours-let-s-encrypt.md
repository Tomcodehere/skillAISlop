---
num: 906
date_ajout: "2026-11"
nom: "Certificats TLS 64 jours (Let's Encrypt)"
emoji: "🔒"
domaine: "Développement"
signal: "Renouvellement automatique certificats TLS, Let's Encrypt passe à 64 jours le 10 février 2027, ACME, Certbot, test staging"
mot_cle: "certificat tls 64 jours"
nom_court: "TLS 64j"
branche: "D16"
synonymes: ["lets encrypt 2027"]
cross_refs: [507, 512, 918]
tags: ["2027"]
depends_on: [1871]
---

> 🔎 **Index** : Objectif · Instructions système · Méthode · Exemple de prompt · Cas d'usage

**Objectif** : préparer le passage des certificats TLS à 64 jours (Let's Encrypt, 10 février 2027, puis 45 jours en 2028) avec renouvellement ACME automatique.

**Quand l'utiliser (triggers)** :
- Toute demande liée à « certificats tls 64 jours (let's encrypt, fév. 2027) ».
- Mots-clés du signal : Renouvellement automatique certificats TLS, Let's Encrypt passe à 64 jours le 10 février 2027, ACME, Certbot, test stagi
**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir les cross-refs du Cas d'usage).
**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer.
- GF-02 : respecter strictement le périmètre de la skill.

**Instructions système** :
Tu es admin sys factuel. Tu rappelles le calendrier annoncé : 10 février 2027 = 64 jours par défaut (profil classic), 16 février 2028 = 45 jours ; staging déjà en 64 jours depuis le 14 octobre 2026 ; dernier certificat 90 jours expire le 11 mai 2027 ; aucune révocation. Tu vérifies : renouvellement automatique ACME (Certbot/acme.sh) actif et testé, pas de renouvellement codé en dur sur une date ; tester sur staging d'abord ; surveiller l'expiration (monitoring  « « Mon site a un certificat Let's Encrypt renouvelé tous les 3 mois en cron. Que dois-je changer avant février 2027 ? » »

**Cas d'usage** : Admin sys, hébergeur, site perso/pro. S'articule avec les skills 507 (HTTPS/TLS) et 512 (HSTS).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande
- [ ] Aucune donnée sensible exposée
**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

**Inputs requis** :
- Le besoin de l'utilisateur, en langage naturel.

**Méthode** :
1. Clarifier « Certificats TLS 64 jours (Let's Encrypt, fév. 2027) ».
2. Appliquer la procédure.
3. Livrer et vérifier.

**Sorties attendues** :
- Livrable pour « Certificats TLS 64 jours (Let's Encrypt, fév. 2027) », structuré et vérifié.

**Exemple de prompt** :
> « Certificats TLS 64 jours (Let's Encrypt, fév. 2027) : décris ta situation concrète. »
