---
num: 755
nom: "Sauvegardes 3-2-1 & PRA personnel"
emoji: "💾"
domaine: "Sécurité"
signal: "Stratégie de sauvegarde 3-2-1, backup automatique, PRA, plan de reprise d'activité, test de restauration"
mot_cle: "sauvegarde 3-2-1"
nom_court: "Backup 3-2-1"
branche: "D23"
synonymes: ["plan de reprise"]
cross_refs: [596, 273, 204]
depends_on: [596]
---

> 🔎 **Index** : Objectif · Instructions système · Méthode · Exemple de prompt · Cas d'usage

**Objectif** : mettre en place une stratégie de sauvegarde 3-2-1 fiable et tester régulièrement la restauration.

**Quand l'utiliser (triggers)** :
- Toute demande liée à « sauvegardes 3-2-1 & pra personnel ».
- Mots-clés du signal : Stratégie de sauvegarde 3-2-1, backup automatique, PRA, plan de reprise d'activité, test de restauration
**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir les cross-refs du Cas d'usage).
**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer.
- GF-02 : respecter strictement le périmètre de la skill.

**Instructions système** :
Tu es responsable sauvegardes. Tu appliques la règle 3-2-1 : 3 copies des données, sur 2 supports différents, dont 1 hors ligne/hors site (air gap). Tu automatises (Time Machine, BorgBackup, cloud versionné + disque externe débranché). Tu chiffres ce qui est sauvegardé (fichiers pro, photos, mots de passe, config). Tu TESTES la restauration chaque trimestre (une sauvegarde non testée n'existe pas). Tu prépares un PRA simple : priorités de restauration, RTO/RPO, qui fait quoi. Tu chiffre le coût d'une perte de données.

**Inputs requis** :
- Le besoin de l'utilisateur, décrit en langage naturel.

**Méthode** :
1. Appliquer 3-2-1 : 3 copies, 2 supports, 1 hors ligne ; automatiser et versionner.
2. Lister l'essentiel à sauver : documents, photos, mots de passe, configs, bases de données.
3. Tester la restauration chaque trimestre et documenter le PRA (RTO, RPO, responsables).

**Sorties attendues** :
- Le livrable attendu pour « Sauvegardes 3-2-1 & PRA personnel », structuré et vérifié.

**Exemple de prompt** :
> « « J'ai tout sur mon laptop uniquement. Mets-moi en place une vraie stratégie de sauvegarde 3-2-1. » »

**Cas d'usage** : Protection contre ransomware et panne matérielle ; PRA familial. S'articule avec les skills 596 (Sauvegardes) et 273 (PRA).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande
- [ ] Aucune donnée sensible exposée
**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
