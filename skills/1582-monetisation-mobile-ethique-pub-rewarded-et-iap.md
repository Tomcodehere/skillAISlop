---
num: 1582
date_ajout: "2026-11"
nom: "Monetisation mobile éthique : pub rewarded et IAP"
emoji: "📱"
domaine: "Game Dev"
signal: "Monétiser un jeu mobile en 2027 sans dark patterns (régulé UE 2027) : publicité rewarded (choisie par le joueur, jamais forcée, max 3/jour), IAP cosmétiques uniquement (jamais pay-to-win, 1585), pas de pop-up agressive, prix transparents, remboursement facile, mineurs protégés (1587). Utilise pour un F2P mobile. N'utilise pas pour un jeu premium payant (prix fixe 1581)."
mot_cle: "monétisation mobile éthique rewarded IAP cosmétique pas pay-to-win dark patterns"
nom_court: "Monétisation éthique"
branche: "D21"
synonymes: ["pub rewarded choisie par le joueur max 3/jour", "IAP cosmétiques uniquement jamais pay-to-win", "pas de pop-up forcée (dark patterns interdits UE 2027)"]
cross_refs: [1585, 1586, 1587]
tags: ["2027"]
depends_on: [1585]
---

## 1582. 📱 Monetisation mobile éthique : pub rewarded et IAP (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Monétiser un F2P mobile en 2027 éthiquement : rewarded ads choisies par le joueur (bouton 'Regarder une vidéo pour +100 gold', max 3/jour, jamais forcées), IAP cosmétiques seuls (jamais pay-to-win), prix transparents, pas de pop-ups agressives (dark patterns interdits).

**Quand l'utiliser (triggers)** :
- Gagner de l'or en regardant une vidéo (rewarded, choisi)
- Skins payants cosmétiques, jamais +10 % dégâts (pay-to-win interdit)
- Pop-up 'Offre urgente !!!' = dark pattern interdit UE 2027

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es game designer monétisation. Tu appliques la règle UE 2027 : rewarded = opt-in explicite (bouton), max 3/jour, récompense claire avant; IAP = cosmétique uniquement (skins 1542, emotes), jamais stats (1535) ni énergie; prix affiché en clair, pas de fausse urgence, remboursement via store. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le modèle F2P (pub rewarded et/ou IAP cosmétique)
- Les récompenses des ads (gold 1529, vies)
- Les IAP cosmétiques (skins, 1542)

**Méthode** :
1. Rewarded : bouton '🎁 +100 gold (vidéo)' placé dans le shop, max 3/jour, récompense après la vidéo complète, jamais de vidéo interstitielle forcée.
2. IAP : uniquement cosmétiques (skins persos, traînées 1557, pas de stats 1535); prix clair (0,99-9,99 €), pas de 'pack urgent -50 % 2 min'.
3. Protection mineurs (1587) : pas de pub ciblée, pas d'achat sans validation parentale (Apple/Google).
4. Revenus : viser ARPU 0,05-0,50 $ selon le marché (analytics 1540), itérer sur l'offre sans dark patterns.
5. Conformité : DSA/UE 2027, CGU claires, remboursement 14 j.

**Sorties attendues** :
- La monétisation éthique déployée (rewarded opt-in + IAP cosmétiques)
- La conformité UE 2027 (pas de dark patterns, mineurs 1587)
- L'ARPU suivi (1540) et ajusté

**Exemple de prompt** :
> « Monétise mon F2P mobile éthiquement : bouton rewarded '+100 gold (vidéo)' max 3/jour opt-in, IAP skins cosmétiques uniquement (jamais de stats), prix clairs, protection mineurs (1587), ARPU suivi (1540). »

**Cas d'usage** : F2P mobile. S'articule avec skills 1585 (IAP), 1586 (gacha légal) et 1587 (RGPD mineurs).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
