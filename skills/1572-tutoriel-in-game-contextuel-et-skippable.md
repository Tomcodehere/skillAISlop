---
num: 1572
date_ajout: "2026-11"
nom: "Tutoriel in-game contextuel et skippable"
emoji: "📖"
domaine: "Game Dev"
signal: "Concevoir un tutoriel in-game en 2027 : astuces contextuelles (pas un texte mural), déclenchées au bon moment (premier saut → astuce coyote 1510), skippable (bouton 'Passer le tutoriel'), rejouable (dans les settings 1574), progression trackée (analytics funnel 1540), pas bloquant (jamais de modale qui bloque le jeu). Utilise pour l'onboarding. N'utilise pas pour un jeu évident (puzzle simple)."
mot_cle: "tutoriel in-game contextuel skippable rejouable funnel analytics onboarding"
nom_court: "Tutoriel"
branche: "D22"
synonymes: ["astuce qui apparaît au bon moment (premier saut)", "bouton 'Passer le tutoriel' toujours visible", "tutoriel rejouable depuis les settings"]
cross_refs: [1540, 1574, 1510]
tags: ["2027"]
depends_on: [1540]
---

## 1572. 📖 Tutoriel in-game contextuel et skippable (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Concevoir un tutoriel in-game en 2027 : astuces contextuelles déclenchées par les actions (analytics funnel 1540 : étape 1→2→3), skippable à tout moment, rejouable (settings 1574), jamais bloquant (pas de modale), 1 astuce à la fois max.

**Quand l'utiliser (triggers)** :
- Le tutoriel mural de 10 pages au début, personne ne lit
- Astuce 'double saut' qui apparaît au 1er précipice
- Passer le tutoriel → plus jamais affiché (sauf rejoué)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es game designer onboarding. Tu définis les triggers d Events (premier saut, première arme, premier ennemi) → toast d'astuce (3 s, coin bas droit), bouton 'Passer' (désactive tout, flag save 1503), rejouable via settings, et le funnel analytics (1540) pour voir où on perd les joueurs. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les mécaniques à expliquer (saut 1510, dash 1511, inventaire 1534, craft 1536)
- Les triggers d'apparition
- Le funnel analytics (1540)

**Méthode** :
1. Lister les 8-10 mécaniques clés à expliquer, chacune avec SON moment (trigger event).
2. UI : toast contextuel (icône + 1 phrase + touche), 5 s auto-dismiss ou clic; jamais de modale bloquante.
3. 'Passer le tutoriel' : bouton toujours visible dans le toast → flag tutos_vus = all (save 1503).
4. Rejouable : settings → 'Revoir le tutoriel' (1574).
5. Analytics : event tutorial_step(n) à chaque étape (1540) → funnel, identifier l'étape où on perd le plus.

**Sorties attendues** :
- Le tutoriel contextuel (triggers + toasts skippables)
- Le flag 'passer' persisté + rejouable
- Le funnel analytics des étapes (1540)

**Exemple de prompt** :
> « Personne ne lit mon tutoriel de 10 pages : passe en tutoriel contextuel (astuce au 1er saut/dash/ennemi, toast 5 s, bouton 'Passer', rejouable, funnel analytics 1540). »

**Cas d'usage** : Onboarding nouveaux joueurs. S'articule avec skills 1540 (analytics), 1574 (settings) et 1510 (coyote).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
