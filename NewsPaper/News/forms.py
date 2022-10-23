from django import forms
from django.core.exceptions import ValidationError

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            # 'type_post',
            'category',
            'post_name',
            'post_text',
            'author',
        ]

    def clean(self):
        cleaned_data = super().clean()
        post_name = cleaned_data.get('post_name')
        post_text = cleaned_data.get('post_text')
        if post_text == post_name:
            raise ValidationError("Текст поста не может быть идентичен его названию")

        return cleaned_data
