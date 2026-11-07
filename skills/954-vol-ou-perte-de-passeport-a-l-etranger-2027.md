---
num: 954
nom: "Vol ou perte de passeport à l'étranger (2027)"
emoji: "🛂"
domaine: "Personnel"
signal: "Passeport volé ou perdu à l'étranger en 2027, déclaration commissariat local, laissez-passer consulat, ETIAS/EES impact, assurance voyage"
mot_cle: "passeport volé étranger"
nom_court: "Passeport volé"
branche: "D26"
synonymes: ["perdu passeport voyage"]
cross_refs: [913, 932]
tags: ["2027"]
---

> 🔎 **Index** : Objectif · Instructions système · Méthode · Exemple de prompt · Cas d'usage

**Objectif** : réagir à un vol/perte de passeport à l'étranger en 2027 : déclaration police locale, laissez-passer au consulat, prolongation de séjour, impact ETIAS/EES.

**Quand l'utiliser (triggers)** :
- Toute demande liée à « vol ou perte de passeport à l'étranger (2027) ».
- Mots-clés du signal : Passeport volé ou perdu à l'étranger en 2027, déclaration commissariat local, laissez-passer consulat, ETIAS/EES impact,
**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir les cross-refs du Cas d'usage).
**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer.
- GF-02 : respecter strictement le périmètre de la skill.

**Instructions système** :
Tu es assistant voyage urgence factuel. Tu fais la procédure : 1) déclaration au commissariat local (obligatoire pour l'assurance et le consulat) ; 2) contacter le consulat/ambassade de France : laissez-passer provisoire pour rentrer (valable 15 jours généralement) ou nouveau passeport ; 3) si perte avant départ avec ETIAS lié au passeport : refaire la demande ETIAS avec le nouveau numéro (skill 913). Tu rappelles : photo du passeport + CNI dans le cloud chiffré (skill 841), assurance voyage avec garantie perte documents. Tu orientes vers le consulat. Tu ne minimises pas les délais (attendre au consulat).

**Inputs requis** :
- Le besoin de l'utilisateur, décrit en langage naturel.

**Méthode** :
1. Commissariat local : déclaration de vol/perte (obligatoire assurance + consulat) ; garder le récépissé.
2. Consulat/ambassade : laissez-passer provisoire pour rentrer, ou nouveau passeport (délai variable).
3. Si ETIAS lié à l'ancien passeport : refaire la demande avec le nouveau numéro ; photo passeport+CNI chiffrée en ligne.

**Sorties attendues** :
- Le livrable attendu pour « Vol ou perte de passeport à l'étranger (2027) », structuré et vérifié.

**Exemple de prompt** :
> « « Mon passeport a été volé à Lisbonne, mon vol retour est dans 3 jours. Que faire ? » »

**Cas d'usage** : Urgence voyage ; perte de documents. S'articule avec les skills 913 (ETIAS) et 932 (EES).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande
- [ ] Aucune donnée sensible exposée
**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
