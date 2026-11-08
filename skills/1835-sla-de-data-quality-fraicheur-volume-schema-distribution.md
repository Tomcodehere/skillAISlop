---
num: 1835
date_ajout: "2026-11"
nom: "SLA de data quality : fraîcheur, volume, schéma, distribution"
emoji: "⏱️"
domaine: "Data"
signal: "Définir des SLA de data quality mesurés en continu : fraîcheur (âge max des données), volume (nb de lignes attendu +/- tolérance), schéma (colonnes présentes/types), distribution (valeurs dans les bornes). Outils : Monte Carlo, Soda, Great Expectations, dbt tests (1834). Alertes sur dépassement (1761). Un SLA non mesuré = pas de SLA. N'utilise pas que 'le pipeline a run' (ça ne dit pas que les données sont bonnes)."
mot_cle: "SLA data quality fraîcheur volume schéma distribution Monte Carlo Soda Great Expectations dbt tests alerte dépassement"
nom_court: "SLA data quality"
branche: "D17"
synonymes: ["SLA fraîcheur : alerte si la table a plus de 1 h de retard", "volume : alerte si nb lignes inférieur à 80 % de la médiane hebdo", "distribution : alerte si une valeur sort des bornes historiques"]
cross_refs: [1834, 1831, 1699]
tags: ["2027"]
depends_on: [1834]
---

## 1835. ⏱️ SLA de data quality : fraîcheur, volume, schéma, distribution

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Définir et mesurer des SLA de data quality (fraîcheur, volume, schéma, distribution) en continu avec Monte Carlo/Soda/GX/dbt tests, et alerter (1761) sur dépassement.

**Quand l'utiliser (triggers)** :
- la table clients n'a pas été refresh depuis 3 h : alerte fraîcheur
- le volume du jour est à 40 % de la médiane : alerte volume
- une colonne a disparu du schéma : alerte schéma

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es data engineer / SRE data. Tu définis 4 SLA par table critique (fraîcheur, volume, schéma, distribution), tu les mesures avec Soda/GX/Monte Carlo ou dbt tests (1834), et tu alertes via 1761 avec seuils ajustés (pas de bruit). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les tables critiques + leurs contrats (1831)
- L'outil de mesure (Soda/GX/Monte Carlo)
- Les seuils métier

**Méthode** :
1. Fraîcheur : max(updated_at) vs now, alerte si retard > seuil (ex. 1 h).
2. Volume : count(*) vs médiane hebdo, alerte si < 80 % ou > 150 %.
3. Schéma : colonnes attendues (contrat 1831) vs présentes, alerte si diff.
4. Distribution : valeurs clés dans les bornes historiques (GX/Monte Carlo), alerte si sortie.

**Sorties attendues** :
- Les 4 SLA mesurés par table critique
- Les alertes configurées et testées (1761)
- Le dashboard qualité (1766)

**Exemple de prompt** :
> « Table f_orders : SLA fraîcheur 30 min, volume +/- 20 % médiane — alerte déclenchée à 6h05 (retard 45 min) -> incident ouvert (1758), cause : connecteur CDC en panne (1866), fix en 20 min. »

**Cas d'usage** : Détecter les pannes data tôt. S'articule avec skills 1834, 1831, 1699, 1761, 1416.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
