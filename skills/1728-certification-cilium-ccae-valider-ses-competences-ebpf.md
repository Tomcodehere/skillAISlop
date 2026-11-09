---
num: 1728
resume: "Préparer la certification Cilium CCAE en 2027 (associate engineer eBPF/Cilium) : CNI eBPF, NetworkPolicy L3-L7, Hubble, service mesh, commandes de debug (cilium bpf policy list, cilium service list, cilium status) — dans la roadmap CKA/CKS (609). Étape 1 : Pré-requis : CKA ou expérience k8s équivalente (609)."
date_ajout: "2026-11"
nom: "Certification Cilium CCAE : valider ses compétences eBPF"
emoji: "🏆"
domaine: "Développement"
signal: "Se certifier Cilium CCAE (Cilium Certified Associate Engineer) en 2027 pour valider ses compétences eBPF/Cilium : CNI eBPF, NetworkPolicy L3-L7, Hubble, service mesh, dépannage (cilium bpf policy list, cilium service list). Dans la roadmap CKA/CKS (609). Utilise pour monter en compétence reconnue ou recruter. N'utilise pas comme seule preuve (expérience de prod requise)."
mot_cle: "certification CCAE Cilium 2027 eBPF CKA CKS roadmap cilium bpf policy list service list hubble dépannage"
nom_court: "CCAE"
branche: "D16"
synonymes: ["passer la certification Cilium CCAE en 2027 (eBPF, Cilium)", "CKA/CKS (609) puis CCAE : la roadmap réseau k8s 2027", "cilium bpf policy list / cilium service list : les commandes de l'exam"]
cross_refs: [1721, 609, 205]
tags: ["2027"]
depends_on: [1721]
---

## 1728. 🏆 Certification Cilium CCAE : valider ses compétences eBPF (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Préparer la certification Cilium CCAE en 2027 (associate engineer eBPF/Cilium) : CNI eBPF, NetworkPolicy L3-L7, Hubble, service mesh, commandes de debug (cilium bpf policy list, cilium service list, cilium status) — dans la roadmap CKA/CKS (609).

**Quand l'utiliser (triggers)** :
- quelle certification réseau k8s après CKA/CKS en 2027 ? (CCAE)
- cilium bpf policy list : voir les programmes eBPF attachés
- cilium service list : voir le load balancing eBPF

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es ingénieur réseau k8s. Tu suis le syllabus CCAE (Cilium 1721, Hubble 1722, mesh 1727, debug CLI), tu t'entraînes sur un cluster de test (kind/minikube + Cilium), tu passes l'examen en ligne (proctored). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Un cluster de test (kind + Cilium 1721)
- Le syllabus CCAE officiel
- L'examen en ligne

**Méthode** :
1. Pré-requis : CKA ou expérience k8s équivalente (609).
2. Syllabus CCAE : architecture Cilium (agent, operator, eBPF dataplane), installation (CLI/helm), NetworkPolicy L3-L7, Hubble (1722), service mesh (1727), sécurité (Tetragon 1725).
3. Labo : kind create cluster + cilium install, puis exercices : CiliumNetworkPolicy L7, hubble observe, cilium bpf policy list, cilium service list, cilium status --wait, debug d'un flux bloqué.
4. Examen : QCM + lab live en ligne (proctored), ~2 h, validité 2 ans.
5. Après : CCAE puis éventuellement Cilium Certified Professional (expert).

**Sorties attendues** :
- La certification CCAE obtenue (ou le plan de révision)
- Le lab d'entraînement (kind + Cilium + exercices CLI)
- La roadmap CKA→CKS→CCAE documentée (205)

**Exemple de prompt** :
> « Après CKA/CKS (609), quelle certif réseau en 2027 ? Prépare la CCAE Cilium : lab kind+Cilium (1721), syllabus (NetworkPolicy L7, Hubble 1722, mesh 1727, Tetragon 1725), commandes de debug (cilium bpf policy list, service list, status), examen en ligne proctored 2 h. »

**Cas d'usage** : Montée en compétence réseau k8s reconnue. S'articule avec skills 1721 (Cilium), 609 (k8s), 205 (compétences) et 1722 (Hubble).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
