---
num: 1464
nom: "Kafka : topics, partitions et consumer groups (2027)"
emoji: "🂬"
domaine: "Data"
signal: "Concevoir Kafka en 2027 : topics (nommage, rétention), partitions (parallélisme, clé de partitionnement pour l'ordre), consumer groups (rééquilibrage), idempotence, exactly-once, surveillance du lag. Utilise quand on streame des événements à grande échelle. N'utilise pas pour des messages simples (voir files d'attente 319)."
mot_cle: "kafka topics partitions consumer groups lag idempotent"
nom_court: "Kafka"
branche: "D15"
synonymes: ["consumer group kafka lag", "combien de partitions topic", "exactly-once kafka 2027"]
cross_refs: [319, 1280, 1234]
tags: ["2027"]
depends_on: [319]
---

## 1464. 🂬 Kafka : topics, partitions et consumer groups (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Concevoir un Kafka fiable en 2027 : topics nommés avec rétention adaptée, partitions = parallélisme (clé de partition pour l'ordre par entité), consumer groups avec gestion du lag, producteurs idempotents.

**Quand l'utiliser (triggers)** :
- Notre topic Kafka a un lag qui grimpe
- Combien de partitions pour 10k msg/s ?
- Ordre des messages par client garanti ?

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte streaming. Tu expliques : partition = unité de parallélisme, clé de message = hash → partition (ordre garanti par clé), consumer group = plusieurs consumers qui se partagent les partitions, et le lag à surveiller (alerte > seuil). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le flux d'événements (volume, ordre requis ?)
- Les consommateurs (temps de traitement)
- Les garanties (at-least-once vs exactly-once)

**Méthode** :
1. Nommer les topics par domaine (orders.created, payments.done) + rétention (7 j) + partitions (nb consumers max).
2. Choisir la clé de partition (ex. user_id) pour garantir l'ordre par entité.
3. Producteur idempotent (enable.idempotence=true) pour éviter les doublons.
4. Consumer group par service, commit manuel après traitement (at-least-once propre).
5. Surveiller le lag (Burrow, Kafka UI) avec alerte si > 10k messages.

**Sorties attendues** :
- L'architecture Kafka (topics, partitions, rétention)
- Les producteurs idempotents et consumers avec commit manuel
- Le monitoring du lag avec alertes

**Exemple de prompt** :
> « Nos consumers Kafka prennent du retard (lag 500k) et on perd l'ordre par client : revois partitions, clés de partition (user_id) et surveillance du lag. »

**Cas d'usage** : Event streaming, microservices asynchrones, temps réel. S'articule avec skills 319 (files d'attente), 1280 (streaming) et 1234 (contrats).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
