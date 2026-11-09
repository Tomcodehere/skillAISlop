---
num: 1763
resume: "Prévenir l'explosion de cardinalité des métriques : interdire les labels à haute cardinalité (user_id, email, IP, URL brute), borner les buckets, et monitorer le nombre de séries actives par métrique. Étape 1 : Lister les metriques avec leurs labels et compter les series (prometheus tsdb)."
lang: "fr"
date_ajout: "2026-11"
nom: "Cardinalité des métriques : pièges et limites"
emoji: "⚠️"
domaine: "Data"
signal: "Comprendre et contenir la cardinalité des métriques en 2027 : un label par utilisateur ou par requête (user_id, URL complète) fait exploser le nombre de séries temporelles et le coût (Prometheus/TimescaleDB). Regles : jamais de label haute cardinalité (user_id, email, IP), utiliser des buckets bornés. Complète la skill coût de l'observabilité (1752)."
mot_cle: "cardinalite metriques labels haute cardinalite user_id explosion series cout Prometheus 2027"
nom_court: "Cardinalité métriques"
branche: "D17"
synonymes: ["pourquoi mon Prometheus coute 10x plus cher ce mois-ci", "label user_id sur une metrique = explosion du nombre de series", "limiter la cardinalite : buckets bornes, jamais d'identifiant brut en label"]
cross_refs: [1752, 1753, 345]
tags: ["2027"]
depends_on: [1752]
---

## 1763. ⚠️ Cardinalité des métriques : pièges et limites (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Prévenir l'explosion de cardinalité des métriques : interdire les labels à haute cardinalité (user_id, email, IP, URL brute), borner les buckets, et monitorer le nombre de séries actives par métrique.

**Quand l'utiliser (triggers)** :
- la facture observabilité a triple ce mois-ci
- ajouter un label customer_id sur une metrique existante
- combien de series actives a ma metrique requetes_total ?

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es ingénieur observabilité / FinOps. Tu audites les labels existants, tu supprimes ou bucketifies les labels haute cardinalité, tu alertes si une metrique depasse N series (ex. 10 000), et tu documentes les regles de nommage des labels. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les metriques existantes et leurs labels
- La facture / le volume de series du stockage
- Les regles de nommage internes

**Méthode** :
1. Lister les metriques avec leurs labels et compter les series (prometheus tsdb).
2. Identifier les labels haute cardinalité (ids, emails, IPs, paths bruts) et les remplacer par des buckets (ex. status 2xx/4xx/5xx, route normalisée).
3. Mettre une alerte interne si une metrique depasse 10 000 series.
4. Documenter la regle : labels = dimensions bornees uniquement, jamais d'identifiant utilisateur.

**Sorties attendues** :
- L'audit des labels et la liste des corrections
- Le nombre de series reduit et le cout stabilise
- La charte de nommage des labels validee

**Exemple de prompt** :
> « La metrique http_requests a un label url brut avec 2 M de paths uniques : remplacer par route normalisée (/api/users/:id) avec 40 valeurs possibles, les series passent de 2 M a quelques dizaines et le coût s'effondre. »

**Cas d'usage** : Éviter l'explosion des coûts métriques. S'articule avec skills 1752 (coût obs), 1753 (golden signals).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
