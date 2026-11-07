---
num: 1469
nom: "Centraliser et requeter ses logs applicatifs (ELK, Loki, 2027)"
emoji: "📚"
domaine: "Data"
signal: "Centraliser les logs applicatifs en 2027 et les requêter : stack ELK (Elasticsearch+Logstash+Kibana, puissant mais lourd), Grafana Loki (léger, label-based, peu cher), ou ClickHouse (très rapide, SQL). Critères : volume, recherche full-text vs métriques de logs, coût. Utilise quand les logs sont sur 50 serveurs. N'utilise pas pour la sécurité (voir SIEM 1453)."
mot_cle: "centraliser logs ELK Loki ClickHouse requêter grep distribué"
nom_court: "Logs centralisés"
branche: "D17"
synonymes: ["ELK ou Loki choisir 2027", "rechercher dans tous les logs d'un coup", "logs distribués ClickHouse rapide"]
cross_refs: [1409, 1453, 1282]
tags: ["2027"]
depends_on: [1409]
---

## 1469. 📚 Centraliser et requeter ses logs applicatifs (ELK, Loki, 2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Centraliser les logs de N serveurs en 2027 (Grafana Loki léger recommandé, ou ELK/ClickHouse) : ingestion (Promtail/Fluent Bit), rétention, recherche full-text distribuée, dashboards et alertes sur patterns de logs.

**Quand l'utiliser (triggers)** :
- Chercher une erreur dans les logs de 50 serveurs
- Loki ou ELK en 2027 ?
- Alertes sur pattern de logs (500 errors)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte observabilité logs. Tu compares Loki (labels, pas d'index full-text, très économique, parfait avec Prometheus/Grafana 1416), ELK (recherche full-text puissante, lourd/cher), ClickHouse (SQL, très rapide sur gros volume). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le volume de logs (Go/jour)
- Les besoins (recherche texte libre vs métriques de logs)
- La stack existante (Grafana déjà là ?)

**Méthode** :
1. Choisir : Loki si stack Grafana + coût serré, ELK si full-text riche, ClickHouse si très gros volume + SQL.
2. Déployer l'ingestion (Promtail/Fluent Bit/Vector) sur tous les serveurs.
3. Structurer les logs (JSON, skill 1409) avec labels (app, env, niveau).
4. Rétention : 7-30 jours chaud, archivage S3 froid.
5. Dashboards (taux d'erreurs) + alertes sur patterns (5xx > seuil).

**Sorties attendues** :
- La stack de logs centralisée (Loki/ELK/ClickHouse)
- La recherche distribuée opérationnelle
- Les alertes sur patterns de logs

**Exemple de prompt** :
> « On debug une erreur en SSHant sur 30 serveurs : centralise les logs dans Loki (Promtail partout, recherche Grafana, alerte si erreurs 5xx > 1 %). »

**Cas d'usage** : Debug distribué, forensic, perfs. S'articule avec skills 1409 (logging structuré), 1453 (SIEM sécu) et 1282 (monitoring).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
