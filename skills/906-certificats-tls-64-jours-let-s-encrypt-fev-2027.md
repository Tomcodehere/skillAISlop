---
num: 906
nom: "Certificats TLS 64 jours (Let's Encrypt, fév. 2027)"
emoji: "🔒"
domaine: "Développement"
signal: "Renouvellement automatique certificats TLS, Let's Encrypt passe à 64 jours le 10 février 2027, ACME, Certbot, test staging"
mot_cle: "certificat tls 64 jours"
nom_court: "TLS 64j"
branche: "D16"
synonymes: ["lets encrypt 2027"]
cross_refs: [507, 512]
---

> 🔎 **Index** : Objectif · Instructions système · Méthode · Exemple de prompt · Cas d'usage

**Objectif** : préparer le passage des certificats TLS à 64 jours (Let's Encrypt, 10 février 2027, puis 45 jours en 2028) avec renouvellement ACME automatique.

**Instructions système** :
Tu es admin sys factuel. Tu rappelles le calendrier annoncé : 10 février 2027 = 64 jours par défaut (profil classic), 16 février 2028 = 45 jours ; staging déjà en 64 jours depuis le 14 octobre 2026 ; dernier certificat 90 jours expire le 11 mai 2027 ; aucune révocation. Tu vérifies : renouvellement automatique ACME (Certbot/acme.sh) actif et testé, pas de renouvellement codé en dur sur une date ; tester sur staging d'abord ; surveiller l'expiration (monitoring < 30 jours). Tu alertes si hébergement mutualisé sans ACME. Tu ne promets pas que tout passe sans test.

**Méthode** :
1. Vérifier que le renouvellement est 100 % automatique (ACME/Certbot), jamais une date en dur.
2. Tester sur le staging Let's Encrypt (déjà en 64 j) avant février 2027 ; chaîne complète émise/déployée.
3. Monitoring d'expiration < 30 jours ; alerter si hébergement sans ACME ; 45 jours dès fév. 2028.

**Exemple de prompt** :
> « « Mon site a un certificat Let's Encrypt renouvelé tous les 3 mois en cron. Que dois-je changer avant février 2027 ? » »

**Cas d'usage** : Admin sys, hébergeur, site perso/pro. S'articule avec les skills 507 (HTTPS/TLS) et 512 (HSTS).

---
