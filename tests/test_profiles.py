from django.test import Client
from django.urls import reverse
from profiles.models import Profile
from django.contrib.auth.models import User
import pytest

client = Client()


@pytest.mark.django_db
def test_profiles_index():
    path = reverse("profiles_index")
    response = client.get(path)
    content = response.content.decode()
    expected_content = "<title>Profiles</title>"
    assert response.status_code == 200
    assert path == "/profiles/"
    assert expected_content in content
    assert response.templates[0].name == "profiles_index.html"


@pytest.mark.django_db
def test_display_profile():
    user = User.objects.create_user(username="testuser", password="password")
    profile = Profile.objects.create(user=user, favorite_city="Test City")
    url = reverse("profile", args=[user.username])
    response = client.get(url)
    assert response.status_code == 200
    assert response.context["profile"] == profile
    assert "Test City" in response.content.decode()
    assert "testuser" in response.content.decode()
    assert response.templates[0].name == "profile.html"
