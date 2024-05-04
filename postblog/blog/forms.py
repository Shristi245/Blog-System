from django import forms


from blog.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment




# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['name', 'email', 'body']
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields= ['title', 'content']





# class CreateUserForm(UserCreationForm):
    
#     class Meta:
#         model = User
#         fields = ("first_name", "last_name", "username", "email", "password1", "password2")
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']


    