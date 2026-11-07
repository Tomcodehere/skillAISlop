---
num: 1544
date_ajout: "2026-11"
nom: "Architecture multijoueur : client-serveur vs P2P (2027)"
emoji: "🖧️"
domaine: "Game Dev"
signal: "Choisir l'architecture réseau d'un jeu multi en 2027 : client-serveur dédié (autoritaire, anti-triche 1543, coûteux en serveurs) vs P2P/host (pas cher, triche facile, latence variable) vs relais (Steam relay, compromis). Critères : compétitif ou coop, budget serveurs, régions. Utilise quand on ajoute le multi (1549). N'utilise pas pour un jeu solo."
mot_cle: "architecture multijoueur client-serveur dédié P2P relais compromis"
nom_court: "Archi multi"
branche: "D1"
synonymes: ["serveur dédié vs P2P pour mon jeu coop", "relais Steam Network (pas cher, pas d'anti-triche)", "client-serveur autoritaire pour un compétitif"]
cross_refs: [1543, 1545, 1549]
tags: ["2027"]
depends_on: [1543]
---

## 1544. 🖧️ Architecture multijoueur : client-serveur vs P2P (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Choisir l'architecture réseau en 2027 : client-serveur dédié (autoritaire, anti-triche, coût serveurs), P2P avec host (gratuit, triche facile), ou relais (Steam Relay, compromis coût/sécurité), selon le type de jeu (compétitif vs coop) et le budget.

**Quand l'utiliser (triggers)** :
- Coop 4 joueurs : serveur dédié ou P2P host ?
- Compétitif : serveur dédié obligatoire (anti-triche)
- Steam Relay pour éviter d'héberger des serveurs

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte réseau jeu. Tu compares : dédié (40 €/mois/VPS, autorité totale, 1543) vs P2P (gratuit, host = autorité, triche, NAT) vs relais (Steam/Photon, 0 infra, mais host voit tout); règle : compétitif = dédié, coop casual = relais/P2P. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le type de jeu (compétitif/coop)
- Le nombre de joueurs par partie (4 vs 100)
- Le budget serveurs et régions cibles

**Méthode** :
1. Compétitif (classé 1549) : client-serveur dédié autoritaire (1543), VPS multi-régions (latence < 50 ms).
2. Coop casual (4 joueurs) : relais Steam Network (pas d'infra) ou P2P host avec migration d'hôte si le host quitte.
3. Hybride : lobby P2P + parties compétitives sur serveurs dédiés loués à la demande.
4. Protocole : UDP (rapide, perte OK) pour positions, TCP fiable pour les événements critiques (achat).
5. Plan de secours : si le serveur tombe, migration ou reconnexion (file d'attente).

**Sorties attendues** :
- L'architecture réseau choisie et justifiée
- Le protocole (UDP/TCP) et la gestion de perte
- Le plan migration d'hôte / failover

**Exemple de prompt** :
> « Mon coop 4 joueurs en P2P lag quand l'hôte a 200 ms de ping : passe en relais Steam Network (0 infra) ou serveurs dédiés si compétitif (1543/1549). »

**Cas d'usage** : Tout jeu multijoueur. S'articule avec skills 1543 (anti-triche), 1545 (lag comp) et 1549 (matchmaking).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
