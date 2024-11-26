from django.urls import path

from .views import TwitCreateView, TwitListView, TwitDetailView, TwitUpdateView, TwitDeleteView, TwitLikeView

urlpatterns = [
    path("<int:pk>/update/", TwitUpdateView.as_view(), name="twit_edit"),
    path("<int:pk>/delete/", TwitDeleteView.as_view(), name="twit_delete"),
    path("<int:pk>/like/", TwitLikeView.as_view(), name="twit_like"),
    path("<int:pk>", TwitDetailView.as_view(), name="twit_detail"),
    path("new/", TwitCreateView.as_view(), name="twit_new"),
    path("", TwitListView.as_view(), name="twit_list"),
]
