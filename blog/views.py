from django.views.generic import DetailView, ListView, TemplateView
from martor.utils import markdownify
from blog.models import Post


class Homepage(TemplateView):
    template_name = "index.html"


class PostListView(ListView):
    model = Post
    template_name = "list.html"
    context_object_name = "posts"
    paginate_by = 6  # ← pagination

    def get_queryset(self):
        qs = super().get_queryset().order_by("-created_at")
        q = self.request.GET.get("q")
        if q:
            qs = qs.filter(title__icontains=q) | qs.filter(content__icontains=q)
        return qs

    def get_template_names(self):
        # If request comes from HTMX → return only the partial
        if self.request.headers.get("HX-Request"):
            return ["partials/blog_list.html"]
        return ["list.html"]


class PostDetailView(DetailView):
    model = Post
    template_name = "detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = context["post"]
        context["rendered_content"] = markdownify(post.content)
        return context
