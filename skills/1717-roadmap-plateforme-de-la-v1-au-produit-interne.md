---
num: 1717
resume: "Construire la roadmap d'une plateforme interne en 2027 par trimestres : v1 = catalogue + 1 golden path (3 mois), v2 = self-service (1703) + scorecards (1711), v3 = IA-assisté (1708) + multi-cluster (1716) — avec DORA (1706), adoption % et NPS interne à chaque version. Étape 1 : V1 (mois 1-3) : portail Backstage (1702) + catalogue auto + 1 golden path (le plus demandé, 1701). Métriques : adoption %"
lang: "fr"
date_ajout: "2026-11"
nom: "Roadmap plateforme : de la v1 au produit interne"
emoji: "🗺️"
domaine: "Gestion"
signal: "Construire la roadmap d'une plateforme interne en 2027 : traiter l'IDP comme un produit interne (utilisateurs = devs) : v1 = catalogue + 1 golden path (1701) en 3 mois ; v2 = self-service (Crossplane 1703) + scorecards (1711) ; v3 = IA-assisté (1708) + multi-cluster (1716) ; métriques à chaque version (DORA 1706, NPS interne, adoption %). Chaque version = un trimestre, revue avec les 'clients' (devs). N'utilise pas pour une roadmap produit externe."
mot_cle: "roadmap plateforme interne IDP 2027 v1 catalogue v2 self-service v3 IA multi-cluster DORA NPS adoption"
nom_court: "Roadmap IDP"
branche: "D25"
synonymes: ["roadmap IDP par trimestre : v1 catalogue+golden path, v2 self-service, v3 IA", "traiter l'IDP comme un produit interne (clients = devs, NPS)", "métriques à chaque version : DORA 1706 + adoption % + NPS"]
cross_refs: [1700, 1701, 1706]
tags: ["2027"]
depends_on: [1700]
---

## 1717. 🗺️ Roadmap plateforme 2027 : de la v1 au produit interne (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Construire la roadmap d'une plateforme interne en 2027 par trimestres : v1 = catalogue + 1 golden path (3 mois), v2 = self-service (1703) + scorecards (1711), v3 = IA-assisté (1708) + multi-cluster (1716) — avec DORA (1706), adoption % et NPS interne à chaque version.

**Quand l'utiliser (triggers)** :
- par où commencer l'IDP en 2027 ? (v1 = 1 golden path en 3 mois)
- chaque trimestre = 1 version avec métriques DORA et NPS
- revue avec les devs (clients internes) à chaque version

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es platform product manager. Tu définis la roadmap produit interne : v1 (catalogue Backstage 1702 + 1 golden path 1701, 3 mois), v2 (self-service Crossplane 1703 + scorecards 1711 + GitOps 1704), v3 (IA 1708 + Kratix 1716 + DORA avancé 1706), avec revue 'clients' (devs) chaque trimestre. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'audit des demandes (top 3 = v1)
- L'équipe platform
- Les métriques (DORA 1706, NPS, adoption 1698)

**Méthode** :
1. V1 (mois 1-3) : portail Backstage (1702) + catalogue auto + 1 golden path (le plus demandé, 1701). Métriques : adoption %, temps du path.
2. V2 (mois 4-6) : self-service (Crossplane 1703, Kratix 1716), scorecards (1711), GitOps (1704), DORA (1706). Métriques : lead time, tickets -70 %.
3. V3 (mois 7-9) : IA-assisté (1708), multi-cluster, SPACE (1712), TCO revu (1709).
4. Chaque trimestre : revue avec 5-10 devs 'clients' (NPS, ce qui manque), ajustement de la roadmap.
5. Communiquer : changelog interne mensuel (1578), démo trimestrielle (1418 canary).

**Sorties attendues** :
- La roadmap IDP 2027 (v1/v2/v3 par trimestre avec livrables et métriques)
- Les revues trimestrielles avec les devs (NPS, ajustements)
- Le changelog interne mensuel + démos

**Exemple de prompt** :
> « Par où commencer l'IDP ? Roadmap 2027 : v1 (3 mois) = catalogue Backstage + 1 golden path (1701) ; v2 = self-service Crossplane (1703) + scorecards (1711) + DORA (1706) ; v3 = IA (1708) + multi-cluster (1716) — revue avec les devs chaque trimestre (NPS). »

**Cas d'usage** : Lancement d'une plateforme interne. S'articule avec skills 1700 (IDP), 1701 (golden paths), 1706 (DORA), 1712 (SPACE) et 1709 (TCO).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
