from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CampusAuthenticationForm
from .views import ProfileUpdateView, SignUpView

urlpatterns = [
    path(
        "login/",
        LoginView.as_view(authentication_form=CampusAuthenticationForm),
        name="login",
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("profile/", ProfileUpdateView.as_view(), name="profile"),
]