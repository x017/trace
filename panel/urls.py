from django.urls import path
from .views import DashboardView, PostListView

app_name = "panel"

urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
    path("posts/", PostListView.as_view(), name="posts"),
    # path("categories/", CategoryListView.as_view(), name="categories"),
]
