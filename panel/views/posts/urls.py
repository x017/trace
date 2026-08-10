from django.urls.conf import path
from .views import PostListView

app_name = "post"
urlpatterns = [path("", PostListView.as_view(), name="list")]
