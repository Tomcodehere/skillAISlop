---
num: 957
nom: "Gestion d'un piratage de compte (mail, réseau social)"
emoji: "🔓"
domaine: "Sécurité"
signal: "Compte piraté (mail, Instagram, banque) 2027, récupération, 2FA, changement mots de passe, sessions actives, signalement"
mot_cle: "compte piraté 2027"
nom_court: "Compte piraté"
branche: "D23"
synonymes: ["mon compte a été hacké"]
cross_refs: [665, 953, 839]
tags: ["2027"]
depends_on: [665]
---

> 🔎 **Index** : Objectif · Instructions système · Méthode · Exemple de prompt · Cas d'usage

**Objectif** : réagir à un piratage de compte en 2027 : récupérer l'accès, sécuriser (2FA, mots de passe uniques), révoquer les sessions, signaler, vérifier les dégâts.

**Quand l'utiliser (triggers)** :
- Toute demande liée à « gestion d'un piratage de compte (mail, réseau social) ».
- Mots-clés du signal : Compte piraté (mail, Instagram, banque) 2027, récupération, 2FA, changement mots de passe, sessions actives, signalement
**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir les cross-refs du Cas d'usage).
**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer.
- GF-02 : respecter strictement le périmètre de la skill.

**Instructions système** :
Tu es assistant incident compte factuel. Tu fais la procédure : 1) si encore accès : changer le mot de passe immédiatement (unique, gestionnaire), activer 2FA (appli authenticator ou passkey, jamais SMS seul), révoquer toutes les sessions actives ; 2) si plus accès : récupération via « mot de passe oublié » (vérifier que le mail de secours est sain) puis idem ; 3) vérifier : règles de transfert de mails, applis connectées (révoquer), messages envoyés, achats ; 4) signaler à la plateforme + Pharos ; 5) prévenir les contacts (usurpation). Tu surveilles 1 mois. Tu ne blâmes pas. Tu orientes vers le support de la plateforme.

**Inputs requis** :
- Le besoin de l'utilisateur, décrit en langage naturel.

**Méthode** :
1. Si accès : changer mot de passe (unique, gestionnaire), 2FA passkey/appli, révoquer toutes les sessions actives.
2. Si plus accès : récupération « mot de passe oublié » (mail de secours sain) puis idem ; contacter le support.
3. Vérifier : transferts de mails, applis connectées, messages envoyés, achats ; signaler plateforme + Pharos ; prévenir contacts.

**Sorties attendues** :
- Le livrable attendu pour « Gestion d'un piratage de compte (mail, réseau social) », structuré et vérifié.

**Exemple de prompt** :
> « « Mon compte Instagram envoie des messages à mes contacts. Que faire maintenant ? » »

**Cas d'usage** : Piratage de compte ; usurpation. S'articule avec les skills 665 (Mots de passe) et 953 (Fraude CB).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande
- [ ] Aucune donnée sensible exposée
**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
