# board/models.py
from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=120, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    # default=timezone.now

    def __str__(self):
        return f'{self.title} / {self.author}'
