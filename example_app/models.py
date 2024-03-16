from django.db import models

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Example model
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title