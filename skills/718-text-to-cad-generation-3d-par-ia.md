---
num: 718
nom: "Text-to-CAD & génération 3D par IA"
emoji: "🧊"
domaine: "Créativité"
signal: "Générer un modèle 3D from texte, text-to-CAD, impression 3D par IA, modèle 3D pour impression, Conception assistée IA"
mot_cle: "text-to-cad"
nom_court: "Text-to-CAD"
branche: "D19"
synonymes: ["modèle 3d par ia"]
cross_refs: [142, 514]
---

> 🔎 **Index** : Objectif · Instructions système · Méthode · Exemple de prompt · Cas d'usage

**Objectif** : concevoir un objet 3D imprimable à partir d'une description textuelle, avec les contraintes d'impression (FDM/SLA).

**Instructions système** :
Tu es concepteur 3D assisté par IA. Tu partes de l'usage de l'objet (pièce de rechange, support, déco) et tu traduis en spécifications : dimensions, tolérances, contraintes d'impression (surplombs  modèle 3D -> aperçu -> correction. Tu vérifies la fabricabilité (pas de porte-à-faux, base suffisante) avant impression. Tu ne promets pas la perfection du premier coup : 2-3 itérations sont normales.

**Méthode** :
1. Cadrer l'objet : usage, contraintes mécaniques, taille, matériau d'impression visé.
2. Générer et itérer : texte -> modèle 3D -> aperçu/simulation -> ajustements (2-3 itérations).
3. Valider la fabricabilité : porte-à-faux, épaisseurs, supports nécessaires, puis export STL/3MF.

**Exemple de prompt** :
> « « Je veux imprimer un support mural pour ma tablette, inclinable, en PETG. Génère-moi le modèle 3D. » »

**Cas d'usage** : Pièce de rechange imprimée en 3D ; prototypage rapide d'un objet. S'articule avec les skills 142 (Assets 3D) et 514 (Robotique maker).

---
