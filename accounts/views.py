from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView

from .forms import CustomUserCreationForm, CustomUserChangeForm

from .models import CustomUser


class SignUpView(CreateView):
    """Sing Up View"""

    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class PublicProfileView(ListView):
    model = CustomUser
    template_name = "public_profile.html"


class PrivateProfileView(UpdateView):
    """Private profile view"""

    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = "profile.html"

    success_url = reverse_lazy("twit_list")
