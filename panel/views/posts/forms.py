from django import forms

from blog.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "category",
            "status",
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "placeholder": "Post title",
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "placeholder": "Write your post...",
                    "rows": 20,
                }
            ),
            "category": forms.CheckboxSelectMultiple(),
            "status": forms.Select(),
        }
