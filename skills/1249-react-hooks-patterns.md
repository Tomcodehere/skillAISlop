---
num: 1249
nom: "React Hooks Patterns"
emoji: "💻"
domaine: "Développement"
signal: "Maîtriser React hooks (useState, useEffect, useContext, custom hooks, useCallback, useMemo) pour composants fonctionnels optimisés."
mot_cle: "react-hooks-patterns"
nom_court: "React Hooks Patterns"
branche: "D1"
synonymes: ["react", "hooks", "usestate"]
cross_refs: [1265, 1284, 1231]
tags: ["2027"]
depends_on: [1403]
---

## 1249. 💻 React Hooks Patterns

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Maîtriser React hooks (useState, useEffect, useContext, custom hooks, useCallback, useMemo) pour composants fonctionnels optimisés.

**Quand l'utiliser (triggers)** :
- « React hooks », « useState », « useEffect », « custom hooks », « useCallback », « useMemo », « performance React ».
- Développement composants React fonctionnels.
- Refacto class components → functional components.

**Hors périmètre** :
- Backend Node.js → skill NestJS Architecture ou typescriptJavascript (backend).
- Tests → l'agent qualité.
- CSS/design → l'agent frontend.

**Garde-fous** :
- useEffect dependencies exhaustives (ESLint react-hooks/exhaustive-deps).
- Cleanup useEffect (unsubscribe, clearTimeout).
- useCallback/useMemo seulement si perf issue (pas prématuré).
- Custom hooks prefix use (convention).
- Éviter state mutations (setState(prev => ...) immutabilité).

**Instructions système** :
Tu es assistant spécialisé « React Hooks Patterns ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- Composants à créer (UI, logique).
- State management (local component, Context API, external Zustand/Jotai).
- Performance requirements (memoization nécessaire).

**Méthode** :
1. **useState** (state local) :
2. **useEffect** (side effects) :
3. **useContext** (shared state) :
4. **Custom hooks** (réutilisabilité) :
5. **Performance** (memoization) :

**Sorties attendues** :
- Composants React fonctionnels avec hooks.
- Custom hooks réutilisables.
- Optimisations performance (useCallback, useMemo, React.memo).

**Exemple de prompt** :
### Exemple 1 : [Titre du cas d'usage]
**Contexte** : [Description de la situation]
**Action** : [Ce qui a été fait]
**Résultat** : [Résultat obtenu]

**Cas d'usage** : complément : skill 1265. react ; hooks ; usestate

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
