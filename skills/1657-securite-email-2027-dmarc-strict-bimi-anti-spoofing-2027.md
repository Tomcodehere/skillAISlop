---
num: 1657
nom: "Securite email 2027 : DMARC strict, BIMI, anti-spoofing (2027)"
emoji: "📧"
domaine: "Sécurité"
signal: "Sécuriser la messagerie en 2027 contre le spoofing/phishing (509) : SPF + DKIM + DMARC en reject (p=reject, pas none), BIMI (logo certifié dans la boîte de réception), MTA-STS/ DANE pour le chiffrement en transit, filtrage avancé (pièces jointes sandboxées). Utilise pour le domaine de l'entreprise. N'utilise pas pour un perso Gmail (déjà protégé par le fournisseur)."
mot_cle: "DMARC reject SPF DKIM BIMI MTA-STS DANE anti-spoofing email entreprise 2027"
nom_court: "Email sécurisé"
branche: "D23"
synonymes: ["DMARC p=reject pour bloquer le spoofing de notre domaine", "BIMI : notre logo certifié affiché dans Gmail/Outlook", "MTA-STS : chiffrement TLS obligatoire en transit"]
cross_refs: [509, 757, 502]
tags: ["2027"]
depends_on: [509]
---

## 1657. 📧 Securite email 2027 : DMARC strict, BIMI, anti-spoofing (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Sécuriser le domaine email de l'entreprise en 2027 : SPF+DKIM+DMARC p=reject (anti-spoofing), BIMI (logo VMC certifié), MTA-STS (TLS obligatoire en transit), sandbox des pièces jointes, filtrage anti-phishing avancé (509).

**Quand l'utiliser (triggers)** :
- quelqu'un usurpe notre domaine pour du phishing (DMARC p=reject)
- BIMI : faire apparaître notre logo certifié dans les mails
- MTA-STS : forcer le chiffrement TLS avec les autres serveurs mail

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es admin messagerie. Tu publies : SPF (IPs autorisés), DKIM (signature), DMARC p=quarantine 1 mois puis p=reject, BIMI (VMC), MTA-STS policy, et tu surveilles les rapports DMARC (aggregate) via un outil (dmarcian, Valimail). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le domaine et ses serveurs d'envoi (M365, Google, Sendgrid...)
- Les certificats (DKIM, VMC pour BIMI)
- L'outil de monitoring DMARC

**Méthode** :
1. SPF : lister toutes les IPs/services qui envoient pour le domaine (M365, Sendgrid, newsletter...), SPF include.
2. DKIM : clés 2048 bits signées par chaque service, rotation annuelle.
3. DMARC : commencer p=none (monitoring rapports), corriger les échecs 1 mois, puis p=quarantine, puis p=reject (100 %).
4. BIMI : obtenir un VMC (Verified Mark Certificate) pour le logo, publier l'enregistrement BIMI.
5. MTA-STS : policy publiée (_mta-sts), TLS-RPT pour les rapports; DANE optionnel.
6. Filtrage : sandbox des pièces jointes (exécution en VM isolée), liens réécrits et revérifiés au clic (Safe Links 509).

**Sorties attendues** :
- DMARC p=reject + BIMI + MTA-STS publiés et monitorés
- Le taux de spoofing de notre domaine à ~0 (rapports DMARC)
- Le sandbox des pièces jointes actif

**Exemple de prompt** :
> « Un attaquant usurpe notre domaine pour du phishing : publie SPF+DKIM+DMARC p=reject (après 1 mois de monitoring), BIMI (VMC logo), MTA-STS, sandbox des PJ, et surveille les rapports DMARC (dmarcian) — spoofing à ~0. »

**Cas d'usage** : Domaine d'entreprise. S'articule avec skills 509 (phishing), 757 (sensibilisation) et 502 (en-têtes).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
