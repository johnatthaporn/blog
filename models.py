from django.db import models
from django_quill.fields import QuillField
from django.urls import reverse
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = QuillField()
    
    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        return reverse('blog:list')