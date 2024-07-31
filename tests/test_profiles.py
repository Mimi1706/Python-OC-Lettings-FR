from django.test import Client
from django.urls import reverse
from profiles.models import Profile
from django.contrib.auth.models import User
import pytest

client = Client()


@pytest.mark.django_db
def test_profiles_index():
    """
    Test the profiles index view.

    This test verifies that the profiles index view:
    1. Returns a 200 status code.
    2. Resolves to the expected URL path '/profiles/'.
    3. Contains the expected HTML content '<title>Profiles</title>'.
    4. Uses the 'profiles_index.html' template.
    """
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
    """
    Test the display of a specific user profile.

    This test verifies that the view for a specific user profile:
    1. Returns a 200 status code.
    2. Passes the correct profile object to the template context.
    3. Displays the favorite city and username in the response content.
    4. Uses the 'profile.html' template.
    """
    user = User.objects.create_user(username="testuser", password="password")
    profile = Profile.objects.create(user=user, favorite_city="Test City")
    url = reverse("profile", args=[user.username])
    response = client.get(url)

    assert response.status_code == 200
    assert response.context["profile"] == profile
    assert "Test City" in response.content.decode()
    assert "testuser" in response.content.decode()
    assert response.templates[0].name == "profile.html"
