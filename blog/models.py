from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=True)