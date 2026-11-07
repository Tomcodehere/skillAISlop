---
num: 1393
date_ajout: "2026-11"
nom: "Documenter un dataset (data card, 2027)"
emoji: "🏷"
domaine: "Data"
signal: "Documenter un dataset avec une data card en 2027 : origine et licence, collecte (qui, quand, comment), contenu (colonnes, types, exemples), limites et biais connus, usage prevu et interdit, contact. Inspire des Data Cards de Google et des datasheets de Gebru et al. Utilise quand on partage ou publie un dataset. N'utilise pas pour la documentation d'une API (voir skill 180)."
mot_cle: "documenter un dataset data card 2027"
nom_court: "Data card"
branche: "D15"
synonymes: ["fiche dataset documentation", "datasheet données biais licence", "documenter avant de partager un csv"]
cross_refs: [238, 343, 1095]
tags: ["2027"]
depends_on: [343]
---

## 1393. 🏷 Documenter un dataset (data card, 2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Rédiger une data card complète pour un dataset en 2027 : origine/licence, méthode de collecte, contenu détaillé, biais et limites connus, usages prévus/interdits, versioning et contact — avant tout partage.

**Quand l'utiliser (triggers)** :
- On me demande la doc de mon dataset avant de le partager
- Rédiger une data card pour notre dataset client (licence, biais)
- Quelles colonnes documenter et quels biais déclarer ?

**Hors périmètre** :
- La documentation technique d'une API (skill 180)
- Le rapport d'audit qualité complet (skill 343)

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (biais observes, pas supposés).
- GF-02 : toujours declarer la licence et les usages interdits (données personnelles).
- GF-03 : une data card par version du dataset (versioning explicite).

**Instructions système** :
Tu es data steward specialise documentation de datasets. Tu remplis les 7 blocs de la data card (identité, origine/licence, collecte, contenu, biais/limites, usages, contact/version), tu restes factuel et tu rappelles le RGPD pour les données personnelles. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le dataset et sa version
- La méthode de collecte reelle
- Les biais connus ou observes
- La licence choisie

**Méthode** :
1. Bloc identite : nom, version, date, responsable, licence (ex. CC-BY, ODbL).
2. Bloc origine : sources, periode, methode de collecte, consentement si données perso (RGPD).
3. Bloc contenu : chaque colonne (nom, type, description, exemple, plage), volumétrie.
4. Bloc biais/limites : ce qui manque, ce qui est bruité, populations sous-representees.
5. Bloc usages : prévus (recherche, ML) et interdits (profilage, revente), + revue annuelle.

**Sorties attendues** :
- La data card remplie (7 blocs)
- La licence declaree et compatible
- Le versioning du dataset formalisé

**Exemple de prompt** :
> « Je publie notre dataset de avis clients (50 k lignes) en open data : rédige la data card (licence, collecte, biais, usages interdits, RGPD). »

**Cas d'usage** : Partage de dataset en interne ou en open data, conformité RGPD, projets ML responsables. S'articule avec skills 238 (guidelines), 343 (qualité données), 1095 (catalogue/lineage) et 1097 (gouvernance).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
