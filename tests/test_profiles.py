from django.test import Client
from django.urls import resolve, reverse

client = Client()

def test_profiles_url():
    path = reverse("profiles_index")
    assert path == "/profiles/"
    assert resolve(path).view_name == "profiles_index"