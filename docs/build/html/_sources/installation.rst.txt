Installation Guide
===================

This guide provides instructions for installing and launching the project. You can choose between using Docker with Docker Compose or setting up a Python virtual environment manually.

**Option 1: Using Docker and Docker Compose**

1. **Ensure Docker is installed:**
Install Docker by following the instructions on `Docker's official website <https://docs.docker.com/get-docker/>`_.

2. **Clone the Repository:**

   Open your terminal and run:

   .. code-block:: bash

      git clone https://github.com/Mimi1706/Python-OC-Lettings-FR
      cd Python-OC-Lettings-FR

3. **Build and Start the Docker Containers:**

   Run the following command to build the Docker images and start the containers:

   .. code-block:: bash

      docker-compose up --build

4. **Access the Application:**

   Once the containers are up and running, you can access the application at `http://0.0.0.0:8000/`.

5. **Stopping the Docker Containers:**

   To stop and remove the containers, use:

   .. code-block:: bash

      docker-compose down

**Option 2: Setting Up a Python Virtual Environment**

1. **Clone the Repository:**

   Open your terminal and run:

   .. code-block:: bash

      git clone https://github.com/Mimi1706/Python-OC-Lettings-FR
      cd Python-OC-Lettings-FR

2. **Create and Activate a Virtual Environment:**

   - **Create the Virtual Environment:**

     .. code-block:: bash

        python3 -m venv venv

   - **Activate the Virtual Environment:**

    .. code-block:: bash

        source env/bin/activate

3. **Install the Project Requirements:**

   With the virtual environment activated, install the required packages:

   .. code-block:: bash

      pip3 install -r requirements.txt

4. **Launch the Application:**

   Run the following command to start the development server:

   .. code-block:: bash

      python3 manage.py runserver

5. **Access the Application:**

   After starting the server, you can access the application at `http://127.0.0.1:8000/`.

6. **Deactivating the Virtual Environment:**

   When you are done working, deactivate the virtual environment by running:

   .. code-block:: bash

      deactivate
