from django import forms
from django.core.exceptions import ValidationError

from .models import Post


class PostForm(forms.ModelForm):
    content = forms.CharField(min_length=20)

    class Meta:
        model = Post
        fields = [
            'post_category',
            'author',
            'header',
            'text',
        ]

    def clean(self):
        cleaned_data = super().clean()
        content = cleaned_data.get("text")
        header = cleaned_data.get("header")
        if content is not None and len(content) < 40:
            raise ValidationError({
                "header": "Текст статьи не может быть менее 40 символов."
            })
        header = cleaned_data.get("header")
        if header == content:
            raise ValidationError(
                "Заголовок не может быть идентичен посту."
            )

        return cleaned_data