from django.urls import path
from .views import SignUpView, PublicProfileView, PrivateProfileView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("accounts/public_profile/<int:pk>", PublicProfileView.as_view(), name="public_profile"),
    path("accounts/profile/<int:pk>/", PrivateProfileView.as_view(), name="profile"),
]
