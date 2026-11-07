---
num: 1696
date_ajout: "2026-11"
nom: "Rendre un chatbot IA accessible (ARIA live, clavier, lecteur d'écran, 2027)"
emoji: "♿"
domaine: "Produit & IA"
signal: "Rendre un chatbot IA accessible en 2027 (WCAG 2.2 AA + EAA 1599) : région aria-live=polite pour les réponses (annoncées au lecteur d'écran 1619), navigation clavier complète (1571), focus géré à l'envoi, contraste 4,5:1 (1484), option 'réduire le mouvement' (1495), alternative humaine proposée (handoff 251), pas de piège clavier. Utilise pour tout chatbot面向 public. N'utilise pas pour un chatbot interne (employés formés)."
mot_cle: "chatbot IA accessible 2027 aria-live polite clavier lecteur écran contraste alternative humaine EAA"
nom_court: "Chatbot a11y"
branche: "D11"
synonymes: ["les réponses du chatbot annoncées au lecteur d'écran (aria-live polite)", "chatbot navigable au clavier seul (1571) sans piège", "proposer un humain (251) + contraste 4,5:1 (1484) EAA 1599"]
cross_refs: [1619, 1571, 1599]
tags: ["2027"]
depends_on: [1599]
---

## 1696. ♿ Rendre un chatbot IA accessible (ARIA live, clavier, lecteur d'écran, 2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Rendre un chatbot IA accessible en 2027 (WCAG 2.2 AA / EAA 1599) : aria-live=polite sur les réponses (annoncées au lecteur d'écran 1619), clavier complet (1571), focus géré, contraste 4,5:1 (1484), reduced-motion (1495), alternative humaine (251).

**Quand l'utiliser (triggers)** :
- NVDA n'annonce pas les réponses du chatbot (aria-live)
- le chat bloque le clavier (piège de focus)
- proposer 'parler à un humain' (251) + contraste 4,5:1 (1484)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es dev front a11y chatbot. Tu appliques : conteneur de messages en role=log aria-live=polite (les nouvelles réponses annoncées), champ de saisie avec label, Entrée envoie, focus revient au champ, pas de piège, contraste (1484), option humain (251). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le chatbot (UI web 66/288)
- Les lecteurs d'écran (NVDA 1619, VoiceOver, TalkBack)
- Les tests clavier (1571)

**Méthode** :
1. Structure : <div role="log" aria-live="polite" aria-label="Réponses du chatbot"> pour l'historique ; chaque réponse = un message avec auteur (user/IA) et heure.
2. Champ : label explicite, Entrée envoie, Échap ferme, focus géré (après envoi, focus sur la zone log ou retour au champ).
3. Annonces : nouvelle réponse annoncée poliment (pas assertive), indicateur 'l'IA écrit…' avec aria-busy.
4. Clavier : tout faisable au clavier (1571), pas de piège de focus, ordre logique.
5. Contraste 4,5:1 (1484), reduced-motion (1495), bouton 'Parler à un humain' (251) toujours visible.
6. Tests : NVDA/VoiceOver (réponses annoncées), clavier seul complet, contraste validé (1484).

**Sorties attendues** :
- Le chatbot accessible (aria-live, clavier, focus) testé NVDA/VoiceOver
- Le contraste (1484) + reduced-motion (1495) validés
- Le bouton humain (251) présent + test EAA (1599)

**Exemple de prompt** :
> « Notre chatbot n'est pas utilisable au clavier ni annoncé par NVDA : ajoute role=log aria-live=polite sur les réponses, navigation clavier complète (1571) sans piège, contraste 4,5:1 (1484), bouton 'humain' (251) — testé NVDA/VoiceOver (1619) + EAA (1599). »

**Cas d'usage** : Chatbots面向 public (support 56, ventes). S'articule avec skills 1619 (a11y front), 1571 (clavier), 1599 (EAA) et 251 (handoff).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
