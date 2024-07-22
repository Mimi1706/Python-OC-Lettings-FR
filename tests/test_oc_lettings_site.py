from django.urls import reverse, resolve
from django.test import Client
client = Client()

def test_index_url():
    path = reverse("index")
    assert path == "/"
    assert resolve(path).view_name == "index"
