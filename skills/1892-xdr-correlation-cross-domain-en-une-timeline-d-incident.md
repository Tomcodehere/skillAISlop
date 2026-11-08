---
num: 1892
date_ajout: "2026-11"
nom: "XDR : corrélation cross-domain en une timeline d'incident"
emoji: "🔗"
domaine: "Sécurité"
signal: "Mettre en place l'XDR (extended detection and response) : corréler endpoint (EDR 1891) + identity (Entra ID Protection) + email (M365) + cloud (Defender for Cloud) + réseau dans UNE timeline d'incident (ex. BEC : phishing mail — vol credential IdP — mouvement latéral endpoint = 1 incident corrélé, pas 3 alertes). Microsoft Defender XDR / CrowdStrike / SentinelOne / Cortex selon le stack (1891). Données : rétention 1-3 ans pour la conformité (1839). N'utilise pas 4 consoles séparées sans corrélation."
mot_cle: "XDR corrélation cross-domain timeline incident unique email identity endpoint cloud Defender XDR Sentinel CrowdStrike Cortex rétention 1-3 ans conformité"
nom_court: "XDR corrélation"
branche: "D23"
synonymes: ["une attaque BEC corrélée en 1 incident (mail + IdP + endpoint) au lieu de 3 alertes séparées", "Defender XDR si stack Microsoft 1891 : corrélation native M365/Entra/Cloud", "rétention 1-3 ans des données XDR pour la conformité (1839)"]
cross_refs: [1891, 1453, 1651]
tags: ["2027"]
depends_on: [1891]
---

## 1892. 🔗 XDR : corrélation cross-domain en une timeline d'incident

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Mettre en place l'XDR : corréler endpoint, identity, email, cloud et réseau dans une timeline d'incident unique (Defender XDR / Falcon / Singularity / Cortex selon le stack 1891).

**Quand l'utiliser (triggers)** :
- 3 alertes séparées pour 1 attaque BEC : il faut la corrélation XDR
- Defender XDR : activer la corrélation cross-domain (M365/Entra/Cloud)
- rétention XDR 2 ans pour l'audit (1839)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es SOC / analyste sécurité. Tu actives la corrélation XDR de la plateforme choisie (1891), tu définis les règles de corrélation (identity+endpoint = incident auto), et la rétention conforme (1839). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La plateforme XDR (1891)
- Les sources connectées (EDR, IdP, mail, cloud, réseau)
- La politique de rétention (1839)

**Méthode** :
1. Connecter les sources : EDR (1891), Entra ID Protection, Exchange/M365, Defender for Cloud, firewall réseau.
2. Règles de corrélation : ex. 'credential volé (IdP) + connexion anomale (endpoint) + exfil (réseau)' = incident auto de priorité haute.
3. Timeline unique par incident : graphiques d'attaque, IOCs extraits -> blocage auto (SOAR 1651).
4. Rétention : 1-3 ans selon conformité (1839), stockage froid au-delà.

**Sorties attendues** :
- Les incidents corrélés (1 timeline par attaque)
- Les règles de corrélation actives + blocages auto (1651)
- La rétention conforme (1839)

**Exemple de prompt** :
> « Attaque BEC : mail phishing (M365) -> credential volé (Entra) -> connexion depuis un nouveau pays (EDR) -> exfil 2 Go (réseau) = 1 incident XDR corrélé, bloqué auto au stade IdP (MFA phishing-resistant 1896 aurait stoppé plus tôt). »

**Cas d'usage** : SOC efficace. S'articule avec skills 1891, 1453, 1651, 1839.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
