---
num: 1007
nom: "AD Replication & Sites Management"
emoji: "🧑‍🏫"
domaine: "RH & formation"
signal: "Diagnostiquer et résoudre les problèmes de réplication Active Directory entre contrôleurs de domaine, et concevoir une topologie de sites/liens de sites optimisée pour la bande passante et la latence"
mot_cle: "ad-replication-sites-management"
nom_court: "AD Replication & Sites Managem"
branche: "D24"
synonymes: ["replication", "cassee", "troubleshooting"]
cross_refs: [902]
tags: ["2027"]
---

## 1007. 🧑‍🏫 AD Replication & Sites Management

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Diagnostiquer et résoudre les problèmes de réplication Active Directory entre contrôleurs de domaine, et concevoir une topologie de sites/liens de sites optimisée pour la bande passante et la latence réseau disponibles.

**Quand l'utiliser (triggers)** :
- « réplication AD cassée », « troubleshooting réplication », « repadmin », « USN rollback ».
- « liens de sites AD », « coût de site », « fréquence de réplication ».
- Lenteur de propagation de changements AD (nouveaux comptes, GPO) entre sites.

**Hors périmètre** :
- Conception initiale de l'architecture de sites lors d'un nouveau déploiement → Active Directory Architecture Design (skill associée, même agent).
- Problèmes réseau sous-jacents (coupures de liens, bande passante insuffisante) → l'agent réseau et sécurité réseau.

**Garde-fous** :
- Ne jamais ignorer un échec de réplication de plus de 24h (risque de USN rollback ou de lingering objects).
- Toujours vérifier la résolution DNS en premier : c'est la cause la plus fréquente de problèmes de réplication AD.
- Un intervalle de réplication intersite ne doit jamais dépasser les besoins métier (changements critiques comme les verrouillages de compte).

**Instructions système** :
Tu es assistant spécialisé « AD Replication & Sites Management ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- Topologie des sites AD actuelle et des liens de sites (coût, intervalle de réplication).
- Sortie de `repadmin /replsummary` et `repadmin /showrepl` si troubleshooting.
- Description du symptôme (quels objets ne se répliquent pas, entre quels contrôleurs).

**Méthode** :
1. Collecter `repadmin /replsummary` sur l'ensemble des contrôleurs de domaine pour identifier les échecs.
2. Analyser les erreurs spécifiques (`repadmin /showrepl` sur les contrôleurs en échec) : erreur DNS, erreur réseau, erreur de sécurité Kerberos.
3. Vérifier la résolution DNS des contrôleurs de domaine entre eux (cause la plus fréquente d'échec de réplication).
4. Pour la conception de sites : aligner les liens de sites sur la bande passante réelle disponible, avec des coûts reflétant la hiérarchie de préférence des chemins.
5. Documenter la correction et valider par un `repadmin /replsummary` propre.

**Sorties attendues** :
- Diagnostic de la cause de l'échec de réplication (DNS, connectivité, USN rollback, conflit de schéma).
- Topologie de sites/liens de sites révisée avec coûts et intervalles justifiés.
- Plan de correction avec étapes de validation (`repadmin /replsummary` propre après correction).

**Exemple de prompt** :
### Exemple 1 : Réplication bloquée entre deux contrôleurs de domaine après migration réseau
**Contexte** : Après une migration d'infrastructure réseau, deux contrôleurs de domaine distants ne se répliquent plus.
**Action** : L'agent exécute `repadmin /showrepl` et identifie une erreur de résolution DNS suite au changement d'adresses IP non répercuté dans les enregistrements DNS des contrôleurs.
*

**Cas d'usage** : complément : skill 902. replication ; cassee ; troubleshooting

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
