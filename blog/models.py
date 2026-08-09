from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.


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

    title = models.CharField(max_length=1000)
    slug = models.SlugField(max_length=256, unique=True)
    content = models.TextField()

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
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
