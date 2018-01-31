from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

    
class Blog_post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published = models.DateTimeField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    user = models.ForeignKey(User, blank=True, null=True, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.title}"

class Comment(models.Model):
    comment = models.TextField()
    blog = models.ForeignKey(Blog_post, blank=True, null=True )
    user = models.ForeignKey(User, blank=True, null=True, on_delete = models.CASCADE)
    published = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return f"{self.comment}"