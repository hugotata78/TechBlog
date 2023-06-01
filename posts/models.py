from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(get_user_model(), related_name='categories',on_delete=models.CASCADE)
    

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(get_user_model(), related_name='posts', on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category,related_name='posts', blank=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    comment = models.TextField()
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    owner = models.ForeignKey(get_user_model(),related_name='comments', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
    
    def __str__(self):
        return self.comment

