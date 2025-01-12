from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    CreateView,
    FormView,
)

from django.http import JsonResponse

from django.http import HttpResponse
from django.views import View


from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)

from .forms import CommentForm

from django.urls import reverse_lazy, reverse
from .models import Twit


class TwitCreateView(LoginRequiredMixin, CreateView):
    """Create Twit View"""

    model = Twit

    template_name = "twit_new.html"
    fields = ("body", "image_url")

    def form_valid(self, form):
        """return user who created the form"""
        form.instance.author = self.request.user
        return super().form_valid(form)


class TwitListView(LoginRequiredMixin, ListView):
    """Twit List View"""

    model = Twit
    template_name = "twit_list.html"


class TwitDetailView(LoginRequiredMixin, DetailView, FormView):
    """Artivle Detial View"""

    model = Twit
    form_class = CommentForm
    template_name = "Twit_detail.html"

    def post(self, request, *args, **kwargs):
        """handle post request"""
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.twit = self.object
        comment.author = self.request.user
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        twit = self.get_object()
        return reverse("twit_detail", kwargs={"pk": twit.pk})


class TwitUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Twit update view"""

    model = Twit
    fields = ("body", "image_url")
    template_name = "twit_edit.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class TwitDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Article Delete View"""

    model = Twit
    template_name = "twit_delete.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class TwitLikeView(LoginRequiredMixin, View):
    """Twit Like View"""

    def get(self, request, *args, **kwargs):
        """GET Request"""

        # Get out the data from the Get request
        twit_id = request.GET.get("twit_id", None)
        twit_action = request.GET.get("twit_action", None)

        if not twit_id or not twit_action:
            return JsonResponse({"success": False})

        twit = Twit.objects.get(id=twit_id)

        if twit_action == "like":
            # Do stuff
            twit.likes.add(request.user)
        else:
            twit.likes.remove(request.user)

        return JsonResponse(
            {
                "success": True,
            }
        )
