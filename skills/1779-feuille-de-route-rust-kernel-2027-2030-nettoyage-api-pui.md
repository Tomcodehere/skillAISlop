---
num: 1779
date_ajout: "2026-11"
nom: "Feuille de route Rust kernel 2027-2030 : nettoyage API puis nouveaux drivers"
emoji: "🗺️"
domaine: "Stratégie"
signal: "La feuille de route 2027-2030 du Rust kernel (Torvalds/Ojeda) : 1-2 ans de nettoyage des API C internes avant d'exposer plus de Rust, puis nouveaux drivers (stockage, réseau, GPU) en Rust par defaut quand pertinent. Objectif : eviter la stagnation du noyau (mainteneurs vieillissants) en attirant de nouveaux contributeurs Rust. Utilise pour planifier l'adoption Rust sur 3 ans."
mot_cle: "feuille de route Rust kernel 2027 2030 nettoyage API C 1-2 ans nouveaux drivers defaut anti-stagnation"
nom_court: "Roadmap Rust kernel"
branche: "D16"
synonymes: ["2027-2030 : nettoyer les API C 1-2 ans avant d'exposer plus de Rust", "nouveaux drivers en Rust par defaut quand pertinent d'ici 2030", "eviter la stagnation du noyau : attirer les jeunes contributeurs Rust"]
cross_refs: [1770, 1776, 1778]
tags: ["2027"]
depends_on: [1770]
---

## 1779. 🗺️ Feuille de route Rust kernel 2027-2030 : nettoyage API puis nouveaux drivers

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Planifier l'adoption de Rust dans le noyau sur 2027-2030 : phase 1 = nettoyage des API C internes (1-2 ans), phase 2 = nouveaux drivers (stockage, réseau, GPU) en Rust par défaut, pour lutter contre la stagnation.

**Quand l'utiliser (triggers)** :
- planifier Rust kernel sur 3 ans
- pourquoi nettoyer les API C avant d'exposer Rust ?
- quels sous-systemes passeront en Rust d'ici 2030 ?

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte noyau / DSI tech. Tu planifies en 2 phases : nettoyage/abstraction des API C (2027-2028) pour rendre le noyau plus 'Rust-friendly', puis nouveaux drivers en Rust par defaut (2028-2030), avec des jalons mesurables (SLOC, drivers, contributeurs). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La roadmap officielle rust-for-linux
- Les API C à nettoyer par sous-système
- Les budgets/equipes disponibles

**Méthode** :
1. Phase 1 (2027-2028) : inventorier les API C internes à nettoyer/abstraire (helpers, wrappers) pour exposer des interfaces sûres utilisables depuis Rust.
2. Phase 2 (2028-2030) : nouveaux drivers stockage/réseau/GPU en Rust par défaut quand la sécurité mémoire compte (1778).
3. Jalons : SLOC Rust, nombre de drivers, nouveaux contributeurs recrutés (anti-stagnation).
4. Revue annuelle avec les mainteneurs C et le tree rust-for-linux (1777).

**Sorties attendues** :
- Le plan 2027-2030 avec 2 phases et jalons chiffres
- La liste des API C prioritaires à nettoyer
- Les objectifs de recrutement de contributeurs Rust

**Exemple de prompt** :
> « Plan 2027 : nettoyer les helpers mémoire du sous-système réseau (API C) pour exposer des wrappers sûrs ; 2028-2030 : tout nouveau driver réseau en Rust par défaut ; jalon : +50 % de contributeurs Rust sur le sous-système d'ici 2030. »

**Cas d'usage** : Stratégie 3 ans. S'articule avec skills 1770, 1776, 1778.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
