from django.urls import reverse
from django.test import Client

client = Client()


def test_index():
    """
    Test the index view.

    This test verifies that the index view:
    1. Returns a 200 status code.
    2. Resolves to the expected URL path.
    3. Contains the expected content in the response.
    4. Uses the correct template for rendering.
    """
    path = reverse("index")
    response = client.get(path)
    content = response.content.decode()
    expected_content = (
        '<h1 class="page-header-ui-title mb-3 display-6">Welcome to Holiday Homes</h1>'
    )

    assert response.status_code == 200
    assert path == "/"
    assert expected_content in content
    assert response.templates[0].name == "index.html"
