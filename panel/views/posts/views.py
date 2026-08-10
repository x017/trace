from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from blog.models import Post


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "panel/posts.html"
    context_object_name = "posts"
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active"] = "posts"
        return context
