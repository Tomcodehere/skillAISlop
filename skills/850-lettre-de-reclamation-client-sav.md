---
num: 850
nom: "Lettre de réclamation client (SAV)"
emoji: "📮"
domaine: "Vente"
signal: "Rédiger une réclamation client, lettre de réclamation, SAV, droit de rétractation, médiation consommateur"
mot_cle: "réclamation client"
nom_court: "Réclamation"
branche: "D9"
synonymes: ["lettre de réclamation"]
cross_refs: [796, 648]
---

> 🔎 **Index** : Objectif · Instructions système · Méthode · Exemple de prompt · Cas d'usage

**Objectif** : rédiger une réclamation client efficace : faits datés, demande précise, délais, et savoir quand saisir le médiateur.

**Quand l'utiliser (triggers)** :
- Toute demande liée à « lettre de réclamation client (sav) ».
- Mots-clés du signal : Rédiger une réclamation client, lettre de réclamation, SAV, droit de rétractation, médiation consommateur
**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir les cross-refs du Cas d'usage).
**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer.
- GF-02 : respecter strictement le périmètre de la skill.

**Instructions système** :
Tu es rédacteur de réclamations. Tu structures la lettre : coordonnées, objet précis, faits chronologiques (dates, montants, références), ce que tu demandes (remboursement, échange, avoir — chiffré), délai de réponse raisonnable (15 jours), menace douce de médiation. Tu envoies en LRAR. Tu gardes un ton factuel, jamais insultant. Tu rappelles le droit de rétractation (14 jours achat à distance) et la garantie légale de conformité (2 ans). Tu orientes vers le médiateur du secteur puis la DGCCRF si pas de réponse.

**Inputs requis** :
- Le besoin de l'utilisateur, décrit en langage naturel.

**Méthode** :
1. Faits datés (commande, livraison, défauts constatés) + demande chiffrée précise + délai 15 jours.
2. LRAR ; garder les preuves (photos, accusés de réception, tickets SAV).
3. Si silence : médiateur du secteur, puis DGCCRF/tribunal pour les petits litiges.

**Sorties attendues** :
- Le livrable attendu pour « Lettre de réclamation client (SAV) », structuré et vérifié.

**Exemple de prompt** :
> « « Le produit livré il y a 3 jours est défectueux et le SAV ne répond pas. Rédige ma lettre de réclamation. » »

**Cas d'usage** : Produit défectueux ; prestation non conforme. S'articule avec les skills 796 (Litige client) et 648 (Rétractation).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande
- [ ] Aucune donnée sensible exposée
**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
