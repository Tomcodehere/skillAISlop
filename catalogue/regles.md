## 📐 Règles du projet (SkillsLibrairy)

> 🔎 **Index** : R1 Indexation · R2 Uniformisation · R3 Routage · R4 Référencement · R5 Audit systématique · R6 Zéro doublon · R7 AGENTS.md & maj trimestrielle · R8 Sync index & routage · R9 Concision des sorties

**R1 — Indexation obligatoire, partout.** Toute section, toute skill et tout document du projet doit commencer par un index. Concrètement :
- Le document a un sommaire global (table des skills).
- Chaque skill ouvre sur une ligne `> 🔎 **Index** : …` listant ses sections.
- Toute nouvelle section de niveau `##` ajoutée au document doit apparaître dans l'index du document, et tout bloc ajouté à une skill doit apparaître dans l'index de la skill.

**R2 — Uniformisation par template.** Toute skill (existante ou nouvelle) doit respecter le **Template officiel de skill** ci-dessous, à l'identique : mêmes sections, dans le même ordre, avec les mêmes libellés. Aucune exception — les sections propres à un domaine (ex. "Table de routage" pour le routeur) se placent entre "Instructions système" et "Exemple".

**R3 — Routage systématique.** Toute nouvelle skill doit être branchée sur le routeur (skill 0) : une ligne dans la table de routage + une branche dans l'arbre de décision. Une skill non routée est considérée comme incomplète.

**R4 — Référencement croisé.** Chaque skill indique, quand c'est pertinent, les skills complémentaires (ex. la skill 1 renvoie aux skills 8 et 17). Le sommaire global reste l'unique source de vérité pour les numéros de skill.

**R5 — Audit systématique à chaque ajout de règle.** Chaque fois qu'une ou plusieurs nouvelles règles sont ajoutées au projet, le script de conformité (canvas « script-conformite-skills ») est exécuté sur le catalogue et le résultat consigné dans la conversation. Une règle fraîchement ajoutée n'est considérée active qu'une fois l'audit repassé : si l'audit révèle des non-conformités, elles sont corrigées avant toute autre évolution du catalogue.

**R6 — Zéro doublon.** Avant d'ajouter une skill, on vérifie qu'aucune skill existante ne couvre déjà le besoin : comparaison des noms, des objectifs et des signaux de routage. En cas de chevauchement, on enrichit la skill existante plutôt que d'en créer une nouvelle. Concrètement : unicité des noms de skills et des signaux de la table de routage (un signal ne peut pas router vers deux skills distinctes pour le même besoin) ; chaque skill porte un emoji pertinent, dont la réutilisation entre skills est permise. Les candidats écartés comme doublons sont consignés lors de l'ajout.

**R7 — Alignement AGENTS.md & mise à jour trimestrielle.** Le projet adopte le format ouvert [AGENTS.md](https://github.com/agentsmd/agents.md) comme mode d'emploi standard pour tout agent IA intervenant sur la bibliothèque : un fichier AGENTS.md (canvas « agents-md-skillslibrairy ») résume le contexte du projet, les règles R1-R8 et les procédures (ajout d'une skill, synchronisation, audit, mise à jour). La bibliothèque se met à jour **4 fois par an** (janvier, avril, juillet, octobre), chaque mise à jour s'appuyant sur ce modèle en lien : veille des nouvelles compétences IA du trimestre (sources de la section Sources d'inspiration), enrichissement conforme à R6, routage complet (R3), puis audit intégral (R5) consigné. Le conservateur (skill 250) et la tâche planifiée trimestrielle du projet déclenchent ce cycle.

**R8 — Synchronisation automatique de l'index et du routage.** À chaque modification du catalogue (ajout, édition, renommage ou retrait d'une skill), l'index et le routage sont mis à jour **automatiquement et immédiatement** : sommaire global, table de routage, arbre de décision, vue d'ensemble et index du document doivent refléter fidèlement l'état réel du catalogue — aucune entrée manquante, orpheline ou en double. **À chaque ajout ou retrait de skill, le compteur de skills (`routage.py count`) et l'export JSON (`routage.py export`) sont régénérés** et leurs canvases (« totalSkillsCount », « Export JSON ») actualisés. Une modification n'est pas terminée tant que le script de conformité (R5) n'a pas été repassé et n'a pas confirmé la synchronisation index/routage.

**R9 — Concision des sorties.** Toute sortie du projet (rapport d'audit, verdict, résumé, consignation) est concise par défaut : verdict en une ligne, seules les non-conformités détaillées, pas de récapitulatif des conformités ni de table intégrale si tout est vert. Le rapport d'audit du script est compact par défaut (`--verbose` pour la table complète). Les réponses et consignations suivent le même principe : l'essentiel d'abord, le détail seulement sur demande ou en cas d'écart.

---
