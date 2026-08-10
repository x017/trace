from django.urls import path, include

app_name = "panel"
urlpatterns = [
    path("", include("panel.views.dashboard.urls")),
    path("posts/", include("panel.views.posts.urls")),
]
