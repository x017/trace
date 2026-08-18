from .views import PostDetailView, PostListView
from django.urls import path

app_name = "blog"
urlpatterns = [
    path("post/list", PostListView.as_view(), name="list"),
    path("post/<slug:slug>", PostDetailView.as_view(), name="detail"),
]
