from django import forms
from blog.models import Post
from martor.fields import MartorFormField


class PostForm(forms.ModelForm):
    content = MartorFormField()

    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "category",
            "status",
            "header",
        ]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "placeholder": "Post title",
                    "form": "post-form",
                },
            ),
            "category": forms.CheckboxSelectMultiple(),
            "status": forms.Select(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False
