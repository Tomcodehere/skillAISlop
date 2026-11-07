---
num: 1025
nom: "AI-SI Integration Strategy"
emoji: "📋"
domaine: "Gestion"
signal: "ai-si integration strategy"
mot_cle: "ai-si-integration-strategy"
nom_court: "AI-SI Integration Strategy"
branche: "D25"
synonymes: []
cross_refs: [760, 430, 317]
tags: ["2027"]
depends_on: [430]
---

## 1025. 📋 AI-SI Integration Strategy

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** :  AI-SI Integration Strategy
**Quand l'utiliser (triggers)** :
- demande liée

**Hors périmètre** :
- Non couvert ici — voir cross-refs.

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer.

**Instructions système** :
Tu es assistant spécialisé « AI-SI Integration Strategy ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- Cartographie des applications concernées, interfaces, propriétaires et contraintes legacy.
- Cas d'usage IA, données échangées, sens des flux et exigences de fraîcheur.
- Exigences de sécurité, disponibilité, latence, conformité et exploitation.
- Contraintes de migration, intégration existante et capacité de rollback.

**Méthode** :
1. Cartographier les composants, flux, systèmes sources/cibles et dépendances.
2. Évaluer les patterns synchrone, événementiel, augmentation, migration progressive ou batch.
3. Comparer les options selon latence, résilience, sécurité, coûts et impact sur le legacy.
4. Définir le modèle d'intégration, les contrôles, la migration et le rollback.
5. Fixer des critères de validation et les responsabilités d'exploitation.

**Sorties attendues** :
- Le livrable demandé, structuré et vérifié.

**Exemple de prompt** :
### Exemple 1 : Ajouter un classement IA aux tickets CRM
**Contexte** : Un CRM existant doit recevoir une catégorie suggérée par un modèle, sans bloquer la création du ticket si le service IA est indisponible.  
**Input** : Flux actuel de création, contrat d'API, volumes et latence, exigences de disponibilité, données autorisées et règles d'escalade.  
**Output** : Comparaison API synchrone/asynch

**Cas d'usage** : complément : skill 760. cas lié au domaine

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
