---
num: 1547
resume: "Implémenter la client-side prediction en 2027 : le client applique chaque input localement immédiatement (avec numéro de séquence), l'envoie au serveur; à chaque état serveur reçu (ack du dernier input traité), il réapplique les inputs non acquittés sur cet état = réconciliation (pas de téléportation). Étape 1 : Client : à chaque input, seq++, appliquer localement (prediction, 0 latence perçue), e"
date_ajout: "2026-11"
nom: "Prediction client et reconciliation serveur"
emoji: "🔮"
domaine: "Game Dev"
signal: "Implémenter la prédiction côté client en 2027 : le client simule localement son personnage dès l'input (réponse instantanée), envoie l'input au serveur; à la réception de l'état serveur (ack), si divergence → réconcilier (rejouer les inputs non acquittés par-dessus l'état serveur). Utilise pour tout jeu d'action en ligne. N'utilise pas pour un tour par tour."
mot_cle: "prédiction client input immédiat reconciliation rejouer inputs non ack"
nom_court: "Prédiction"
branche: "D1"
synonymes: ["mon perso répond instantanément malgré 100 ms de ping", "réconciliation : état serveur + rejouer mes inputs non ack", "input sequence number et acquittement serveur"]
cross_refs: [1546, 1545, 1544]
tags: ["2027"]
depends_on: [1544]
---

## 1547. 🔮 Prediction client et reconciliation serveur (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Implémenter la client-side prediction en 2027 : le client applique chaque input localement immédiatement (avec numéro de séquence), l'envoie au serveur; à chaque état serveur reçu (ack du dernier input traité), il réapplique les inputs non acquittés sur cet état = réconciliation (pas de téléportation).

**Quand l'utiliser (triggers)** :
- 100 ms de ping et mon perso avance avec 100 ms de retard
- Appliquer l'input localement tout de suite (prediction)
- À la réponse serveur, rejouer mes inputs non acquittés

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es programmeur réseau client. Tu numérotés les inputs (seq++), tu les stockes dans un buffer; le serveur renvoie lastProcessedSeq dans chaque snapshot; client : état = snapshot serveur, puis rejoue tous les inputs avec seq > lastProcessed sur cet état (même sim que le serveur, 1501). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La sim du joueur côté client (même code que serveur, 1501)
- Le buffer d'inputs envoyés (seq, input, timestamp)
- Les snapshots serveur avec lastProcessedInputSeq

**Méthode** :
1. Client : à chaque input, seq++, appliquer localement (prediction, 0 latence perçue), envoyer {seq, input} au serveur.
2. Serveur : traite les inputs dans l'ordre, renvoie snapshot avec lastProcessedSeq + état monde.
3. Client à la réception : poser l'état du serveur pour MON perso = snapshot; puis rejouer buffer[seq > lastProcessed] dessus (même sim).
4. Les autres entités : interpolation (1546), pas de prédiction.
5. Si grosse divergence (triche/erreur) : snap direct (téléportation) + log (1543).

**Sorties attendues** :
- La prédiction client (0 latence perçue pour son perso)
- La réconciliation propre (rejeu des inputs non ack)
- Le snap de secours si divergence

**Exemple de prompt** :
> « Mon perso a 150 ms de retard à chaque déplacement : ajoute la prédiction client (input appliqué localement + seq), serveur renvoie lastProcessedSeq, client rejoue les inputs non ack sur l'état serveur. »

**Cas d'usage** : Tout jeu d'action en ligne. S'articule avec skills 1546 (snapshots), 1545 (lag comp) et 1544 (archi).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
