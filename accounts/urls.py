from django.urls import path
from .views import SignUpView, PublicProfileView, PrivateProfileView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("public_profile/<int:pk>", PublicProfileView.as_view(), name="public_profile"),
    path("profile/<int:pk>/", PrivateProfileView.as_view(), name="profile"),
]
