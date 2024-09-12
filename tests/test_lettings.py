from django.test import Client
from django.urls import reverse
from lettings.models import Letting, Address
import pytest

client = Client()


@pytest.mark.django_db
def test_lettings_index():
    """
    Test the lettings index view.

    This test verifies that the lettings index view:
    1. Returns a 200 status code.
    2. Resolves to the expected URL path '/lettings/'.
    3. Contains the expected HTML content '<title>Lettings</title>'.
    4. Uses the 'lettings_index.html' template.
    """
    path = reverse("lettings_index")
    response = client.get(path)
    content = response.content.decode()
    expected_content = "<title>Lettings</title>"

    assert response.status_code == 200
    assert path == "/lettings/"
    assert expected_content in content
    assert response.templates[0].name == "lettings/index.html"


@pytest.mark.django_db
def test_display_letting():
    """
    Test the display of a specific letting.

    This test verifies that the view for a specific letting:
    1. Returns a 200 status code.
    2. Displays the title of the letting in the response content.
    3. Displays the address details in the response content.
    """
    address = Address.objects.create(
        number=123,
        street="Test Street",
        city="Test City",
        state="TS",
        zip_code=12345,
        country_iso_code="TST",
    )
    letting = Letting.objects.create(title="Test Letting", address=address)
    url = reverse("letting", args=[letting.id])
    response = client.get(url)

    assert response.status_code == 200
    assert "Test Letting" in response.content.decode()
    assert "123 Test Street" in response.content.decode()
