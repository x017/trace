from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
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
