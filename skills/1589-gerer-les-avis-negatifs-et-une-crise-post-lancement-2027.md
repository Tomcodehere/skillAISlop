---
num: 1589
nom: "Gerer les avis negatifs et une crise post-lancement (2027)"
emoji: "💬"
domaine: "Game Dev"
signal: "Gérer les avis Steam négatifs et une mini-crise post-lancement en 2027 : ne pas supprimer (interdit), répondre publiquement et calmement aux avis techniques (en moins de 24 h), prioriser les bugs bloquants (hotfix 1578 sous 48 h), communiquer (devlog 1596 + patch notes claires), ne pas acheter d'avis. Utilise quand le lancement se passe mal. N'utilise pas pour la communication marketing normale (1596)."
mot_cle: "avis négatifs Steam répondre hotfix 48 h crise post-lancement communication"
nom_court: "Avis/crise"
branche: "D10"
synonymes: ["répondre aux avis Steam négatifs en 24 h calmement", "hotfix sous 48 h si bug bloquant au lancement", "devlog transparent (1596) + patch notes claires (1578)"]
cross_refs: [1578, 1596, 1540]
tags: ["2027"]
depends_on: [1578]
---

## 1589. 💬 Gerer les avis negatifs et une crise post-lancement (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Gérer une mauvaise réception au lancement en 2027 : répondre aux avis négatifs Steam en < 24 h (calme, factuel, jamais supprimé), hotfix des bugs bloquants sous 48 h (branche 1578), communiquer (devlog 1596 + patch notes), et surveiller le ratio d'avis (1580).

**Quand l'utiliser (triggers)** :
- 50 avis négatifs 'ne démarre pas' au lancement
- Répondre aux avis Steam sans être agressif
- Hotfix 48 h + annonce devlog (1596) quand ça va mieux

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es community manager crise. Tu appliques : réponse publique à chaque avis technique en < 24 h (remercier, dire ce qui est corrigé et quand, lien patch notes 1578), hotfix branche 1578 sous 48 h pour les bloquants, devlog transparent (1596), jamais d'achat d'avis ni de suppression. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les avis Steam (1580) et le ratio (très négatif < 70 %)
- Les bugs remontés (crash log 1586, playtests 1598)
- Le canal de communication (devlog 1596, Discord)

**Méthode** :
1. Trier les avis : bloquants (crash/démarrage) > gênants (perf 1585) > suggestions (contenu).
2. Répondre publiquement en < 24 h : merci + 'corrigé dans le patch du JJ/MM (lien 1578)' ou 'pris en compte pour la vX'. Jamais agressif, jamais supprimé (interdit Steam).
3. Hotfix : bug bloquant → branche hotfix (1578), build en 48 h, patch notes claires (quoi, pourquoi).
4. Communiquer : devlog 1596 'on vous écoute, voici le plan', Discord, pas de langue de bois.
5. Surveiller : ratio d'avis qui repasse > 70 % en 2 semaines; si < 50 %, envisager remboursement massif (1582) ou retrait temporaire.

**Sorties attendues** :
- Les avis répondus en < 24 h + hotfix 48 h
- Le devlog de crise publié (1596)
- Le ratio d'avis surveillé et remonté

**Exemple de prompt** :
> « Lancement raté : 40 % d'avis négatifs 'ne démarre pas' (crash 1586). Réponds à tous en 24 h, hotfix branche 1578 en 48 h, devlog transparent (1596) avec le plan, surveille le ratio (1580) qui remonte > 70 % en 2 semaines. »

**Cas d'usage** : Post-lancement difficile. S'articule avec skills 1578 (versions), 1596 (communauté) et 1540 (analytics crash-free).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
