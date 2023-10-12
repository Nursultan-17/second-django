from django.db import models
from django.contrib.auth.models import User


class Answer(models.Model):
    header = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
