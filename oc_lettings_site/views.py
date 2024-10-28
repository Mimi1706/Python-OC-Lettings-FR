from django.shortcuts import render
from lettings.models import Letting
from profiles.models import Profile
import sentry_sdk


def index(request):
    """
    Render the homepage.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered homepage.
    """
    try:
        return render(request, "index.html")
    except Exception as e:
        sentry_sdk.capture_exception(e)
        return render(request, "errors/error_500.html", status=500)


def lettings_index(request):
    """
    Render a list of all lettings.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered page with a list of all lettings.
    """
    try:
        lettings_list = Letting.objects.all()
        context = {"lettings_list": lettings_list}
        return render(request, "lettings/index.html", context)
    except Exception as e:
        sentry_sdk.capture_exception(e)
        return render(request, "errors/error_500.html", status=500)


def letting(request, letting_id):
    """
    Render details for a specific letting.

    Args:
        request (HttpRequest): The HTTP request object.
        letting_id (int): The ID of the letting to retrieve.

    Returns:
        HttpResponse: Rendered page with details of the specified letting.
    """
    try:
        letting = Letting.objects.get(id=letting_id)
        context = {
            "title": letting.title,
            "address": letting.address,
        }
        return render(request, "lettings/letting.html", context)
    except Letting.DoesNotExist:
        return render(request, "errors/error_404.html", status=404)
    except Exception as e:
        sentry_sdk.capture_exception(e)
        return render(request, "errors/error_500.html", status=500)


def profiles_index(request):
    """
    Render a list of all user profiles.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered page with a list of all user profiles.
    """
    try:
        profiles_list = Profile.objects.all()
        context = {"profiles_list": profiles_list}
        return render(request, "profiles/index.html", context)
    except Exception as e:
        sentry_sdk.capture_exception(e)
        return render(request, "errors/error_500.html", status=500)


def profile(request, username):
    """
    Render a specific user profile based on username.

    Args:
        request (HttpRequest): The HTTP request object.
        username (str): The username of the profile to retrieve.

    Returns:
        HttpResponse: Rendered page with the specified user profile.
    """
    try:
        profile = Profile.objects.get(user__username=username)
        context = {"profile": profile}
        return render(request, "profiles/profile.html", context)
    except Profile.DoesNotExist:
        return render(request, "errors/error_404.html", status=404)
    except Exception as e:
        sentry_sdk.capture_exception(e)
        return render(request, "errors/error_500.html", status=500)


def error_404(request, exception):
    """
    Render a custom 404 error page.

    Args:
        request (HttpRequest): The HTTP request object.
        exception (Exception): The exception that triggered the 404 error.
        Needs exception parameter to avoid SystemCheckError with Sentry

    Returns:
        HttpResponse: Rendered 404 error page.
    """
    return render(request, "errors/error_404.html", status=404)


def error_500(request):
    """
    Render a custom 500 error page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered 500 error page.
    """
    return render(request, "errors/error_500.html", status=500)


def simulate_error_500(request):
    """
    Simulate a 500 server error by raising an exception.

    Args:
        request (HttpRequest): The HTTP request object.

    Raises:
        Exception: Always raises an exception to simulate a 500 error.
    """
    try:
        raise Exception("Simulating a 500 error!")
    except Exception as e:
        sentry_sdk.capture_exception(e)
        return render(request, "errors/error_500.html", status=500)
