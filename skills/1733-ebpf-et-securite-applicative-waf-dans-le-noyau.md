---
num: 1733
date_ajout: "2026-11"
nom: "eBPF et sécurité applicative : WAF dans le noyau"
emoji: "🛡"
domaine: "Sécurité"
signal: "Filtrer au niveau noyau avec eBPF (1720) en 2027 en complément du WAF applicatif (1451) : XDP pour dropper les paquets (DDoS L3-L4, IPs blacklistées) avant même la stack réseau, eBPF sur TC pour des règles L4 fines. Le WAF L7 (SQLi, XSS) reste applicatif (1451/1452 CSP). Utilise pour la protection DDoS volumineuse à bas coût. N'utilise pas pour remplacer le WAF L7."
mot_cle: "eBPF XDP TC noyau filtrage paquets DDoS L3 L4 WAF noyau 2027 blacklist IP drop avant stack réseau"
nom_court: "eBPF WAF"
branche: "D23"
synonymes: ["dropper les paquets d'une IP blacklistée dans le noyau (XDP)", "DDoS volumineux : filtrer en XDP avant la stack réseau (eBPF)", "WAF L7 (SQLi) reste applicatif 1451, eBPF fait le L3-L4"]
cross_refs: [1720, 1451, 1132]
tags: ["2027"]
depends_on: [1720]
---

## 1733. 🛡 eBPF et sécurité applicative : WAF dans le noyau (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Protéger à bas coût en 2027 avec eBPF au niveau noyau (XDP/TC, 1720) : dropper les paquets (IPs blacklistées, DDoS L3-L4) avant la stack réseau ; le WAF L7 (SQLi/XSS 1451/1452) reste applicatif.

**Quand l'utiliser (triggers)** :
- attaque DDoS de 10 Gbps, le serveur tombe avant le WAF
- XDP : drop les paquets de l'IP attaquante dans le noyau (eBPF)
- blacklist dynamique (SIEM 1453 pousse les IPs vers XDP)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es sécurité réseau. Tu programmes XDP (drop/redirect/pass) ou TC (classification) en eBPF (via Cilium 1721 ou un programme custom vérifié), piloté par une blacklist dynamique (SIEM 1453 → eBPF map), et tu mesures le débit protégé. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les serveurs exposés
- La blacklist dynamique (SIEM 1453)
- Le débit à protéger

**Méthode** :
1. XDP (le plus tôt, dans la carte réseau) : programme eBPF qui drop les paquets de la map des IPs bloquées, compte les drops, renvoie le reste (XDP_PASS) à la stack normale.
2. TC (après XDP) : classification L4 (ports, protocoles) si besoin.
3. Blacklist dynamique : le SIEM/SOAR (1453/1651) pousse les IPs attaquantes dans la map eBPF (via bpftool ou l'API de l'agent), retrait automatique après TTL.
4. Ne pas tout faire en noyau : le L7 (SQLi, XSS, requêtes lentes) reste au WAF applicatif (1451) + CSP (1452).
5. Mesurer : débit absorbé (Gbps), faux positifs (IPs legit bloquées = 0), latence ajoutée (~nulle en XDP).

**Sorties attendues** :
- Le filtre XDP eBPF déployé (blacklist dynamique depuis le SIEM 1453)
- Le débit DDoS absorbé mesuré (Gbps) avec 0 faux positif
- L'architecture : XDP (L3-L4) + WAF L7 (1451) + CSP (1452)

**Exemple de prompt** :
> « Attaque DDoS de 10 Gbps qui tue le serveur avant le WAF : déploie un filtre XDP eBPF (1720) qui drop dans le noyau les IPs poussées en temps réel par le SIEM (1453), débit absorbé mesuré, WAF L7 (1451) inchangé pour le L7. »

**Cas d'usage** : Protection DDoS volumineuse. S'articule avec skills 1720 (eBPF), 1451 (WAF), 1132 (firewall), 1453 (SIEM).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
