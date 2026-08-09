# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic import ListView

from blog.models import Post, Category


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "panel/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "active": "dashboard",
                "total_posts": Post.objects.count(),
                "published_posts": Post.objects.filter(
                    status=Post.Status.PUBLISHED
                ).count(),
                "draft_posts": Post.objects.filter(status=Post.Status.DRAFT).count(),
                "total_categories": Category.objects.count(),
            }
        )
        return context


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "panel/posts.html"
    context_object_name = "posts"
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active"] = "posts"
        return context
