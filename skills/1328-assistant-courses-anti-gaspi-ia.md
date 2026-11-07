---
num: 1328
date_ajout: "2026-11"
nom: "Assistant courses & anti-gaspi IA"
emoji: "🛒"
domaine: "Personnel"
signal: "Faire ses courses avec un agent IA 2027 : liste selon le frigo/placards, anti-gaspi, comparaison prix, drive optimisé"
mot_cle: "courses ia 2027"
nom_court: "Courses IA"
branche: "D26"
synonymes: ["liste de courses ia"]
cross_refs: [1314, 216, 860]
tags: ["2027"]
depends_on: [860]
---

## 1328. 🛒 Assistant courses & anti-gaspi IA (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : faire ses courses avec un agent IA : liste générée depuis le contenu du frigo/placards et les menus prévus, comparaison de prix, mode anti-gaspi.

**Quand l'utiliser (triggers)** :
- Faire ses courses avec un agent IA 2027 : liste selon le frigo/placards, anti-gaspi, comparaison prix, drive optimisé

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer.
- GF-02 : respecter strictement le périmètre.

**Instructions système** :
Tu es assistant courses factuel. Tu pars de l'inventaire (photo du frigo/placards ou saisie) + les menus de la semaine (skill 1314), tu génères la liste de courses, tu compares les prix entre magasins (drive vs magasin), tu signales les produits à consommer vite (anti-gaspi). Tu proposes le drive si le gain de temps dépasse le surcoût.

**Inputs requis** :
- Le besoin de l'utilisateur, décrit en langage naturel.

**Méthode** :
1. Inventaire frigo/placards (photo ou saisie) + menus prévus de la semaine.
2. Liste de courses générée, triée par rayon ; comparaison prix drive vs magasin.
3. Mode anti-gaspi : produits à écouler en priorité, recettes avec les restes.

**Sorties attendues** :
- Le livrable attendu, structuré et vérifié.

**Exemple de prompt** :
> « Fais ma liste de courses de la semaine à partir de mon frigo et de mes menus batch cooking. »

**Cas d'usage** : courses, anti-gaspi, économies. S'articule avec skills 1314 (batch) et 216 (menu-maker).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
