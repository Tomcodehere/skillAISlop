---
num: 1642
nom: "Harvest now, decrypt later : proteger les donnees long terme (2027)"
emoji: "⏳"
domaine: "Sécurité"
signal: "Se protéger en 2027 contre « harvest now, decrypt later » (des attaquants volent aujourd'hui des données chiffrées pour les déchiffrer plus tard avec un ordinateur quantique) : identifier les données à très long terme (santé, contrats, secrets industriels, clés racines), les chiffrer en PQC/hybride dès maintenant (1641), minimiser la rétention (189). Utilise pour les données sensibles à 10-30 ans. N'utilise pas pour les données à 1 an (le risque est faible)."
mot_cle: "harvest now decrypt later données long terme chiffrer PQC maintenant rétention minimale 2027"
nom_court: "Harvest now"
branche: "D23"
synonymes: ["données volées aujourd'hui, déchiffrées en 2035 par quantique", "quelles données protéger en PQC dès maintenant", "réduire la rétention des données sensibles (RGPD)"]
cross_refs: [1641, 506, 189]
tags: ["2027"]
depends_on: [1641]
---

## 1642. ⏳ Harvest now, decrypt later : proteger les donnees long terme (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Se protéger en 2027 du « harvest now, decrypt later » : identifier les données à très long terme (santé, contrats 30 ans, secrets industriels, clés racines), les chiffrer en PQC/hybride dès maintenant (1641), et minimiser la rétention (RGPD 189).

**Quand l'utiliser (triggers)** :
- mes dossiers médicaux chiffrés aujourd'hui seront lisibles en 2035
- quelles données chiffrer en PQC en priorité
- réduire la durée de rétention des données sensibles

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es DPO + RSSI. Tu classes les données par durée de vie : 10-30 ans (santé, contrats, R&D, clés racines) → PQC/hybride maintenant (1641) ; 1-3 ans → chiffrement actuel suffisant ; minimiser la rétention (purge auto, 189). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'inventaire des données sensibles et leur durée de vie légale
- Les chiffrements actuels (1641)
- La politique de rétention (189)

**Méthode** :
1. Classer : données à vie longue (santé, contrats, brevets, clés racines PKI) = risque quantique réel → PQC/hybride prioritaire.
2. Données courtes (logs 90 j, sessions) → chiffrement actuel OK.
3. Minimiser : durée de conservation au strict nécessaire + purge auto (189), pseudonymisation (1465).
4. Chiffrer les backups et archives aussi (souvent oubliés).
5. Documenter la politique « long terme = PQC » et la faire valider (comité sécurité).

**Sorties attendues** :
- La liste des données long terme à passer en PQC/hybride
- La politique de rétention réduite (purge auto)
- La décision documentée et validée

**Exemple de prompt** :
> « Nos dossiers patients (conservés 30 ans) sont chiffrés en RSA/AES aujourd'hui : liste-les, passe-les en hybrid/PQC (1641), réduis la rétention au légal (purge auto 189) pour le reste. »

**Cas d'usage** : Santé, juridique, R&D, PKI, données classifiées. S'articule avec skills 1641 (PQC), 506 (chiffrement) et 189 (RGPD rétention).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
