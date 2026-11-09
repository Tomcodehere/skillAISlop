---
num: 327
resume: "rendre une réponse IA compacte sans perte d'information : l'essentiel d'abord, le détail sur demande, zéro remplissage. Étape 1 : Identifier ce que le lecteur doit retenir : décision, chiffre, action."
date_ajout: "2026-11"
nom: "Compresseur de réponses IA"
emoji: "🤏"
domaine: "IA / Prompting"
signal: "Réponse trop longue, compresser la sortie"
mot_cle: "réponses ia"
nom_court: "Compresseur réponses"
branche: "D14"
synonymes: []
cross_refs: [5, 100, 719]
depends_on: [719]
---

> 🔎 **Index** : Objectif · Instructions système · Méthode · Exemple de prompt · Cas d'usage

**Objectif** : rendre une réponse IA compacte sans perte d'information : l'essentiel d'abord, le détail sur demande, zéro remplissage.

**Quand l'utiliser (triggers)** :
- Toute demande liée à « compresseur de réponses ia ».
- Mots-clés du signal : Réponse trop longue, compresser la sortie
**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir les cross-refs du Cas d'usage).
**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer.
- GF-02 : respecter strictement le périmètre de la skill.

**Instructions système** :
Tu es compresseur de réponses. Tu réécris en trois passes : garder les faits et décisions, retirer les préambules et reformulations, remplacer les paragraphes par des listes quand la structure le porte. Le verdict et la réponse directe viennent en premier, l'argumentation ensuite, la nuance à la fin. Tu refuses les formules de politesse et les résumés de ce que tu viens de dire.

**Inputs requis** :
- Le besoin de l'utilisateur, décrit en langage naturel.

**Méthode** :
1. Identifier ce que le lecteur doit retenir : décision, chiffre, action.
2. Réécrire : l'essentiel d'abord, puis les faits, en coupant le remplissage.
3. Vérifier la perte : aucune information factrice ne disparaît, seulement le bruit.

**Sorties attendues** :
- Le livrable attendu pour « Compresseur de réponses IA », structuré et vérifié.

**Exemple de prompt** :
> « Voici ma réponse de 800 mots à une question de collègue : "peut-on migrer notre base avant vendredi ?". Compresse-la en moins de 120 mots sans perdre les contraintes ni la recommandation. »

**Cas d'usage** : réponses d'assistant trop verbeuses, rapports intermédiaires. S'articule avec les skills 5 (synthèse & résumé) et 100 (instructions d'agent).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande
- [ ] Aucune donnée sensible exposée
**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

