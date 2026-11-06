---
num: 1304
nom: "VPN Configuration"
emoji: "📋"
domaine: "Gestion"
signal: "Configurer VPN site-to-site et client-to-site (IPsec, WireGuard, OpenVPN) sécurisés et performants."
mot_cle: "vpn-configuration"
nom_court: "VPN Configuration"
branche: "D25"
synonymes: ["ipsec", "wireguard", "openvpn"]
cross_refs: [426]
---

## 1304. 📋 VPN Configuration

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Configurer VPN site-to-site et client-to-site (IPsec, WireGuard, OpenVPN) sécurisés et performants.

**Quand l'utiliser (triggers)** :
- « VPN », « IPsec », « WireGuard », « OpenVPN », « tunnel chiffré », « remote access ».
- Connexion sécurisée sites distants ou remote workers.
- Remplacement VPN legacy (PPTP interdit).

**Hors périmètre** :
- Firewall rules → skill Firewall Rule Design.
- Architecture réseau complète → networkFirewall (autre skill).
- Cloud VPN (AWS Site-to-Site VPN, Azure VPN Gateway) → l'agent d'architecture cloud (IaC provisioning).

**Garde-fous** :
- Encryption forte (AES-256/ChaCha20, pas 3DES legacy).
- MTU adjusted (WireGuard 1420, IPsec 1400 si fragmentation).
- Firewall allow VPN (UDP 51820 WireGuard, UDP 500/4500 IPsec).
- DNS over VPN (force DNS WireGuard AllowedIPs, éviter DNS leaks).
- Keepalive (PersistentKeepalive 25 WireGuard, DPD IPsec).

**Instructions système** :
Tu es assistant spécialisé « VPN Configuration ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- Type VPN (site-to-site, client-to-site).
- Protocole (IPsec IKEv2, WireGuard, OpenVPN).
- Endpoints (public IPs, subnets privés).
- Encryption (AES-256, ChaCha20).

**Méthode** :
1. **WireGuard (preferred, performance)** :
2. **IPsec IKEv2** (interopérabilité) : strongSwan config /etc/ipsec.conf.
3. **OpenVPN** (legacy, compatibilité) : server.conf, client.ovpn, CA certs.
4. Tests : ping 10.0.0.1 (serveur), tcpdump (vérifier traffic encrypted).

**Sorties attendues** :
- Configuration VPN (ipsec.conf, wg0.conf, openvpn.conf).
- Certificats/clés (WireGuard keys, OpenVPN CA/certs).
- Tests tunnel (ping cross-subnet, traffic encrypted).
- Runbook troubleshooting VPN (tunnel down, MTU issues).

**Exemple de prompt** :
### Exemple 1 : [Titre du cas d'usage]
**Contexte** : [Description de la situation]
**Action** : [Ce qui a été fait]
**Résultat** : [Résultat obtenu]

**Cas d'usage** : complément : skill 426. ipsec ; wireguard ; openvpn

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
