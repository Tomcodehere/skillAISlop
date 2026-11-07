---
num: 1548
date_ajout: "2026-11"
nom: "Chat in-game et moderation automatique"
emoji: "💬"
domaine: "Game Dev"
signal: "Ajouter un chat in-game en 2027 : chat texte (général/équipe/privé), filtre de vulgarité (liste + LLM léger 1490), anti-spam (rate limit 1 msg/2 s), signalement + mute/ban par les joueurs (vote), modération auto des insultes, conformité mineurs (1587). Utilise pour tout jeu multi. N'utilise pas pour un chat vocal (1569)."
mot_cle: "chat in-game filtre vulgarité anti-spam signalement mute ban vote"
nom_court: "Chat in-game"
branche: "D23"
synonymes: ["filtrer les insultes automatiquement", "rate limit 1 message 2 secondes anti-spam", "signaler un joueur toxique → mute/ban vote"]
cross_refs: [1490, 1543, 1587]
tags: ["2027"]
depends_on: [1543]
---

## 1548. 💬 Chat in-game et moderation automatique (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Ajouter un chat in-game en 2027 : canaux (général/équipe/privé), filtre de vulgarité (liste + classificateur), rate limit anti-spam, signalement avec vote mute/ban, historique des sanctions, conformité mineurs (1587).

**Quand l'utiliser (triggers)** :
- Filtrer automatiquement les insultes dans le chat
- Limiter à 1 message/2 s (anti-spam)
- Signaler un joueur → 3 signalements = mute auto 24 h

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es programmeur chat modéré. Tu fais : canaux + messages horodatés, filtre (liste de mots + score LLM 1490) → masque ou bloque, rate limit serveur (1 msg/2 s, burst 3), signalement → compteur par joueur → mute 24 h à 3, ban à 10, log pour la modération humaine. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les canaux (général, équipe, privé)
- La liste de mots interdits + seuil LLM
- Les seuils de sanction (3 mute, 10 ban)

**Méthode** :
1. Chat : envoi {canal, texte, auteur, ts}; serveur valide (rate limit 1/2 s, longueur 200 car.), filtre vulgarité (liste + LLM 1490 score > 0,8 → masqué '[modéré]').
2. Signalement : un joueur signale un message → +1 au compteur de l'auteur; 3 signalements → mute 24 h; 10 → ban 7 j; log modération.
3. UI : fenêtre chat (Echap), canaux onglets, clic droit joueur → signaler/mute/bloquer localement.
4. Majuscules excessives / spam de liens → ralentir (cooldown croissant).
5. Conformité : filtre renforcé si compte < 18 ans (1587), pas de chat privé adulte-mineur.

**Sorties attendues** :
- Le chat in-game avec filtres et rate limit
- Le système de signalement/mute/ban
- Les logs de modération + conformité mineurs

**Exemple de prompt** :
> « Le chat général est toxique : ajoute filtre de vulgarité (liste + LLM), rate limit 1 msg/2 s, signalement → mute 24 h à 3 signalements, ban à 10, filtre renforcé pour les -18 ans. »

**Cas d'usage** : Tout jeu multijoueur avec chat. S'articule avec skills 1490 (modération IA), 1543 (anti-triche) et 1587 (RGPD mineurs).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
