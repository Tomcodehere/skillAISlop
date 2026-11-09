---
num: 1891
resume: "Choisir son EDR/XDR en 2027 (CrowdStrike Falcon, SentinelOne Singularity, Defender for Endpoint P2, Cortex XDR) selon le threat model, le stack existant (M365/Entra) et le budget — Gartner MQ 2026 : 3 Leaders. Étape 1 : Court-circuiter : si 100 % M365 E5 -supérieur à Defender P2 déployé (déjà payé), évaluer ensuite."
lang: "fr"
date_ajout: "2026-11"
nom: "Choisir son EDR/XDR : CrowdStrike, SentinelOne, Defender, Cortex"
emoji: "🛡️"
domaine: "Sécurité"
signal: "Choisir son endpoint protection en 2027 : CrowdStrike Falcon (Threat Graph supérieur à 1 000 Md événements/j, détection 100 % MITRE 2025, hunting) ; SentinelOne Singularity (réponse autonome, rollback ransomware 1 clic, Purple AI, offline) ; Microsoft Defender for Endpoint P2 (~5,20 $/user/mo, inclus E5, XDR corrélé M365/Entra/Sentinel, Defender Agent SPM pour agents IA en preview) ; Palo Alto Cortex XDR (si déjà Palo). Gartner MQ Endpoint 2026 : 3 Leaders. Critère : threat model + stack existant + budget (écart 17x entre plans). Linux serveurs : Falcon/SentinelOne mieux que Defender."
mot_cle: "choisir EDR XDR 2027 CrowdStrike Falcon SentinelOne Singularity Defender P2 Cortex XDR Gartner MQ threat model rollback ransomware Linux serveurs coût"
nom_court: "Choisir EDR/XDR"
branche: "D23"
synonymes: ["CrowdStrike vs SentinelOne vs Defender en 2027 : lequel selon le threat model", "SentinelOne : rollback ransomware en 1 clic (Complete tier)", "Defender P2 ~5,20 $/user/mo inclus E5 : suffisant pour 75 % des orgs (Microsoft stack)"]
cross_refs: [1892, 1893, 1453]
tags: ["2027"]
depends_on: [1892]
---

## 1891. 🛡️ Choisir son EDR/XDR : CrowdStrike, SentinelOne, Defender, Cortex

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Choisir son EDR/XDR en 2027 (CrowdStrike Falcon, SentinelOne Singularity, Defender for Endpoint P2, Cortex XDR) selon le threat model, le stack existant (M365/Entra) et le budget — Gartner MQ 2026 : 3 Leaders.

**Quand l'utiliser (triggers)** :
- on est en M365 E5 : Defender for Endpoint suffit pour 75 % des cas
- ransomware : SentinelOne rollback 1 clic vs Defender (Controlled Folder Access)
- Linux serveurs prod : Falcon/SentinelOne > Defender (détection)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es RSSI / responsable sécurité endpoint. Tu poses le threat model (APT/nation-state -> CrowdStrike ; ransomware -> SentinelOne ; stack Microsoft -> Defender), tu pilotes un PoC (MITRE ATT&CK eval) et tu benchmark le coût total (licence + MDR). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le parc (OS, taille, criticité)
- Le threat model (ransomware vs APT)
- Le stack existant (M365/Palo)

**Méthode** :
1. Court-circuiter : si 100 % M365 E5 -> Defender P2 déployé (déjà payé), évaluer ensuite.
2. PoC : même attaque (MITRE ATT&CK) sur les 3 candidats, mesurer détection + temps de réponse.
3. Critères pondérés : détection (MITRE), réponse auto (rollback), corrélation XDR (1892), Linux, coût/user.
4. Décision ADR + déploiement + playbook de réponse (1897).

**Sorties attendues** :
- L'EDR/XDR choisi (ADR avec PoC)
- Le déploiement sur le parc (100 % des endpoints)
- Le playbook de réponse (1897)

**Exemple de prompt** :
> « PME 500 postes M365 E5 : Defender P2 (déjà inclus) déployé en 1 semaine, XDR corrélé avec Sentinel (1453) — économies vs CrowdStrike (~17x sur ce profil) ; PoC ransomware montre rollback manuel (acceptable avec backups 1880). »

**Cas d'usage** : Protection endpoints. S'articule avec skills 1892, 1893, 1453, 1651.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
