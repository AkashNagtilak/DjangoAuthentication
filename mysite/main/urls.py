from django.urls import path
from . import views
from django.contrib.auth import views as auth_views #import this
app_name = "main"


urlpatterns = [

    path("", views.homepage, name="homepage"),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
    path("password_reset/", views.password_reset_request, name="password_reset")

]