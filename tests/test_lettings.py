from django.test import Client
from django.urls import resolve, reverse

client = Client()

def test_lettings_url():
    path = reverse("lettings_index")
    assert path == "/lettings/"
    assert resolve(path).view_name == "lettings_index"