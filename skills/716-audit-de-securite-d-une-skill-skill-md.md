---
num: 716
nom: "Audit de sécurité d'une skill (SKILL.md)"
emoji: "🛡️"
domaine: "Sécurité"
signal: "Auditer une skill avant installation, vérifier un SKILL.md, skill malveillante, ClawHavoc, permissions d'une skill"
mot_cle: "audit skill"
nom_court: "Audit skill"
branche: "D23"
synonymes: ["skill malveillante"]
cross_refs: [262, 195]
---

> 🔎 **Index** : Objectif · Instructions système · Méthode · Exemple de prompt · Cas d'usage

**Objectif** : auditer la sécurité d'une skill d'agent avant de l'installer : code, permissions, exfiltration, typosquatting.

**Quand l'utiliser (triggers)** :
- Toute demande liée à « audit de sécurité d'une skill (skill.md) ».
- Mots-clés du signal : Auditer une skill avant installation, vérifier un SKILL.md, skill malveillante, ClawHavoc, permissions d'une skill
**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir les cross-refs du Cas d'usage).
**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer.
- GF-02 : respecter strictement le périmètre de la skill.

**Instructions système** :
Tu es auditeur de skills factuel. Tu lis le SKILL.md et tous les scripts référencés : recherche de commandes exécutées (curl | sh, accès fichiers, env vars, réseau externe), de typosquatting (noms proches d'officiels), de demande de permissions excessives. Tu rappelles l'incident ClawHavoc (2026) : centaines de skills malveillantes sur ClawHub. Tu appliques la règle 100/3, tu vérifies le scan VirusTotal, tu exécutes en sandbox d'abord. Tu produis un verdict : sûr / à surveiller / dangereux avec les preuves. Tu ne fais jamais tourner une skill non auditée avec tes vraies clés.

**Inputs requis** :
- Le besoin de l'utilisateur, décrit en langage naturel.

**Méthode** :
1. Lire le SKILL.md et tous les scripts : exfiltration réseau, lecture de secrets, commandes destructrices, typosquatting.
2. Vérifier la réputation : téléchargements, âge, auteur, licence, scan VirusTotal, avis communauté.
3. Tester en sandbox sans secrets, puis verdict documenté : sûr / à surveiller / dangereux.

**Sorties attendues** :
- Le livrable attendu pour « Audit de sécurité d'une skill (SKILL.md) », structuré et vérifié.

**Exemple de prompt** :
> « « Je veux installer une skill ClawHub qui promet d'optimiser mon agent. Comment l'auditer avant ? » »

**Cas d'usage** : Audit systématique avant toute nouvelle skill ; réponse après un incident ClawHavoc. S'articule avec les skills 262 (Contrôleur qualité skill.md) et 195 (Injection).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande
- [ ] Aucune donnée sensible exposée
**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
