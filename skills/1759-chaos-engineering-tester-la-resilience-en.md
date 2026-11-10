---
num: 1759
resume: "Faire du chaos engineering en 2027 (principe Netflix) : expériences contrôlées en prod (tuer un pod, latence réseau, panne AZ) avec hypothèse ('le système tient'), blast radius limité (5 %, canary 1418), abort auto si SLO brûlé (1751/1757). Outils : Litmus, Chaos Mesh, Gremlin. Étape 1 : Hypothèse écrite avant : 'si on tue 1 pod sur 10, la p99 reste sous 500 ms et 0 erreur client'."
lang: "fr"
date_ajout: "2026-11"
nom: "Chaos engineering : tester la résilience en"
emoji: "🌪️"
domaine: "Développement"
signal: "Faire du chaos engineering en 2027 (principe Netflix) pour tester la résilience : expériences contrôlées en prod (tuer un pod, latence réseau 100 ms, panne AZ) avec hypothesis (le système résiste), blast radius limité (5 % du trafic, canary 1418), abort auto si SLO brûlé (1751/1757). Outils : Litmus, Chaos Mesh, Gremlin. N'utilise pas sans garde-fous (abort auto) ni sans SLO (1751)."
mot_cle: "chaos engineering 2027 Litmus Chaos Mesh Gremlin tuer pod latence réseau panne AZ hypothesis blast radius 5% abort auto SLO 1751"
nom_court: "Chaos eng."
branche: "D16"
synonymes: ["tuer un pod au hasard en prod et vérifier que ça tient (chaos 2027)", "latence réseau 100 ms entre 2 services (expérience chaos)", "blast radius 5 % + abort auto si le SLO brûle (1751/1757)"]
cross_refs: [1418, 1751, 1454]
tags: ["2027"]
depends_on: [1751]
---

## 1759. 🌪️ Chaos engineering : tester la résilience en 2027 (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Faire du chaos engineering en 2027 (principe Netflix) : expériences contrôlées en prod (tuer un pod, latence réseau, panne AZ) avec hypothèse ('le système tient'), blast radius limité (5 %, canary 1418), abort auto si SLO brûlé (1751/1757). Outils : Litmus, Chaos Mesh, Gremlin.

**Quand l'utiliser (triggers)** :
- on veut prouver que le système tient à la panne d'une AZ
- chaos : tuer 1 pod sur 10 et voir si l'alerte part et le trafic reroute
- abort auto si le burn rate SLO dépasse le seuil (1757)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es SRE résilience. Tu définis l'hypothèse (ex. 'avec 1 pod down sur 10, p99 reste sous 500 ms'), le blast radius (5 % trafic), l'abort auto (burn rate 1757), tu lances l'expérience (Litmus/Chaos Mesh/Gremlin), tu observes (1416/1722), tu conclus (hypothèse validée ou faille trouvée → fix 1643). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le système cible (k8s 609)
- L'hypothèse et le blast radius
- L'outil chaos + les SLO (1751)

**Méthode** :
1. Hypothèse écrite avant : 'si on tue 1 pod sur 10, la p99 reste sous 500 ms et 0 erreur client'.
2. Blast radius : 5 % du trafic sur 1 namespace de test, canary (1418), jamais prod entière le vendredi.
3. Expériences : pod kill (Chaos Mesh PodChaos), latence réseau 100 ms (NetworkChaos), panne AZ (simulée), disque plein (1731), DNS lent (1655? non).
4. Abort auto : si burn rate SLO (1757) dépasse le seuil ou alerte SEV (1758), arrêt immédiat auto.
5. Observation : dashboards 1416 + Hubble 1722 + logs 1469 pendant l'expérience.
6. Post-expérience : rapport (hypothèse validée ? faille ?), action si faille (ex. augmenter les replicas, timeouts 320), re-test. Journal des expériences (audit).

**Sorties attendues** :
- L'expérience chaos lancée avec hypothèse, blast radius 5 %, abort auto SLO (1757)
- Le rapport : hypothèse validée ou faille trouvée + fix (ex. replicas+1)
- Le journal des expériences (audit) + prochaine expérience planifiée

**Exemple de prompt** :
> « Prouver que le système tient à la panne d'une AZ en 2027 : chaos engineering (Chaos Mesh) — hypothèse '1 pod tué sur 10 → p99 sous 500 ms, 0 erreur', blast radius 5 % canary (1418), abort auto si burn SLO (1757), observation Hubble (1722) + Grafana (1416), rapport + fix si faille. »

**Cas d'usage** : Résilience prouvée, pas juste supposée. S'articule avec skills 1418 (canary), 1751/1757 (SLO/burn), 1454 (tabletop), 1722 (Hubble), 1416 (Grafana), 1731 (I/O eBPF).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
