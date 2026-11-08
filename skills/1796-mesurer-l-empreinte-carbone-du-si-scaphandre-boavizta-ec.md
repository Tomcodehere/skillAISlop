---
num: 1796
date_ajout: "2026-11"
nom: "Mesurer l'empreinte carbone du SI : Scaphandre, Boavizta, EcoIndex, CSRD"
emoji: "🌍"
domaine: "Gestion"
signal: "Mesurer en 2027 l'empreinte carbone du SI : Scaphandre/PowerAPI (consommation électrique des serveurs/processus, en W puis kWh), Boavizta (impact matériel, fabrication = ~78 % de l'empreinte des terminaux), EcoIndex/WebsiteCarbon (empreinte d'une page web), facteurs NégaOctet (ADEME). Contexte : numérique = 4,4 % de l'empreinte carbone française (29,5 Mt CO2eq, ADEME 2024). Reporting CSRD (scope 3, catégorie 11 'utilisation des produits vendus'). N'utilise pas des estimations au doigt mouillé pour le reporting officiel."
mot_cle: "mesurer empreinte carbone SI Scaphandre PowerAPI Boavizta EcoIndex NégaOctet ADEME 4,4 % 29,5 Mt CO2 CSRD scope 3 2027"
nom_court: "Empreinte carbone SI"
branche: "D25"
synonymes: ["Scaphandre mesure la conso electrique W/kWh des serveurs en temps reel", "Boavizta evalue l'impact fabrication du materiel (78 % de l'empreinte terminaux)", "CSRD scope 3 categorie 11 : empreinte du numerique dans le reporting 2027"]
cross_refs: [1795, 1752, 1766]
tags: ["2027"]
depends_on: [1795]
---

## 1796. 🌍 Mesurer l'empreinte carbone du SI (2027) : Scaphandre, Boavizta, EcoIndex, CSRD

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Mesurer l'empreinte carbone du SI en 2027 : Scaphandre/PowerAPI (conso élec serveurs), Boavizta (impact matériel), EcoIndex (pages web), facteurs NégaOctet/ADEME, et la reporter dans le CSRD (scope 3).

**Quand l'utiliser (triggers)** :
- combien de kWh consomment mes serveurs par mois ?
- CSRD 2027 : ou va l'empreinte numerique dans le reporting ?
- EcoIndex de la homepage : score et plan d'amelioration

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es responsable Green IT / reporting RSE. Tu deploies Scaphandre sur les serveurs (kWh), tu inventories le materiel via Boavizta (fabrication), tu mesures les pages avec EcoIndex, tu consolides avec les facteurs NégaOctet/ADEME, et tu mappe au CSRD scope 3. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'infrastructure (serveurs, postes, cloud)
- Les URLs a mesurer (EcoIndex)
- Le référentiel CSRD (scope 3 cat. 11)

**Méthode** :
1. Deployer Scaphandre sur les serveurs physiques/cloud (export Prometheus) : conso W -> kWh/mois.
2. Inventaire materiel -> Boavizta : impact fabrication (dominant pour les terminaux, ~78 %).
3. Mesurer les pages clés : EcoIndex / WebsiteCarbon (g CO2eq/page vue).
4. Consolider : kWh x facteur emission région (Electricity Maps) + Boavizta + EcoIndex x trafic = t CO2eq.
5. Reporter : CSRD scope 3 catégorie 11 (utilisation des produits vendus).

**Sorties attendues** :
- Le dashboard conso kWh/serveur/mois (Scaphandre)
- L'empreinte totale t CO2eq (exploitation + fabrication + web)
- Le volet CSRD scope 3 renseigne

**Exemple de prompt** :
> « SI entreprise 2027 : Scaphandre -> 180 MWh/an serveurs (facteur France 0,05 kgCO2/kWh = 9 t), Boavizta -> 400 postes fabrication = 120 t amorties, site web EcoIndex x 10 M pages = 3 t — total ~132 t CO2eq, reporté CSRD scope 3 cat. 11. »

**Cas d'usage** : Piloter et reporter. S'articule avec skills 1795 (RGESN), 1752 (coût/cardinalité), 1766 (dashboards).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
