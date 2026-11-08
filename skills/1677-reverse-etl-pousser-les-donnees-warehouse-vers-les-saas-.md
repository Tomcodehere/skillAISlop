---
num: 1677
date_ajout: "2026-11"
nom: "Reverse ETL : pousser les données warehouse vers les SaaS (Hightouch, Census)"
emoji: "🔄"
domaine: "Data"
signal: "Faire du reverse ETL en 2027 (Hightouch, Census, ou natif dbt 350) : les données du warehouse (segments clients, scores propension 353) sont poussées automatiquement vers les outils métier (Salesforce CRM 270, HubSpot, ads 747, email 357, Intercom support 56) — plus de CSV exportés à la main (264). Utilise quand le warehouse est la source de vérité mais les équipes travaillent dans les SaaS. N'utilise pas pour de l'analytics pure (BI 107)."
mot_cle: "reverse ETL 2027 Hightouch Census warehouse vers SaaS CRM ads email sans CSV"
nom_court: "Reverse ETL"
branche: "D17"
synonymes: ["pousser mes segments clients du warehouse vers Salesforce automatiquement", "plus d'export CSV manuel vers les ads (747)", "Hightouch ou Census : sync warehouse → SaaS 2027", "automatiser mon formulaire typeform vers mon crm"]
cross_refs: [270, 747, 350]
tags: ["2027"]
depends_on: [350]
---

## 1677. 🔄 Reverse ETL : pousser les données warehouse vers les SaaS (Hightouch, Census, 2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Faire du reverse ETL en 2027 (Hightouch/Census) : les modèles du warehouse (dbt 350, segments, scores 353) sont synchronisés automatiquement vers les SaaS métier (CRM 270, ads 747, email 357, support 56) — plus d'export CSV manuel (264).

**Quand l'utiliser (triggers)** :
- exporter les segments clients en CSV vers Salesforce chaque semaine
- Hightouch : sync auto warehouse → CRM/ads/email
- le score de propension (353) doit arriver dans l'outil commercial

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es data activation engineer. Tu définis les 'audiences' (modèles dbt 350 : segments, scores) dans le reverse ETL, tu maps les champs vers chaque destination (Salesforce, Meta ads 747, Mailchimp 357), sync incrémentale, et tu surveilles la fraîcheur (1675). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le warehouse (modèles dbt 350 : segments, scores 353)
- Les destinations SaaS (CRM, ads, email, support)
- Les mappings de champs

**Méthode** :
1. Choisir l'outil : Hightouch, Census, ou natif (dbt + Airbyte 1460).
2. Définir les audiences : modèles SQL (segments VIP, churn risk 106, propension 353) dans le warehouse.
3. Mapper : champ warehouse → champ SaaS (ex. segment_vip → Salesforce Campaign member), direction (warehouse → SaaS).
4. Sync : incrémentale (seuls les changements), fréquence (15 min à 1 j), gestion des conflits (warehouse gagne).
5. Monitoring : fraîcheur par audience (1675), erreurs de mapping, volumes — alertes (1417).

**Sorties attendues** :
- Les audiences sync auto warehouse → SaaS (CRM/ads/email/support)
- Les mappings de champs documentés
- Le monitoring de fraîcheur/erreurs (1675/1417)

**Exemple de prompt** :
> « On exporte les segments clients en CSV vers Salesforce/ads chaque semaine : reverse ETL (Hightouch) — modèles dbt (350) (segments, propension 353) sync auto vers Salesforce (270), Meta ads (747), email (357), fraîcheur monitorée (1675). »

**Cas d'usage** : Activation des données (marketing, vente, support). S'articule avec skills 270 (CRM), 747 (ads), 350 (dbt) et 353 (propension).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
