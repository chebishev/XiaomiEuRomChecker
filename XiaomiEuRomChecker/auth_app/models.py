from django.db import models
from django.contrib.auth import models as auth_models


# Create your models here.
class AuthUser(auth_models.AbstractUser):
    preferred_device = models.CharField(max_length=40, default='No Device', blank=True, null=True)

    def __str__(self):
        return self.username


class ThreadTitle(models.Model):
    title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.title
