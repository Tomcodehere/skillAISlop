---
num: 1602
resume: "Réduire le JS envoyé au client en 2027 avec les React Server Components (logique/data côté serveur, streaming SSR avec Suspense) et déployer sur edge functions (latence inférieur à 50 ms) — le « retour au serveur ». Étape 1 : Passer les composants en Server Components par défaut (pas de 'use client'), ne garder client que l'interactivité (état, événements)."
lang: "fr"
date_ajout: "2026-11"
nom: "Retour au serveur : React Server Components et edge"
emoji: "☁️"
domaine: "Développement"
signal: "Appliquer le « retour au serveur » en 2027 : React Server Components (RSC) dans Next.js/App Router pour moins de JS envoyé au client, edge functions (Vercel/Cloudflare) pour la latence, streaming SSR. Utilise pour les apps web modernes. N'utilise pas pour du 100 % client (éditeur offline)."
mot_cle: "react server components RSC edge functions streaming SSR 2027"
nom_court: "RSC + edge"
branche: "D1"
synonymes: ["moins de JavaScript envoyé au client (RSC)", "edge functions latence 50 ms", "streaming SSR Suspense 2027"]
cross_refs: [1249, 1612, 253]
tags: ["2027"]
depends_on: [1612]
---

## 1602. ☁️ Retour au serveur : React Server Components et edge (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Réduire le JS envoyé au client en 2027 avec les React Server Components (logique/data côté serveur, streaming SSR avec Suspense) et déployer sur edge functions (latence < 50 ms) — le « retour au serveur ».

**Quand l'utiliser (triggers)** :
- Notre bundle React fait 400 kB, aller en RSC
- edge functions Vercel Cloudflare latence
- streaming SSR avec Suspense 2027

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es dev front architecture. Tu expliques la frontière serveur/client ('use client' uniquement pour l'interactivité), le streaming (Suspense avec fallback skeleton), les Server Actions (mutations sans API), et le déploiement edge. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'app React (Next.js App Router ou migrée)
- Les données à charger côté serveur (DB, API internes)
- L'hébergement edge (Vercel/Cloudflare 1612)

**Méthode** :
1. Passer les composants en Server Components par défaut (pas de 'use client'), ne garder client que l'interactivité (état, événements).
2. Data fetching directement dans le composant serveur (await db...), zéro API intermédiaire pour le rendu initial.
3. Mutations via Server Actions (fonction 'use server' appelée depuis le formulaire).
4. Streaming : Suspense autour des parties lentes (liste longue) avec skeleton, le reste de la page s'affiche vite.
5. Déployer sur edge (Vercel Edge / Cloudflare Pages 1612), mesurer TTFB < 100 ms.

**Sorties attendues** :
- L'app en RSC (bundle client réduit mesuré)
- Le streaming SSR avec skeletons
- Le TTFB edge mesuré (< 100 ms)

**Exemple de prompt** :
> « Notre app React envoie 400 kB de JS : passe en Server Components (Next.js App Router), Server Actions pour les mutations, Suspense streaming, déploiement edge — mesure le bundle et le TTFB avant/après. »

**Cas d'usage** : Apps web modernes, dashboards, e-commerce. S'articule avec skills 1249 (React hooks), 1612 (edge) et 253 (perf web).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
