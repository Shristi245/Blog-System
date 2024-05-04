from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone



#category choices
CATEGORY_CHOICES = (
    ('paintings', 'Paintings'),
    ('sculptures', 'Sculptures'),
    ('foods', 'Foods'),

)

class Category(models.Model):
    name = models.CharField(max_length=100)

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=1000)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"pk": self.pk})
    

class Item(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add= True)


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']



  






