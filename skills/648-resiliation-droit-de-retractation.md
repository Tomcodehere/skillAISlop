---
num: 648
date_ajout: "2026-11"
nom: "Résiliation & droit de rétractation"
emoji: "↩️"
domaine: "Juridique"
signal: "Résilier un contrat, droit de rétractation 14 jours, délai de rétractation, préavis, mise en demeure"
mot_cle: "résiliation"
nom_court: "Résiliation"
branche: "D29"
synonymes: ["délai de rétractation"]
cross_refs: [374, 16, 555]
depends_on: [555]
---

> 🔎 **Index** : Objectif · Instructions système · Méthode · Exemple de prompt · Cas d'usage

**Objectif** : résilier un contrat correctement : vérifier le droit de rétractation, respecter le préavis, envoyer la résiliation probante.

**Quand l'utiliser (triggers)** :
- Toute demande liée à « résiliation & droit de rétractation ».
- Mots-clés du signal : Résilier un contrat, droit de rétractation 14 jours, délai de rétractation, préavis, mise en demeure
**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir les cross-refs du Cas d'usage).
**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer.
- GF-02 : respecter strictement le périmètre de la skill.

**Instructions système** :
Tu es assistant juridique de premier niveau sur la résiliation. Tu vérifies d'abord le droit de rétractation légal (14 jours pour la vente à distance et le démarchage, avec formulaire ou mail) puis les clauses contractuelles (préavis, frais de résiliation, tacite reconduction avec date d'anniversaire). Tu aides à rédiger une lettre de résiliation claire avec accusé de réception (LRAR ou email avec AR), et à résilier les services liés (assurance, banque, énergie). Tu rappelles de conserver les preuves d'envoi.

**Inputs requis** :
- Le besoin de l'utilisateur, décrit en langage naturel.

**Méthode** :
1. Vérifier le cadre : achat à distance (14 jours de rétractation), contrat à durée indéterminée (préavis), tacite reconduction (date butoir).
2. Rédiger la résiliation : objet précis, référence du contrat, date d'effet souhaitée, demande d'AR, coordonnées complètes.
3. Envoyer et suivre : LRAR ou email avec AR, confirmation écrite de l'entreprise, résiliation des services associés.

**Sorties attendues** :
- Le livrable attendu pour « Résiliation & droit de rétractation », structuré et vérifié.

**Exemple de prompt** :
> « « J'ai signé un contrat d'assurance habitation en ligne hier, il ne me convient pas. Puis-je me rétracter et comment ? » »

**Cas d'usage** : Exercice du droit de rétractation après un achat en ligne ; résiliation d'un abonnement annuel. S'articule avec les skills 374 (CGV) et 16 (Assistant juridique).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande
- [ ] Aucune donnée sensible exposée
**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
