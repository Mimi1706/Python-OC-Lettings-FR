from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("lettings/", views.lettings_index, name="lettings_index"),
    path("lettings/<int:letting_id>/", views.letting, name="letting"),
    path("profiles/", views.profiles_index, name="profiles_index"),
    path("profiles/<str:username>/", views.profile, name="profile"),
    path("admin/", admin.site.urls),
    path("error_500/", views.simulate_error_500, name="simulate_500"),
]

# Define custom error views
handler404 = views.error_404
handler500 = views.error_500
