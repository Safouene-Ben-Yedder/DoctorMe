from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField 

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = RichTextField(blank=True,null=True)
    #body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def get_absolute_url(self):
        return reverse('page')
    

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name ='comments' , on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ['date_added']

