from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # AbstractUser already gives: username, first_name, last_name, email, password
    # Nothing extra needed — just extend it

    def __str__(self):
        return self.username


class Post(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_constraint=False
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text[:30]