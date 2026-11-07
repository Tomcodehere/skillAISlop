---
num: 1756
date_ajout: "2026-11"
nom: "RUM : performance réelle des utilisateurs (2027)"
emoji: "📱"
domaine: "Développement"
signal: "Mesurer la performance côté client en 2027 avec le RUM (Real User Monitoring) : la librairie web-vitals injectée dans l'app envoie LCP/INP/CLS réels (1618) des vrais utilisateurs vers l'analytics (1540), agrégés p75 par page/navigateur/zone. Complète le labo (Lighthouse). Utilise quand le SEO/conversion dépend de la vitesse réelle. N'utilise pas pour des données perso (1440, anonymiser)."
mot_cle: "RUM real user monitoring 2027 web-vitals LCP INP CLS réels utilisateurs p75 par page navigateur zone analytics 1540 anonymisé 1440"
nom_court: "RUM 2027"
branche: "D16"
synonymes: ["les métriques réelles des utilisateurs (RUM web-vitals), pas que Lighthouse (labo)", "INP réel p75 par page et par navigateur (Chrome vs Safari)", "anonymiser le RUM (pas d'ID user 1440)"]
cross_refs: [1618, 1540, 253]
tags: ["2027"]
depends_on: [1618]
---

## 1756. 📱 RUM : performance réelle des utilisateurs (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Mesurer la performance réelle côté client en 2027 (RUM) : la lib web-vitals envoie LCP/INP/CLS des vrais utilisateurs (p75 par page/navigateur/zone) vers l'analytics (1540), anonymisé (1440) — complément du labo (Lighthouse).

**Quand l'utiliser (triggers)** :
- Lighthouse dit 95 mais les users disent que c'est lent (RUM vs labo)
- INP réel p75 par page : la page produit est à 600 ms
- RUM anonymisé : pas d'ID utilisateur (1440)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es dev front perf. Tu injectes web-vitals (npm) dans l'app, tu envoies les métriques (LCP/INP/CLS/CLS attribution) vers ton analytics (1540) avec la page, le navigateur, la zone, le type de connexion — jamais d'ID user (1440). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'app web
- La lib web-vitals
- L'analytics cible (1540)

**Méthode** :
1. Installer web-vitals, appeler onCLS/onINP/onLCP avec une fonction qui envoie {name, value, rating, id} + contexte (page, navigateur, zone, 4G/5G) vers l'analytics (1540), anonymisé (hash session 1465, pas d'ID user 1440).
2. Agrégation : p75 par page, par navigateur, par zone, par type de connexion — dashboard (1416).
3. Complément du labo : Lighthouse (CI 1413) pour le dev, RUM pour la réalité ; les deux doivent converger (écart > 20 % = investiguer).
4. Alertes (1417) : INP p75 qui dépasse 200 ms sur une page clé.
5. Corréler avec le business : taux de rebond/conversion vs LCP (1698) pour prouver l'impact.

**Sorties attendues** :
- Le RUM déployé (web-vitals → analytics 1540, anonymisé 1440)
- Le dashboard p75 par page/navigateur/zone + corrélation business (1698)
- Les alertes (1417) sur INP/LCP dégradés + convergence labo/RUM

**Exemple de prompt** :
> « Lighthouse dit 95 mais les users râlent : déploie le RUM 2027 (web-vitals → analytics 1540) — INP p75 réel par page/navigateur/zone (la page produit à 600 ms sur mobile 4G), anonymisé (1440), alertes 1417, corrélation conversion (1698). »

**Cas d'usage** : Performance web réelle. S'articule avec skills 1618 (CWV), 1540 (analytics), 253 (perf web), 1440 (PII) et 1416 (dashboards).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
