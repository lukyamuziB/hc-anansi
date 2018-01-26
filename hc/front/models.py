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
