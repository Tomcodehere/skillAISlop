---
num: 1709
date_ajout: "2026-11"
nom: "Cout de l'IDP : TCO et justification metier (2027)"
emoji: "💰"
domaine: "Gestion"
signal: "Justifier le coût d'une IDP en 2027 (TCO) : self-host Backstage = 3-6 ingénieurs/an (plus maintenance/upgrades) vs IDP managé (Port/Cortex, licence) ; gains mesurés : lead time 2-5 j → moins de 4 h, déploiements 3-5x plus fréquents, tickets -70 %, onboarding nouveau dev de semaines à jours. Présenter au comité financier avec DORA (1706). N'utilise pas pour décider seul (comité)."
mot_cle: "TCO IDP 2027 coût self-host backstage 3-6 ingénieurs vs managé gains DORA tickets -70%"
nom_court: "TCO IDP"
branche: "D25"
synonymes: ["combien coûte une IDP en 2027 (3-6 ing/an self-host vs licence managée)", "gains IDP : lead time 2-5j à 4h, déploiements x3-5, tickets -70%", "présenter l'IDP au comité financier avec les métriques DORA 1706"]
cross_refs: [1700, 1706, 775]
tags: ["2027"]
depends_on: [1700]
---

## 1709. 💰 Cout de l'IDP : TCO et justification metier (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Chiffrer le TCO d'une IDP en 2027 (self-host Backstage : 3-6 ing/an + maintenance vs IDP managé Port/Cortex : licence) et la justifier par les gains mesurés (DORA 1706 : lead time, fréquence, tickets -70 %, onboarding).

**Quand l'utiliser (triggers)** :
- l'IDP coûte 500k€/an d'ingénieurs, ça vaut le coup ?
- self-host Backstage (3-6 ing/an) vs Port managé (licence) comparatif
- gains : lead time 2-5 j → 4 h, tickets -70 %, onboarding jours vs semaines

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es platform manager. Tu fais le tableur TCO (coûts directs : équipe/licence/hébergement ; gains : DORA avant/après, tickets évités, onboarding) et tu présentes au comité avec les 4 métriques DORA (1706) et le NPS interne. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le choix self-host vs managé
- Les métriques DORA avant/après (1706)
- La file de tickets (avant/après)

**Méthode** :
1. Coûts : self-host = 3-6 ETP/an (équipe platform) + hébergement + upgrades Backstage (douloureux) ; managé = licence (Port/Cortex/Humanitec) + intégration.
2. Gains mesurés : lead time (DORA 1706), deploy frequency x3-5, MTTR, tickets support -70 %, onboarding nouveau dev (semaines → jours), turnover réduit.
3. TCO sur 3 ans = coûts - gains annualisés ; point mort souvent < 18 mois.
4. Présenter au comité financier (775) : chiffres DORA + tickets + NPS interne + risques (maintenance).
5. Décider : build (équipe dédiée) vs buy (managé) vs hybride (Port + équipe légère).

**Sorties attendues** :
- Le tableur TCO 3 ans (self-host vs managé vs hybride)
- Les gains DORA mesurés (lead time, fréquence, tickets -70 %)
- La décision présentée au comité (build/buy/hybride)

**Exemple de prompt** :
> « Le comité demande si l'IDP à 500 k€/an vaut le coup : tableur TCO 3 ans (self-host 3-6 ETP vs Port managé) vs gains DORA mesurés (1706 : lead time 2-5 j → 4 h, déploiements x3-5, tickets -70 %, onboarding jours), point mort < 18 mois. »

**Cas d'usage** : Décision investissement plateforme. S'articule avec skills 1700 (IDP), 1706 (DORA), 775 (business plan).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
