from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from martor.models import MartorField


class Category(models.Model):
    name = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hex_color = models.CharField(max_length=7)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.created_at}"


class Post(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 1
        PUBLISHED = 2
        ARCHIVED = 3

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    header = models.ImageField(upload_to="headers", null=True, blank=True)
    title = models.CharField(max_length=1000, blank=True)
    slug = models.SlugField(max_length=256, unique=True, blank=True)
    content = MartorField()
    category = models.ManyToManyField(Category, related_name="posts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    status = models.IntegerField(
        choices=Status.choices,
        default=Status.DRAFT,
    )

    def __str__(self):
        return f"{self.title} - {self.created_at}"

    def save(self, *args, **kwargs):
        base_slug = slugify(self.title) or "post"
        slug = base_slug
        counter = 1
        qs = Post.objects.exclude(pk=self.pk)
        while qs.filter(slug=slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        self.slug = slug
        super().save(*args, **kwargs)

    class Meta:
        ordering = ("-created_at",)


class Images(models.Model):
    image = models.ImageField()
    is_active = models.BooleanField(default=True)
    is_header = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
