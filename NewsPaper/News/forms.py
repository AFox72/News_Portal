from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import  Group
from allauth.account.forms import SignupForm

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

class CommonSignupForm(SignupForm):
    def save(self, requst):
        user = super(CommonSignupForm, self).save(requst)
        basic_group = Group.objects.get(name='common')
        basic_group.user_set.add(user)
        return user