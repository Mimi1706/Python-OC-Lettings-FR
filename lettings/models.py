from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Represents a physical address.

    Attributes:
        number (PositiveIntegerField): Street number of the address.
        street (CharField): Name of the street.
        city (CharField): Name of the city.
        state (CharField): State abbreviation (2 letters).
        zip_code (PositiveIntegerField): Postal code.
        country_iso_code (CharField): ISO country code.
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(
        max_length=3, validators=[MinLengthValidator(3)]
    )

    def __str__(self):
        """
        Return a string representation of the address.

        Returns:
            str: Formatted address as 'number street'.
        """
        return f"{self.number} {self.street}"

    class Meta:
        verbose_name_plural = "Addresses"


class Letting(models.Model):
    """
    Represents a rental property.

    Attributes:
        title (CharField): Title (name) of the letting.
        address (OneToOneField): Associated address for the letting.
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
