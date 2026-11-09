---
num: 1807
resume: "Monter des artifacts OCI (images, SBOM, configs signées) comme volumes de pods via OCI VolumeSource (stable 1.36), distribués par le registre — immuables, re-pull au restart. Étape 1 : Publier l'artifact : crane/push ou oras push, noter le digest sha256."
lang: "fr"
date_ajout: "2026-11"
nom: "OCI VolumeSource : monter des artifacts OCI comme volumes"
emoji: "📦"
domaine: "Développement"
signal: "Monter n'importe quel artifact d'un registre OCI (image, SBOM, config signée) comme volume de pod via OCI VolumeSource (stable dans k8s 1.36) : le kubelet pull l'artifact et le monte en read-only. Cas : distribuer une config signée, un SBOM (1821), des modèles. Nécessite un registre accessible + éventuellement imagePullSecret. N'utilise pas pour des données volatiles (les volumes OCI sont immutables, re-pull au restart du pod)."
mot_cle: "OCI VolumeSource monter artifact registre OCI comme volume pod image SBOM config signée k8s 1.36 stable"
nom_court: "OCI VolumeSource"
branche: "D16"
synonymes: ["monter une image OCI comme volume dans un pod (OCI VolumeSource)", "distribuer une config signée via registre OCI + volume", "SBOM ou modèle en artifact OCI monté read-only dans le pod"]
cross_refs: [1821, 1822, 609]
tags: ["2027"]
depends_on: [609]
---

## 1807. 📦 OCI VolumeSource : monter des artifacts OCI comme volumes

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Monter des artifacts OCI (images, SBOM, configs signées) comme volumes de pods via OCI VolumeSource (stable 1.36), distribués par le registre — immuables, re-pull au restart.

**Quand l'utiliser (triggers)** :
- ma config signée doit venir du registre OCI, pas d'un ConfigMap
- monter le SBOM de l'image directement dans le pod pour audit
- distribuer des poids de modèle via OCI artifact

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es ingénieur plateforme. Tu publies l'artifact dans le registre OCI (avec digest sha256), tu déclares le volume OCIVolumeSource dans le pod, et tu vérifies l'intégrité par digest (pas par tag). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Un registre OCI accessible
- L'artifact publié avec son digest
- Le pod (imagePullSecret si registre privé)

**Méthode** :
1. Publier l'artifact : crane/push ou oras push, noter le digest sha256.
2. Déclarer dans le pod : volumes: - name: config oci: driver: image, ref: registry.example.com/config@sha256:...
3. Le kubelet pull et monte en read-only au path choisi.
4. Vérifier : contenu présent, digest vérifié (cosign verify si signé 1822).
5. Note : re-pull au restart du pod (immuable), tag mutable déconseillé.

**Sorties attendues** :
- Le volume OCI monté (read-only) dans le pod
- La vérification par digest (sha256)
- La doc : re-pull au restart, utiliser digest pas tag

**Exemple de prompt** :
> « Config TLS signée : oras push registry/config@sha256:abc... puis volume oci ref avec ce digest dans le pod proxy — au restart le kubelet re-pull la même config vérifiée. »

**Cas d'usage** : Distribution d'artifacts immuables signés. S'articule avec skills 1821 (SBOM), 1822 (cosign), 609, 1411 (images).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
