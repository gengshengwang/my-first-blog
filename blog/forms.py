# forms
#
# Description: Enter file description here
#
# Author: watson
# Created: 2024/10/7

from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)
