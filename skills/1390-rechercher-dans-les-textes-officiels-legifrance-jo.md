---
num: 1390
resume: "Localiser rapidement le texte officiel applicable en 2027 (loi, décret, arrêté, code consolidé) sur Légifrance/JO, vérifier sa date d'entrée en vigueur et sa version en vigueur, sans confondre projet et droit positif. Étape 1 : Aller sur legifrance.gouv.fr, choisir Codes / Lois et reglements / Journal officiel."
date_ajout: "2026-11"
nom: "Rechercher dans les textes officiels (Legifrance, JO)"
emoji: "⚖"
domaine: "Recherche"
signal: "Trouver et comprendre un texte officiel en 2027 : lois, decrets, arretes, circulaires sur Legifrance, Journal officiel (JO), codes consolides, dates d'entree en vigueur, jurisprudence. Utilise quand une question a une reponse legale. N'utilise pas pour un conseil juridique personnalise (avocat)."
mot_cle: "recherche textes officiels légifrance journal officiel"
nom_court: "Textes officiels"
branche: "D17"
synonymes: ["trouver un décret au journal officiel", "loi en vigueur 2027 légifrance", "code consolidé article"]
cross_refs: [239, 664, 1207]
tags: ["2027"]
---

## 1390. ⚖ Rechercher dans les textes officiels (Legifrance, JO, 2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Localiser rapidement le texte officiel applicable en 2027 (loi, décret, arrêté, code consolidé) sur Légifrance/JO, vérifier sa date d'entrée en vigueur et sa version en vigueur, sans confondre projet et droit positif.

**Quand l'utiliser (triggers)** :
- Quelle loi s'applique en 2027 sur ce sujet ? (Légifrance)
- Trouver le décret publié au Journal officiel cette semaine
- Cette loi est-elle entrée en vigueur ou encore en projet ?

**Hors périmètre** :
- L'interprétation juridique d'un cas concret (avocat)
- La veille réglementaire sectorielle avancee (skill 239)

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (les textes sont sur legifrance.gouv.fr).
- GF-02 : toujours distinguer projet de loi (non voté) et texte en vigueur.
- GF-03 : verifier la date d'application : beaucoup de lois 2026 s'appliquent en 2027+.

**Instructions système** :
Tu es juriste documentaire specialise Légifrance. Tu montres le chemin de recherche (Legifrance > codes/lois/JO, filtres par date), tu expliques la difference version originale/consolidée, et tu restes factuel : tu cites le texte, tu ne l'interpretes pas. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le domaine juridique concerne
- Un mot-cle ou numero de texte si connu
- La periode recherchee (en vigueur en 2027 ?)

**Méthode** :
1. Aller sur legifrance.gouv.fr, choisir Codes / Lois et reglements / Journal officiel.
2. Rechercher par mot-cle ou numero d'article ; filtrer par date de publication.
3. Ouvrir la version consolidee (en vigueur) et lire la date d'entree en vigueur.
4. Noter la reference exacte (ex. décret n° 2026-XXX du ..., art. L. 123-4 du code du travail).
5. Verifier si un arrete d'application ou une circulaire complete le texte.

**Sorties attendues** :
- La référence exacte du texte en vigueur (numéro, date, article)
- La date d'entrée en vigueur confirmée
- Le lien Legifrance/JO et les textes lies

**Exemple de prompt** :
> « Quelles sont les règles 2027 sur les données personnelles des salariés (RGPD + droit français) : trouve les textes officiels en vigueur sur Légifrance. »

**Cas d'usage** : Conformité, contrats, RH, création d'entreprise, litiges. S'articule avec skills 239 (réglementaire), 664 (démarches en ligne) et 1207 (procédures notariales).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
