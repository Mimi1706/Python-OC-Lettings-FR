Database Architecture
=====================

This document provides an overview of the models used in the application, including their attributes and relationships.

Address Model
-------------

Represents a physical address.

Attributes
^^^^^^^^^^

**number** (*PositiveIntegerField*)
    - Street number of the address.
    - **Validation**: Must be a positive integer with a maximum value of 9999.

**street** (*CharField*)
    - Name of the street.
    - **Max length**: 64 characters.

**city** (*CharField*)
    - Name of the city.
    - **Max length**: 64 characters.

**state** (*CharField*)
    - State abbreviation (2 letters).
    - **Max length**: 2 characters.
    - **Validation**: Must have a minimum length of 2 characters.

**zip_code** (*PositiveIntegerField*)
    - Postal code.
    - **Validation**: Must be a positive integer with a maximum value of 99999.

**country_iso_code** (*CharField*)
    - ISO country code.
    - **Max length**: 3 characters.
    - **Validation**: Must have a minimum length of 3 characters.

Methods
^^^^^^^

**`__str__()`**
    - Returns a string representation of the address formatted as `'number street'`.

Meta Options
^^^^^^^^^^^^

**verbose_name_plural**
    - "Addresses"

Letting Model
-------------

Represents a rental property.

Attributes
^^^^^^^^^^

**title** (*CharField*)
    - Title (name) of the letting.
    - **Max length**: 256 characters.

**address** (*OneToOneField*)
    - Associated address for the letting.
    - **Relationship**: One-to-One relationship with the `Address` model.
    - **On deletion**: CASCADE (delete the letting if the associated address is deleted).

Methods
^^^^^^^

**`__str__()`**
    - Returns the title of the letting.

Profile Model
-------------

Represents a user profile.

Attributes
^^^^^^^^^^

**user** (*OneToOneField*)
    - The associated user account.
    - **Relationship**: One-to-One relationship with Django's built-in `User` model.
    - **On deletion**: CASCADE (delete the profile if the associated user account is deleted).
    - **Related name**: `profiles_profile`

**favorite_city** (*CharField*)
    - The user's favorite city (optional).
    - **Max length**: 64 characters.
    - **Blank**: True (this field can be empty).

Methods
^^^^^^^

**`__str__()`**
    - Returns the username of the associated user.