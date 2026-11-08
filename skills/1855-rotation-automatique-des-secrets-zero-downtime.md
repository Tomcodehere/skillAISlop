---
num: 1855
date_ajout: "2026-11"
nom: "Rotation automatique des secrets (zero downtime)"
emoji: "🔄"
domaine: "Sécurité"
signal: "Automatiser la rotation des secrets sans downtime : Vault dynamic secrets (1853, TTL auto) ou rotation cloud (AWS Secrets Manager rotation lambda) — ESO resync (refreshInterval 1854) — Stakater Reloader détecte le changement de Secret/ConfigMap et fait un rolling restart des pods. Les secrets montés en volume se propagent sans restart (kubelet sync ~1 min). N'utilise pas de restart manuel 'quand on y pense'."
mot_cle: "rotation automatique secrets zero downtime Reloader rolling restart ESO refreshInterval volume kubelet sync Vault TTL cloud lambda"
nom_court: "Rotation auto"
branche: "D23"
synonymes: ["changer un secret sans redémarrer manuellement : ESO refreshInterval + Reloader rolling restart", "secret en volume : le kubelet propage en ~1 min sans restart de pod", "Vault dynamic secrets TTL : la rotation est automatique (1853)"]
cross_refs: [1853, 1854, 1851]
tags: ["2027"]
depends_on: [1854]
---

## 1855. 🔄 Rotation automatique des secrets (zero downtime)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Automatiser la rotation des secrets sans downtime : Vault dynamic (TTL) ou rotation cloud -> ESO resync (1854) -> Reloader rolling restart ; ou secret en volume (propagation kubelet ~1 min sans restart).

**Quand l'utiliser (triggers)** :
- on a changé le mot de passe BDD : faut-il redémarrer tous les pods ? (non : volume ou Reloader)
- Reloader : détecter le changement de Secret et rolling restart auto
- rotation cloud AWS Secrets Manager (lambda) + ESO sync

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es SRE plateforme. Tu choisis le mode : volume (propagation auto ~1 min, pas de restart) pour les fichiers, ou ESO+Reloader (rolling restart) pour les env vars ; la source tourne toute seule (Vault TTL 1853 ou lambda cloud). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La source qui tourne (Vault 1853 / cloud)
- ESO (1854) + Reloader
- Le mode volume vs env

**Méthode** :
1. Source : Vault dynamic TTL 24 h (1853) ou AWS SM rotation lambda (30 j).
2. Volume : monter le secret en volume -> kubelet resync ~1 min, l'app re-lit le fichier (si elle le supporte).
3. Env : ESO refreshInterval 1 h + Reloader (annotation reloader.stakater.com/auto) -> rolling restart au changement.
4. Vérifier : 0 downtime (rolling), nouveau secret actif partout en < 1 h.

**Sorties attendues** :
- La rotation automatique en place (0 intervention manuelle)
- Le rolling restart sans downtime (Reloader)
- Le délai de propagation mesuré (< 1 h)

**Exemple de prompt** :
> « Rotation mensuelle clé API externe : AWS SM lambda change la clé -> ESO resync le Secret en 1 h -> Reloader rolling restart les 12 pods (0 downtime, métriques 1416 stables) -> ancien secret révoqué. »

**Cas d'usage** : Rotation continue. S'articule avec skills 1853, 1854, 1851, 609.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
