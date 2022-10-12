from django.forms import ModelForm
from .models import Post, Comment, User
from django.contrib.auth.forms import UserCreationForm

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'content']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['user', 'body']