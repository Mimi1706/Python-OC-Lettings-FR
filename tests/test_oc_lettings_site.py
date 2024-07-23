from django.urls import reverse, resolve
from django.test import Client

client = Client()


def test_index():
    path = reverse("index")
    response = client.get(path)
    content = response.content.decode()
    expected_content = '<h1 class="page-header-ui-title mb-3 display-6">'
    "Welcome to Holiday Homes</h1>"
    assert response.status_code == 200
    assert path == "/"
    assert expected_content in content
    assert response.templates[0].name == "index.html"
