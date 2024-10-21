Documentation
=============

This project uses **Sphinx** to generate structured documentation and **Read the Docs** to host it online, providing easy access and updates.

Updating the Documentation
---------------------------

To update the documentation:

1. Modify or add `.rst` files in the `/docs` directory.

2. From the project root, navigate to the `/docs` folder and run:

   .. code-block:: bash

      cd docs
      make html

This will generate the HTML version in the `_build/html/` directory.

Notes
-----

- If formatting issues arise, clean and rebuild the documentation:

   .. code-block:: bash

      make clean
      make html

- To change the theme, update the `html_theme` value in `conf.py`. The default theme is "alabaster."