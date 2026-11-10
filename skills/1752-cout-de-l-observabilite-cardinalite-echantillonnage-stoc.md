---
num: 1752
resume: "Maîtriser le coût de l'observabilité en 2027 (volume prévu x5-10) : cardinalité des labels (jamais d'ID utilisateur 1440), logs structurés + rétention différenciée (1469), traces échantillonnées (head 10 % + tail sur erreurs), stockage objet (0,50 $/Go 1699), budget par équipe (1092). Étape 1 : Audit cardinalité : promtool / Grafana — séries par métrique ; règle : jamais d'ID (user_id, trace_id, s"
lang: "fr"
date_ajout: "2026-11"
nom: "Cout de l'observabilite : cardinalite, echantillonnage, stockage"
emoji: "💰"
domaine: "Data"
signal: "Maîtriser le coût de l'observabilité en 2027 (ça explose avec le volume x5-10 prévu) : cardinalité des métriques (jamais d'user_id en label Prometheus — 1440), logs structurés + rétention différenciée (7 j chaud, 90 j froid S3 1469), traces échantillonnées (head sampling 10 % + tail sampling sur erreurs), stockage objet pas cher (OpenObserve 0,50 $/Go 1699), gouvernance (budget par équipe 1092). N'utilise pas sans mesurer la facture d'abord."
mot_cle: "coût observabilité 2027 cardinalité labels jamais user_id échantillonnage traces head tail rétention stockage objet 0,50$/Go gouvernance budget"
nom_court: "Coût observabilité"
branche: "D17"
synonymes: ["ma facture Prometheus explose à cause des labels user_id (cardinalité)", "traces : head sampling 10% + tail sampling 100% sur erreurs (2027)", "stockage objet 0,50 $/Go (OpenObserve 1699) vs disque cher"]
cross_refs: [1416, 1092, 1469]
tags: ["2027"]
depends_on: [1416]
---

## 1752. 💰 Cout de l'observabilite : cardinalite, echantillonnage, stockage (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Maîtriser le coût de l'observabilité en 2027 (volume prévu x5-10) : cardinalité des labels (jamais d'ID utilisateur 1440), logs structurés + rétention différenciée (1469), traces échantillonnées (head 10 % + tail sur erreurs), stockage objet (0,50 $/Go 1699), budget par équipe (1092).

**Quand l'utiliser (triggers)** :
- la facture Grafana/Prometheus a triplé en 6 mois
- jamais de user_id en label de métrique (cardinalité infinie)
- échantillonner les traces : 10 % en head + 100 % des erreurs en tail

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es SRE FinOps observabilité. Tu audites la cardinalité (nb de séries par métrique), tu règles l'échantillonnage des traces (head+tail), la rétention par tier (1469), tu choisis le stockage objet (1699), et tu poses des budgets par équipe (1092). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La stack observabilité (1416/1680) et sa facture
- Les métriques à haute cardinalité
- Les besoins de rétention (DORA 1649? non — conformité)

**Méthode** :
1. Audit cardinalité : promtool / Grafana — séries par métrique ; règle : jamais d'ID (user_id, trace_id, session) en label (1440) — remplacer par des buckets (status=2xx/4xx/5xx).
2. Logs : structurés (1409), rétention 7 j chaud (SSD), 90 j froid (S3 Glacier 1469), sampling des logs verbeux (debug) à 1 %.
3. Traces : head sampling 10 % (1/10) + tail sampling 100 % sur erreurs/latence haute (décision à la fin du span, 1680).
4. Métriques : agréger au niveau service (pas pod) quand possible, baisser la résolution au-delà de 30 j (1 min → 1 h).
5. Stockage : object storage (S3) pour logs/traces longues durées (0,50 $/Go 1699 OpenObserve) vs disque cher.
6. Budget par équipe (1092) + alerte à 80 % (1417) + revue mensuelle de la facture.

**Sorties attendues** :
- L'audit de cardinalité (séries/métrique) + labels corrigés (plus d'ID 1440)
- Le sampling traces (head 10 % + tail erreurs) et la rétention par tier en place
- Le budget par équipe (1092) + la facture projetée maîtrisée (x5-10 absorbé)

**Exemple de prompt** :
> « La facture observabilité a triplé : audit cardinalité (labels user_id supprimés 1440), traces head 10 % + tail 100 % erreurs, logs 7 j chaud/90 j S3 (1469), stockage objet 0,50 $/Go (1699), budget par équipe (1092) — volume x10 absorbé, facture stable. »

**Cas d'usage** : Gouvernance coûts observabilité. S'articule avec skills 1416 (Grafana), 1092 (FinOps), 1469 (logs), 1680 (OTel), 1699 (OpenObserve) et 1440 (PII).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
