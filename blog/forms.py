from django import forms
from .models import Post, Comment
from django.contrib.auth.models import User
from PIL import Image


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

class UserForm(forms.ModelForm):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username', 'password', 'email',)