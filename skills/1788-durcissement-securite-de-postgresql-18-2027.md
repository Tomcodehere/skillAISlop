---
num: 1788
date_ajout: "2026-11"
nom: "Durcissement sécurité de PostgreSQL 18 (2027)"
emoji: "🔒"
domaine: "Sécurité"
signal: "Durcir PG18 en 2027 : SCRAM-SHA-256 par defaut pour les mots de passe (md5 desactive), TLS 1.3 min pour les connexions (ssl_min_protocol_version), row-level security (RLS) sur les tables multi-tenant, pg_hba restrictif (hostssl uniquement), audit pg_audit, et OAuth 2.0 (1786) pour les applis. N'utilise pas de connexions en clair (hostnossl interdit)."
mot_cle: "durcir PostgreSQL 18 SCRAM-SHA-256 TLS 1.3 RLS row level security pg_audit pg_hba hostssl 2027"
nom_court: "Durcissement PG18"
branche: "D23"
synonymes: ["SCRAM-SHA-256 par defaut PG18, md5 desactive", "ssl_min_protocol_version = TLSv1.3 dans postgresql.conf", "RLS row level security sur table multi-tenant + policy"]
cross_refs: [1786, 1780, 1790]
tags: ["2027"]
depends_on: [1780]
---

## 1788. 🔒 Durcissement sécurité de PostgreSQL 18 (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Durcir une instance PG18 : SCRAM-SHA-256 par défaut, TLS 1.3 minimum, hostssl uniquement, RLS sur les tables multi-tenant, pg_audit, OAuth 2.0 (1786) pour les applis.

**Quand l'utiliser (triggers)** :
- md5 encore accepte pour les mots de passe PG
- activer RLS sur la table tenants
- interdire les connexions non-TLS (hostnossl refuse)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es DBA sécurité. Tu appliques la checklist : password_encryption=scram-sha-256, ssl_min_protocol_version=TLSv1.3, pg_hba en hostssl uniquement, RLS + policies par tenant, pg_audit actif, et tu testes chaque controle. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'instance PG18
- Les roles et mots de passe existants
- Les tables multi-tenant

**Méthode** :
1. password_encryption = scram-sha-256 + rehash des mots de passe existants (md5 interdit).
2. ssl_min_protocol_version = TLSv1.3, certificats valides, pg_hba : hostssl uniquement (supprimer hostnossl).
3. RLS : ALTER TABLE t ENABLE ROW LEVEL SECURITY + CREATE POLICY par tenant_id = current_setting.
4. pg_audit : log des connexions et DDL sensibles. OAuth 2.0 pour les applis (1786).

**Sorties attendues** :
- La checklist de durcissement appliquee et cochee
- Les policies RLS en place et testees
- Le log d'audit actif (connexions, DDL)

**Exemple de prompt** :
> « Table orders multi-tenant : RLS ENABLE + POLICY tenant_policy USING (tenant_id = current_setting('app.tenant_id')::int) — un role applicatif ne voit que son tenant, test : SELECT count(*) avec app.tenant_id=42 ne renvoie que les lignes du tenant 42. »

**Cas d'usage** : Sécuriser la base. S'articule avec skills 1786 (OAuth), 1780, 1790 (PQC TLS hybride).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
