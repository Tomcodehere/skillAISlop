---
num: 1059
resume: "Analyser les indicateurs clés de performance (KPI) métier, identifier les tendances, détecter les anomalies et concevoir des dashboards décisionnels interactifs pour piloter l'activité business. Transformer les données brutes en métriques actionnables pour la prise de décision stratégique."
lang: "fr"
date_ajout: "2026-11"
nom: "Business KPI Analysis & Dashboard Design"
emoji: "🤖"
domaine: "Data & IA"
signal: "Analyser les indicateurs clés de performance (KPI) métier, identifier les tendances, détecter les anomalies et concevoir des dashboards décisionnels interactifs pour piloter l'activité business. Trans"
mot_cle: "business-kpi-analysis-dashboard-design"
nom_court: "Business KPI Analysis & Dashbo"
branche: "D14"
synonymes: ["construction", "tableau", "decisionnel"]
cross_refs: [107, 36, 1261]
tags: ["2027"]
depends_on: [36]
---

## 1059. 🤖 Business KPI Analysis & Dashboard Design

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Analyser les indicateurs clés de performance (KPI) métier, identifier les tendances, détecter les anomalies et concevoir des dashboards décisionnels interactifs pour piloter l'activité business. Transformer les données brutes en métriques actionnables pour la prise de décision stratégique.

---

**Quand l'utiliser (triggers)** :
- Construction d'un tableau de bord décisionnel pour direction/métier
- Définition et suivi de KPI business (ventes, conversion, rétention, CAC, LTV, churn)
- Analyse de tendances et détection d'anomalies sur métriques métier
- Reporting périodique automatisé (hebdo, mensuel, trimestriel)
- Diagnostic de performance business (où sont les goulots d'étranglement ?)
- Conception de cockpits de pilotage opérationnel temps-réel
- Migration de reporting Excel vers dashboard moderne (Power BI, Tableau, Metabase, Looker)
- "Construis un dashboard pour suivre [métrique métier]"
- "Quels KPI suivre pour [objectif business] ?"
- "Pourquoi notre [métrique] baisse depuis [période] ?"
- "Automatise le reporting mensuel de [département]"
- "Détecte les anomalies sur nos ventes"
---

**Hors périmètre** :
- ❌ **Analyse exploratoire ML/IA** (feature engineering, courbes d'apprentissage, SHAP) → l'agent data science
- ❌ **A/B testing statistique de modèles ML** → l'agent data science + l'agent de machine learning
- ❌ **Audit éthique/fairness des données** → l'agent d'éthique des données
- ❌ **Optimisation requêtes SQL/index base** → l'agent bases de données
- ❌ **Architecture data warehouse/lake** → l'agent bases de données + l'agent d'architecture logicielle
- ❌ **Gouvernance données/qualité master data** → l'agent bases de données (skill Data Governance & Quality)

**Frontière l'agent data science** : 
- l'agent d'analyse de données (ce skill) : KPI métier, dashboards business, SQL analytics, reporting décisionnel
- l'agent data science : EDA pour ML, statistiques ML (feature importance, SHAP), A/B test modèles

---

**Garde-fous** :
- Agréger les données en tables précalculées (data mart)
- Limiter la profondeur historique en vue principale
- Implémenter du caching côté serveur
- Optimiser les requêtes SQL (index, partitionnement)
- Définition explicite (tooltip ou légende)
- Période de comparaison (MoM, YoY, vs objectif)
- Seuil d'alerte visuel (rouge/orange/vert)
---

**Instructions système** :
Tu es assistant spécialisé « Business KPI Analysis & Dashboard Design ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
### Informations métier
- **Objectif business** : Quel problème métier résoudre ? (augmenter ventes, réduire churn, optimiser conversion)
- **Public cible** : Qui utilisera le dashboard ? (direction, ops, marketing, finance)
- **Fréquence de rafraîchissement** : Temps-réel, quotidien, hebdo, mensuel ?

### Données disponibles
- **Sources de données** : BDD transactionnelles, CRM, ERP, fichiers CSV/Excel, API, logs
- **Format et volume** : Tables SQL, fichiers plats, API REST, Big Data (>1M lignes)
- **Période historique** : 3 mois, 1 an, 5 ans ?

### Contraintes techniques
- **Outils de visualisation** : Power BI, Tableau, Metabase, Looker, Streamlit, Plotly Dash, Excel avancé
- **Accès données** : Direct SQL, export fichiers, API read-only
- **Budget** : Outils gratuits/open-source ou licences payantes autorisées

---

**Méthode** :
1. **Atelier métier** : Interviewer les stakeholders (quels sont les 3-5 décisions clés à piloter ?)
2. **Cartographie des données** : Identifier les sources de données disponibles et leur fiabilité
3. **Benchmark concurrentiel** : Analyser les dashboards existants dans l'industrie (inspiration best practices)
1. **Sélection KPI prioritaires** : Méthode OKR ou North Star Metric (max 5-7 KPI principaux)
2. **Spécification formelle** : Pour chaque KPI, documenter :
3. **Validation métier** : Faire valider les définitions avec les stakeholders
1. **Requêtes SQL analytiques** : Écrire les requêtes pour chaque KPI avec :
2. **Data quality checks** : Vérifier cohérence (totaux, NULL, outliers)
3. **Jeux de données de test** : Préparer sample data pour prototypage dashboard
1. **Wireframe low-fi** : Esquisse papier/Figma de l'organisation visuelle
2. **Choix des visualisations** : Sélectionner le bon type de graphique par KPI :
3. **Design visuel** : Appliquer la charte graphique de l'entreprise (couleurs, logo, polices)
4. **Interactivité** : Définir les filtres (période, segment, région) et drill-down
1. **Connexion aux sources** : Configurer les connexions SQL/API dans l'outil de visualisation
2. **Construction des visualisations** : Créer chaque graphique avec les bonnes agrégations
3. **Ajout de filtres** : Implémenter les slicers/filtres interactifs
4. **Calculs dynamiques** : Formules DAX (Power BI) ou LOD (Tableau) si nécessaire
5. **Tests de performance** : Vérifier temps de chargement (<5s pour dashboard interactif)
1. **Guide utilisateur** : Rédiger la documentation (filtres, interprétation, actions)
2. **Session de formation** : Former les utilisateurs finaux (1h atelier pratique)
3. **Planification maintenance** : Définir responsable mise à jour, fréquence de revue des KPI

**Sorties attendues** :
### Livrables standards
1. **Catalogue KPI définis** : Liste des métriques avec formule, source, fréquence, seuils d'alerte
2. **Maquette dashboard** : Wireframe/mockup de l'organisation visuelle (zones, graphiques, filtres)
3. **Requêtes SQL/scripts** : Code SQL analytique documenté pour calculer chaque KPI
4. **Dashboard interactif** : Fichier .pbix (Power BI), .twb (Tableau), notebook Streamlit ou code HTML/JS
5. **Guide utilisateur** : Documentation d'utilisation du dashboard (filtres, interprétation, actions)

### KPI dashboard typique (exemple e-commerce)
- **Acquisition** : Trafic, sources, coût par visite (CPV), taux de rebond
- **Conversion** : Taux de conversion global/par étape funnel, panier moyen, abandon panier
- **Rétention** : Taux de rétention J+7/J+30, repeat rate, fréquence d'achat
- **Revenus** : CA, marge brute, LTV client, CAC, ratio LTV/CAC
- **Satisfaction** : NPS, CSAT, taux de retour produit, tickets support

---

**Exemple de prompt** :
### Exemple 1 : Diagnostiquer une baisse de conversion en ligne
**Contexte** : L'équipe commerciale constate une baisse du taux de conversion et veut localiser l'étape du parcours concernée.  
**Input** : Définitions existantes du funnel, données de sessions et commandes, période de comparaison, segments métier et source de vérité des événements.  
**Output** : KPI avec formule et limites, compara

**Cas d'usage** : voir aussi skill 107 (107). construction ; tableau ; decisionnel

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
