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


def test_error_404():
    """
    Test the custom 404 error view.

    This test verifies that the 404 error view:
    1. Returns a 404 status code.
    2. Uses the correct template for rendering.
    3. Contains expected content in the response.
    """
    response = client.get("/error_404/")
    content = response.content.decode()
    expected_content = "404 Not Found"

    assert response.status_code == 404
    assert response.templates[0].name == "errors/error_404.html"
    assert expected_content in content


def test_simulate_error_500():
    """
    Test the simulate 500 error view.

    This test verifies that the simulate error view:
    1. Returns a 500 status code.
    2. Uses the correct template for rendering.
    3. Contains expected content in the response.
    """
    path = reverse("simulate_500")
    response = client.get(path)
    content = response.content.decode()
    expected_content = "500 Internal Server Error"

    assert response.status_code == 500
    assert response.templates[0].name == "errors/error_500.html"
    assert expected_content in content
