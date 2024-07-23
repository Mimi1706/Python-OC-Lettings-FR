from django.test import Client
from django.urls import reverse
from lettings.models import Letting, Address
import pytest

client = Client()


@pytest.mark.django_db
def test_lettings_index():
    path = reverse("lettings_index")
    response = client.get(path)
    content = response.content.decode()
    expected_content = "<title>Lettings</title>"
    assert response.status_code == 200
    assert path == "/lettings/"
    assert expected_content in content
    assert response.templates[0].name == "lettings_index.html"


@pytest.mark.django_db
def test_display_letting():
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
