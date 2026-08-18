from django.urls.conf import path
from .views import PostDetailView, PostListView, PostCreateView, PostUpdateView

app_name = "post"
urlpatterns = [
    path("", PostListView.as_view(), name="list"),
    path("create/", PostCreateView.as_view(), name="create"),
    path("<int:pk>/detail/", PostDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", PostUpdateView.as_view(), name="update"),
]
