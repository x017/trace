from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Post
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.urls import reverse_lazy
from panel.views.posts.forms import PostForm


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "post/list.html"
    context_object_name = "posts"
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active"] = "posts"
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "post/form.html"
    success_url = reverse_lazy("panel:post:list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "post/form.html"
    success_url = reverse_lazy("panel:post:list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "post/detail.html"
    context_object_name = "post"
