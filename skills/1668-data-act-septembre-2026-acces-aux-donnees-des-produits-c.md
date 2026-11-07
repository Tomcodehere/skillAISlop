---
num: 1668
nom: "Data Act septembre 2026 : acces aux donnees des produits connectes (2027)"
emoji: "⚖️"
domaine: "Data"
signal: "Se préparer au Data Act européen en 2027 : depuis le 12 septembre 2026, les produits connectés placés sur le marché UE doivent permettre aux utilisateurs d'accéder aux données qu'ils génèrent (et les partager avec des tiers choisis) via une API standardisée. Obligations pour les fabricants (API données, format interopérable, sécurité) et les détenteurs de données (ne pas verrouiller). Utilise pour tout produit connecté vendu en UE. N'utilise pas pour les données hors produits connectés."
mot_cle: "Data Act 12 septembre 2026 produits connectés accès données utilisateur API standardisée UE 2027"
nom_court: "Data Act 2026"
branche: "D15"
synonymes: ["nos objets connectés vendus en UE doivent exposer leurs données (12 sept 2026)", "API standardisée d'accès aux données générées par le produit", "partage des données avec des tiers choisis par l'utilisateur (Data Act)"]
cross_refs: [1670, 1671, 189]
tags: ["2027"]
depends_on: [1671]
---

## 1668. ⚖️ Data Act septembre 2026 : acces aux donnees des produits connectes (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Se mettre en conformité avec le Data Act UE (12 sept 2026) pour un produit connecté vendu en UE : exposer les données générées via une API standardisée et sécurisée, permettre le partage avec des tiers choisis, documenter — sans verrouiller les données.

**Quand l'utiliser (triggers)** :
- notre objet connecté vendu en UE doit exposer ses données depuis sept 2026
- API Data Act : format interopérable, sécurité, authentification
- l'utilisateur peut partager ses données avec un tiers (ex. réparateur)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es responsable conformité produit. Tu listes les obligations fabricant : API d'accès aux données (format ouvert, documentée 1406), consentement de l'utilisateur (RGPD 189), partage tiers sécurisé, pas de verrouillage propriétaire, registre des accès. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le produit connecté (capteurs, données générées)
- L'API d'exposition des données
- Les cas de partage tiers (réparateur, assureur)

**Méthode** :
1. Inventorier les données générées par le produit (capteurs, usage, logs) et leur sensibilité (1440).
2. API Data Act : endpoint standardisé (format ouvert JSON/Parquet), auth OAuth2 (1450), rate limit, doc (1406).
3. Consentement : l'utilisateur active l'accès/partage explicitement (RGPD 189), peut révoquer.
4. Partage tiers : l'utilisateur désigne un tiers (ex. réparateur) qui reçoit un accès temporaire et scopé.
5. Anti-lock-in : pas de format propriétaire forcé, interopérable (Data Act janv 2027 1671 pour le cloud).
6. Registre des accès + audit (qui a lu quelles données, quand) → conformité.

**Sorties attendues** :
- L'API Data Act du produit (format ouvert, OAuth2, doc) déployée
- Le consentement + partage tiers fonctionnel et scopé
- Le registre des accès et la conformité documentée

**Exemple de prompt** :
> « Notre thermostat connecté vendu en UE doit exposer ses données depuis le 12/09/2026 : API Data Act (JSON ouvert, OAuth2 1450, doc 1406), consentement user (189), partage vers le réparateur désigné (accès temporaire scopé), registre des accès. »

**Cas d'usage** : Fabricants de produits connectés (IoT 1644, domotique, médical, auto). S'articule avec skills 1670 (no switching fees cloud), 1671 et 189 (RGPD).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
