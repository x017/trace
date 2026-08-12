from django.urls.conf import path
from .views import PostListView, PostCreateView

app_name = "post"
urlpatterns = [
    path("", PostListView.as_view(), name="list"),
    path("create/", PostCreateView.as_view(), name="create"),
]
