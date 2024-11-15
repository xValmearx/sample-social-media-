from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    CreateView,
)

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)

from django.urls import reverse_lazy
from .models import Twit


class TwitCreateView(LoginRequiredMixin, CreateView):
    """Create Twit View"""

    model = Twit

    template_name = "twit_new.html"
    fields = ("body",)

    def form_valid(self, form):
        """return user who created the form"""
        form.instance.author = self.request.user
        return super().form_valid(form)


class TwitListView(LoginRequiredMixin, ListView):
    """Twit List View"""

    model = Twit
    template_name = "twit_list.html"


class TwitDetailView(LoginRequiredMixin, DetailView):
    """Twit Detial View"""

    model = Twit
    template_name = "twit_detail.html"


class TwitUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Twit update view"""

    model = Twit
    fields = ("body",)
    template_name = "twit_edit.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class TwitDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Article Delete View"""

    model = Twit
    template_name = "twit_delete.html"
    success_url = reverse_lazy("twit_list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
