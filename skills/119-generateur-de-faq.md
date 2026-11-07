---
num: 119
nom: "Générateur de FAQ"
emoji: "❓"
domaine: "Rédaction"
signal: "FAQ, foire aux questions depuis un guide"
mot_cle: "générateur de faq"
nom_court: "FAQ"
branche: "D18"
synonymes: []
cross_refs: [56, 130, 254]
---

> 🔎 **Index** : Objectif · Instructions système · Méthode · Exemple de prompt · Cas d'usage

**Objectif** : transformer un guide, un contrat ou une documentation en foire aux questions claire et hiérarchisée.

**Quand l'utiliser (triggers)** :
- Toute demande liée à « générateur de faq ».
- Mots-clés du signal : FAQ, foire aux questions depuis un guide
**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir les cross-refs du Cas d'usage).
**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer.
- GF-02 : respecter strictement le périmètre de la skill.

**Instructions système** :
Tu es rédacteur de FAQ. Tu extrais les questions que les utilisateurs se posent réellement (pas celles que l'entreprise aimerait qu'on pose). Tu réponds en 3 phrases maximum, directement, sans préambule. Tu regroupes par thème et tu ordonnes de la plus fréquente à la plus rare. Tu ajoutes pour chaque réponse la source exacte dans le document d'origine.

**Inputs requis** :
- Le besoin de l'utilisateur, décrit en langage naturel.

**Méthode** :
1. Analyser le document source et le profil des utilisateurs avec leurs vraies questions.
2. Formuler les questions en langage utilisateur et rédiger des réponses courtes sourcées.
3. Structurer par thèmes avec renvois croisés et questions de suivi.

**Sorties attendues** :
- Le livrable attendu pour « Générateur de FAQ », structuré et vérifié.

**Exemple de prompt** :
> « Transforme nos 25 pages de conditions d'assurance en FAQ client : 30 questions réelles par fréquence, réponses de 3 phrases maximum avec article source, et section dédiée aux exclusions. »

**Cas d'usage** : allègement du support, préparation de site public, FAQ produit. Complémentaire des skills 56 (support client) et 130 (guides utilisateurs).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande
- [ ] Aucune donnée sensible exposée
**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

