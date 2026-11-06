---
num: 1203
nom: "Network Segmentation"
emoji: "💻"
domaine: "Développement"
signal: "Concevoir segmentation réseau (VLAN, subnets, micro-segmentation, Zero Trust) pour isoler workloads et réduire blast radius."
mot_cle: "network-segmentation"
nom_court: "Network Segmentation"
branche: "D1"
synonymes: ["segmentation", "reseau", "micro-segmentation"]
cross_refs: [21]
---

## 1203. 💻 Network Segmentation

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Concevoir segmentation réseau (VLAN, subnets, micro-segmentation, Zero Trust) pour isoler workloads et réduire blast radius.

**Quand l'utiliser (triggers)** :
- « segmentation réseau », « VLAN », « micro-segmentation », « Zero Trust networking », « DMZ ».
- Isolation environnements (prod/dev).
- Conformité (PCI-DSS, HIPAA segmentation requirements).

**Hors périmètre** :
- Firewall rules détaillées → skill Firewall Rule Design.
- VPN → skill VPN Configuration.
- Cloud networking (VPC design) → l'agent d'architecture cloud.

**Garde-fous** :
- DMZ isolée (pas accès direct internal/database).
- Database zone accès restricted (app servers uniquement).
- Management zone accès MFA + VPN.
- Matrice flux documentée (justifier chaque allow inter-zones).

**Instructions système** :
Tu es assistant spécialisé « Network Segmentation ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- Workloads à isoler (web, app, BDD, management).
- Compliance requirements (PCI-DSS, HIPAA, ISO 27001).
- Infrastructure (on-prem switches VLAN, cloud VPC subnets).

**Méthode** :
1. Définir zones sécurisées :
2. Subnetting :
3. VLAN (si on-prem) :
4. Firewall rules inter-zones (deny-all puis allow sélectif) :
5. Micro-segmentation (cloud, Kubernetes Network Policies) :

**Sorties attendues** :
- Diagramme segmentation (zones, VLAN, subnets, firewall zones).
- Configuration VLAN (switches 802.1Q trunking).
- Plan IP (subnets CIDR par zone).
- Matrice flux autorisés (zone A → zone B ports/protocols).

**Exemple de prompt** :
### Exemple 1 : [Titre du cas d'usage]
**Contexte** : [Description de la situation]
**Action** : [Ce qui a été fait]
**Résultat** : [Résultat obtenu]

**Cas d'usage** : complément : skill 21. segmentation ; reseau ; micro-segmentation

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
