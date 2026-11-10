---
num: 1669
resume: "Exploiter le Data Act au 12 janvier 2027 : plus de frais de switching (egress gratuit), préavis max 2 mois, portabilité réelle obligatoire — pour renégocier son cloud, faire du multi-cloud, ou quitter un fournisseur sans pénalité. Étape 1 : Vérifier le contrat : frais de switching (egress) → interdits à partir du 12/01/2027, préavis supérieur à 2 mois → non conforme."
lang: "fr"
date_ajout: "2026-11"
nom: "Data Act janvier : fin des frais de switching cloud"
emoji: "⚖️"
domaine: "Data"
signal: "Préparer le 12 janvier 2027 (Data Act) : les fournisseurs cloud ne peuvent plus facturer le changement de fournisseur (egress inclus), préavis de résiliation max 2 mois, contrats doivent permettre la portabilité réelle. Conséquences : multi-cloud facilité, négociations renforcées, exit strategies obligatoires (DORA 1672). Utilise pour renégocier ou quitter un cloud. N'utilise pas pour les données non-cloud."
mot_cle: "Data Act 12 janvier 2027 fin des frais de switching cloud egress gratuit préavis 2 mois portabilité"
nom_court: "Data Act"
branche: "D15"
synonymes: ["plus de frais de sortie cloud depuis janvier 2027 (Data Act)", "egress gratuit : changer de cloud ne coûte plus rien", "préavis de résiliation cloud max 2 mois (Data Act)"]
cross_refs: [1668, 1672, 1671]
tags: ["2027"]
depends_on: [1672]
---

## 1669. ⚖️ Data Act janvier 2027 : fin des frais de switching cloud (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Exploiter le Data Act au 12 janvier 2027 : plus de frais de switching (egress gratuit), préavis max 2 mois, portabilité réelle obligatoire — pour renégocier son cloud, faire du multi-cloud, ou quitter un fournisseur sans pénalité.

**Quand l'utiliser (triggers)** :
- notre cloud facture 50k€ de frais de sortie (egress), c'est fini en 2027
- changer de fournisseur cloud gratuitement depuis janv 2027
- négocier avec le cloud actuel en brandissant le Data Act

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es responsable achats cloud. Tu rappelles les échéances : sept 2025 Data Act applicable (portabilité), 12 sept 2026 produits connectés (1668), 12 janv 2027 fin des frais de switching + préavis 2 mois. Tu prépares l'exit (1672) AVANT de menacer. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le contrat cloud actuel (frais de sortie, préavis)
- La cible de migration (cloud UE 1688, multi-cloud)
- Le volume de données à sortir (egress)

**Méthode** :
1. Vérifier le contrat : frais de switching (egress) → interdits à partir du 12/01/2027, préavis > 2 mois → non conforme.
2. Préparer la sortie quand même : export des données en format ouvert (Parquet/Iceberg 1663), test de restauration chez le nouveau (1672).
3. Négocier : présenter le Data Act + un devis concurrent (multi-cloud) → réduction ou crédits.
4. Multi-cloud : répartir les nouvelles charges sur 2 fournisseurs (le Data Act rend ça abordable).
5. Garder la preuve des négociations (date, montants) pour l'audit (DORA 1649).

**Sorties attendues** :
- L'exit cloud préparé (export ouvert 1663, test chez le nouveau 1672)
- La renégociation réussie (frais de sortie supprimés, crédits) ou la migration lancée
- Le multi-cloud partiel en place

**Exemple de prompt** :
> « Notre cloud facture 50 k€ d'egress à la sortie : à partir du 12/01/2027 c'est interdit (Data Act) — prépare l'exit (export Parquet/Iceberg 1663, test chez OVH 1688), négocie avec la preuve + devis concurrent, ou migre gratuitement. »

**Cas d'usage** : Gestion des contrats cloud. S'articule avec skills 1668 (Data Act produits), 1672 (exit DORA), 1688 (souverain) et 1649 (DORA).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
