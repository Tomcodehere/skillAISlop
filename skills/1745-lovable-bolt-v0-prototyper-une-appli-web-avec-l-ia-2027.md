---
num: 1745
date_ajout: "2026-11"
nom: "Lovable, Bolt, v0 : prototyper une appli web avec l'IA (2027)"
emoji: "⚡"
domaine: "Produit & IA"
signal: "Prototyper une appli web complète en 2027 en quelques heures avec Lovable (chat → app full-stack déployée, Supabase intégré), Bolt.new (StackBlitz, édition live dans le navigateur), ou v0 (Vercel, composants shadcn, déploiement Vercel). Utilise pour un POC/MVP rapide avec de vrais utilisateurs (1483). Le code généré doit être revu/audité avant prod (1401/1658) et exporté (pas de lock-in). N'utilise pas pour de la prod directe sans revue."
mot_cle: "lovable bolt v0 prototyper appli web IA 2027 chat full-stack déployé POC MVP shadcn supabase stackblitz vercel revue 1401"
nom_court: "Lovable/Bolt/v0"
branche: "D11"
synonymes: ["créer une app complète en 2 h avec Lovable (chat → déployé)", "Bolt.new : éditer l'app générée en live dans le navigateur (StackBlitz)", "v0 (Vercel) : composants shadcn + déploiement Vercel en 1 clic"]
cross_refs: [1494, 1735, 1658]
tags: ["2027"]
depends_on: [1735]
---

## 1745. ⚡ Lovable, Bolt, v0 : prototyper une appli web avec l'IA (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Prototyper une appli web complète en 2027 en quelques heures avec Lovable (chat → full-stack déployé, Supabase), Bolt.new (édition live StackBlitz) ou v0 (Vercel, shadcn) — pour un POC/MVP avec de vrais utilisateurs (1483), puis revue/audit (1401/1658) et export du code avant prod.

**Quand l'utiliser (triggers)** :
- un POC client en 2 jours avec Lovable (vrai backend Supabase)
- Bolt.new : modifier l'app IA générée en live dans le navigateur
- v0 : landing + dashboard en composants shadcn déployés sur Vercel

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es product builder. Tu décris l'app en langage naturel, l'outil génère + déploie, tu itères en chat, tu exportes le code (GitHub) pour la revue (1401) et la prod propre — jamais de prod directe sur le code généré. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'idée d'app (écrans, données, auth)
- L'outil (Lovable/Bolt/v0)
- Un compte (déploiement inclus)

**Méthode** :
1. Décrire l'app : écrans, rôles (auth), données (ex. 'tâches avec assignation'), style (1694).
2. Génération : l'outil crée le front + back (Supabase pour Lovable : BDD/auth/storage intégrés), déployé sur une URL.
3. Itérer en chat : 'ajoute le drag&drop', 'dark mode' (1496) — chaque itération redéployée.
4. Tester avec 5 utilisateurs réels (1483/1598) sur l'URL déployée.
5. Avant prod : exporter le code (GitHub), revue humaine (1401), SAST/SCA (1658), migration vers son propre hébergement (pas de lock-in), politique sécurité (1736).

**Sorties attendues** :
- Le POC déployé (URL) testé avec 5 utilisateurs (1483)
- Le code exporté sur GitHub + revue (1401) + SAST (1658) avant prod
- La décision go/no-go documentée (MVP validé ou pivot)

**Exemple de prompt** :
> « POC d'un outil de tâches en équipe en 2 jours : Lovable (chat 'app de tâches avec auth et notifications' → full-stack Supabase déployé), testé par 5 collègues (1483), puis code exporté GitHub + revue (1401) + SAST (1658) avant prod. »

**Cas d'usage** : POC/MVP rapides. S'articule avec skills 1494 (proto IA), 1735 (outils), 1658 (DevSecOps), 1483 (tests users).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
