CI/CD Pipeline and Deployment
=============================

This section outlines the CI/CD pipeline setup and deployment process for the project:

- **Continuous Integration**: Two jobs were created for building and testing the application.
- **Continuous Deployment**: One job was set up for the deployment of the image application on DockerHub and one job was set up for the deployment of the project on Render.

DockerHub
---------

A Dockerfile was generated in this project using the command:

.. code-block:: bash

   docker init

This Dockerfile defines the instructions for creating a Docker image that contains the application’s data and structure. The generated Docker image is pushed to DockerHub, where it is stored for later use.

DockerHub Job
^^^^^^^^^^^^^

The CI/CD job responsible for pushing the Docker image to DockerHub is named `dockerhub`. This job automates the process of building the Docker image and pushing it to the DockerHub repository.

You can access Docker Hub at `DockerHub <https://hub.docker.com/>`_.

For simplicity, the Docker image is tagged with `:latest`, ensuring that Render always pulls the most recent version when deploying the application.

The image stored on DockerHub will be pulled by Render to set up and deploy the application, ensuring consistency across development, testing, and production environments.

Render
------

We chose Render to host the preview of the project.

The web service on Render was created with the image URL from the Docker registry (DockerHub) and configured with an API key created in the account settings and stored in GitHub secret keys.

A live version of the project is available at `the following URL <https://python-oc-lettings-fr-qgyr.onrender.com/>`_.