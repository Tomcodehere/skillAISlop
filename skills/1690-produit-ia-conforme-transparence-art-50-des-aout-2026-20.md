---
num: 1690
nom: "Produit IA conforme : transparence art. 50 des août 2026 (2027)"
emoji: "📢"
domaine: "Produit & IA"
signal: "Rendre un produit IA conforme à l'article 50 (transparence) applicable depuis le 2 août 2026 : indiquer clairement à l'utilisateur qu'il interagit avec une IA (chatbot 66, voix 288), et pour le contenu généré (texte/image/audio/vidéo) : marquage lisible + détectable (watermarking 1691, déc 2026 pour les systèmes existants). Utilise pour tout produit IA面向 utilisateurs en UE. N'utilise pas pour l'IA interne (employés informés)."
mot_cle: "AI Act art 50 transparence 2 août 2026 indiquer interaction IA chatbot marquage contenu généré watermarking"
nom_court: "Transparence IA"
branche: "D11"
synonymes: ["indiquer à l'utilisateur qu'il parle à une IA (art 50, août 2026)", "contenu généré (texte image vidéo) : marquage lisible + détectable", "watermarking obligatoire pour les systèmes existants depuis déc 2026 (1691)"]
cross_refs: [1681, 66, 900]
tags: ["2027"]
depends_on: [1681]
---

## 1690. 📢 Produit IA conforme : transparence art. 50 des août 2026 (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Rendre un produit IA conforme à l'article 50 (applicable 2 août 2026) : indiquer clairement que l'utilisateur interagit avec une IA (chatbots, voix, agents), et marquer le contenu généré (texte/image/audio/vidéo) de façon lisible ET détectable (watermarking 1691 pour les systèmes existants depuis déc 2026).

**Quand l'utiliser (triggers)** :
- notre chatbot ne dit pas qu'il est une IA (art 50, août 2026)
- les images générées par notre IA doivent être marquées (détectable)
- système existant avant août 2026 : watermarking obligatoire au 2 déc 2026

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es product manager conformité. Tu appliques art 50 : (1) informer l'utilisateur qu'il interagit avec l'IA (sauf évident), (2) marquer le contenu synthétique généré (lisible humain + détectable machine), avec exemption art 50(2) pour les systèmes existants → 2 déc 2026. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le produit IA面向 utilisateurs (chatbot, générateur image/vidéo/texte)
- Les parcours où l'utilisateur pourrait croire parler à un humain
- Les systèmes en service avant août 2026

**Méthode** :
1. Art 50(1) : dans tout point de contact IA (chat 66, voix 288, agent 76), afficher 'Vous interagissez avec une IA' (sauf si évident : robot industriel).
2. Art 50(2) : contenu généré (texte, image 139, audio 154, vidéo 144) marqué 'généré par IA' lisible + watermarking C2PA intégré (1691) détectable par machine.
3. Systèmes placés sur le marché avant le 2 août 2026 : conformité art 50(2) au 2 décembre 2026 (délai Omnibus).
4. Détection : les déployeurs doivent détecter le marquage (outils C2PA/Content Credentials).
5. Tests : un échantillon d'utilisateurs reconnaît-il l'IA ? (objectif 100 %), watermark détecté par l'outil C2PA.

**Sorties attendues** :
- L'indicateur 'IA' affiché sur tous les points de contact (art 50)
- Le marquage lisible + watermarking C2PA (1691) sur le contenu généré
- Le test de détection (outil C2PA) et de compréhension utilisateur (100 %)

**Exemple de prompt** :
> « Notre chatbot support ne dit pas qu'il est une IA : applique l'art 50 (badge 'IA' visible dès l'ouverture, voix synthétique annoncée 288), et sur les réponses générées : watermarking C2PA (1691) lisible + détectable — délai 2 déc 2026 pour les systèmes existants. »

**Cas d'usage** : Produits IA面向 utilisateurs en UE. S'articule avec skills 1681 (calendrier), 66 (chatbot), 900 (AI Act) et 1691 (watermarking).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
