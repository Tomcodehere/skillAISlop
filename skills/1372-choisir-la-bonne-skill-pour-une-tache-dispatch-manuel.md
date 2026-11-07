---
num: 1372
date_ajout: "2026-11"
nom: "Choisir la bonne skill pour une tache (dispatch manuel)"
emoji: "🧭"
domaine: "Routage"
signal: "Choisir manuellement la bonne skill du catalogue pour une tache donnee : lire la carte des domaines, verifier le signal et le hors perimetre, tester la requete avec le routeur, consulter les cross-refs. Utilise quand le routeur automatique ne renvoie rien (exit 2) ou une mauvaise piste. N'utilise pas pour modifier le catalogue (voir skill 250)."
mot_cle: "choisir la bonne skill pour une tâche"
nom_court: "Dispatch manuel"
branche: "D26"
synonymes: ["quelle skill utiliser pour ça", "trouver la bonne skill", "le routeur ne trouve rien"]
cross_refs: [0, 250, 262]
tags: ["2027"]
depends_on: [0]
---

## 1372. 🧭 Choisir la bonne skill pour une tache (dispatch manuel, 2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Trouver manuellement la bonne skill pour une tache quand le routeur automatique ne convient pas : carte des domaines, signaux, hors perimetre, cross-refs, et verification par une requete test.

**Quand l'utiliser (triggers)** :
- Le routeur ne trouve aucune skill pour ma demande (exit 2)
- Quelle skill du catalogue utiliser pour rédiger un communiqué ?
- Vérifier le hors périmètre d'une skill avant de l'utiliser

**Hors périmètre** :
- La modification ou l'ajout de skills (voir skill 250)
- Le routage automatique en ligne de commande (skill 0)

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (se baser sur les signaux lus).
- GF-02 : toujours lire « Hors perimetre » avant de retenir une skill.
- GF-03 : en cas de doute entre 2 skills, tester les deux requetes avec le routeur.

**Instructions système** :
Tu es routeur manuel expert du catalogue de skills. Tu parcours la carte des domaines puis le bloc de routage du domaine dominant, tu compares signal et hors perimetre, tu proposes 1-3 skills avec cross-refs, et tu restes factuel. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La tache a realiser decrite en langage naturel
- Le domaine probable
- Le resultat du routeur automatique si disponible

**Méthode** :
1. Identifier le domaine dominant de la demande (carte des domaines).
2. Lire les signaux du bloc de routage de ce domaine (3-5 candidats).
3. Exclure ceux dont le hors perimetre correspond a la demande.
4. Verifier les cross-refs pour completer (workflow).
5. Tester la requete reformulee avec le routeur pour confirmer le rang.

**Sorties attendues** :
- 1-3 skills recommandees avec justification
- La requete reformulee qui route bien
- Les cross-refs a enchaîner ensuite

**Exemple de prompt** :
> « Je dois préparer un bilan de compétences pour mon entretien annuel : quelle est la bonne skill du catalogue pour cette tâche ? »

**Cas d'usage** : Demande non routée (exit 2), doute entre deux skills, recherche d'une skill complementaire. S'articule avec skills 0 (routeur), 250 (conservateur du catalogue) et 262 (audit des skills).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
