Amélioration de l’architecture modulaire
=========================================
Nous avons optimisé l'architecture du site web en réorganisant le code pour qu'il soit plus flexible et évolutif.

**Aspects techniques**

L’application actuelle, `oc_lettings_site`, a été scindée en deux nouvelles applications : **lettings** et **profiles**.

Les modifications suivantes ont été apportées :

- Création de l'application **lettings** contenant les modèles `Address` et `Letting`.
- Migration des données existantes en utilisant les fichiers de migration Django (sans SQL direct).
- Création de l'application **profiles** contenant le modèle `Profile`.
- Suppression des anciennes tables de la base de données après migration.
- Déplacement des URLs (lettings, profiles, lettings_index, profiles_index).

> **Note** : Ces changements ne doivent pas affecter l'apparence ni les fonctionnalités actuelles du site.
