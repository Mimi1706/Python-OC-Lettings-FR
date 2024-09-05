Pipeline CI/CD et Déploiement
=============================
Un pipeline CI/CD a été mis en place avec les étapes suivantes :

- Compilation et exécution de tests unitaires (couverture > 80 %).
- Conteneurisation de l’application avec **Docker**
- Déploiement automatique sur la plateforme Render, uniquement si la compilation et les tests réussissent.

Le site déployé doit correspondre à l’apparence et au fonctionnement local.
