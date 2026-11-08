---
num: 1894
date_ajout: "2026-11"
nom: "Threat intelligence : MISP, STIX/TAXII, intégration SIEM"
emoji: "🕵️"
domaine: "Sécurité"
signal: "Alimenter la détection avec de la threat intelligence : MISP (open source, communautés de partage, événements/IOCs) ou flux commerciaux (Recorded Future, Mandiant) ; standards STIX 2.1 (objets) + TAXII 2.1 (transport) pour échanger ; IOCs (IP, domaines, hash, YARA) intégrés au SIEM (1453) / EDR (1891) / firewall pour blocage auto. SOAR (1651) exécute les playbooks sur IOC. N'utilise pas de TI non vérifiée (faux positifs) — scoring de confiance (TLP)."
mot_cle: "threat intelligence MISP STIX 2.1 TAXII 2.1 IOCs IP domaine hash YARA SIEM 1453 EDR 1891 blocage auto SOAR 1651 TLP confiance"
nom_court: "Threat intel"
branche: "D23"
synonymes: ["déployer MISP pour partager/recevoir des IOCs (communautés de confiance, TLP)", "STIX/TAXII : importer des flux TI commerciaux dans le SIEM 1453 automatiquement", "un IOC (hash malveillant) bloque auto sur tous les endpoints (EDR 1891) via le SIEM"]
cross_refs: [1453, 1891, 1651]
tags: ["2027"]
depends_on: [1453]
---

## 1894. 🕵️ Threat intelligence : MISP, STIX/TAXII, intégration SIEM

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Alimenter la détection avec de la threat intelligence (MISP open source ou flux STIX/TAXII commerciaux) : IOCs intégrés au SIEM (1453)/EDR (1891) pour blocage automatique, scoring de confiance (TLP).

**Quand l'utiliser (triggers)** :
- déployer MISP et rejoindre une communauté de partage (TLP:amber)
- TAXII : importer automatiquement les IOCs d'un fournisseur commercial
- un hash malveillant bloque auto sur les 500 endpoints (EDR 1891) en 5 min

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es analyste CTI / SOC. Tu déploies MISP (ou consommes du TAXII), tu sélectionnes les sources fiables (TLP, score), et tu pousses les IOCs vers SIEM/EDR/firewall avec blocage auto. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- MISP déployé ou flux TAXII (commercial)
- Le SIEM 1453 + EDR 1891 + firewall
- La politique TLP (partage)

**Méthode** :
1. MISP : rejoindre les communautés (secteur, éditeur), configurer TLP, synchronisation.
2. Ou TAXII : client qui pull les collections STIX 2.1 du serveur TAXII du fournisseur.
3. IOCs -> SIEM (1453) en règles de détection + push EDR (1891)/firewall pour blocage.
4. Confiance : TLP + score de source ; revue des faux positifs hebdo (1761).
5. SOAR 1651 : playbook auto (blocage IP, isolation endpoint) sur IOC match.

**Sorties attendues** :
- MISP/TAXII opérationnel (IOCs reçus)
- Les IOCs déployés en détection (SIEM) + blocage (EDR/firewall)
- Le taux de faux positifs surveillé

**Exemple de prompt** :
> « Communauté MISP partage l'IOC d'une campagne de phishing (domaine + hash pièce jointe) TLP:amber -> en 5 min : règle SIEM (1453) + blocage domaine au proxy + hash bloqué sur les 500 endpoints (1891) — campagne stoppée avant 1er clic. »

**Cas d'usage** : CTI opérationnelle. S'articule avec skills 1453, 1891, 1651, 1892.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
