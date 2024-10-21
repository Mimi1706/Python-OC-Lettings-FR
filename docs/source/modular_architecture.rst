Modular Architecture Improvements
=================================

This section describes the improvements made to the architecture of the project by reorganizing it into a more modular structure.

**Technical Aspects**

The current application, `oc_lettings_site`, has been split into two new applications: **lettings** and **profiles**.

The following modifications have been made:

- Created the **lettings** application containing the `Address` and `Letting` models.
- Migrated existing data using Django migration files (SQL direct usage was avoided).
- Created the **profiles** application containing the `Profile` model.
- Removed old database tables after migration.
- Moved URLs (lettings, profiles, lettings_index, profiles_index) to the new applications.

> **Note:** These changes didn't affect the current appearance or functionality of the site.
