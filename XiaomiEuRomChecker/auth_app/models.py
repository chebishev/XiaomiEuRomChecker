from django.db import models
from django.contrib.auth import models as auth_models


# Create your models here.
class AuthUser(auth_models.AbstractUser):
    preferred_device = models.CharField(max_length=40, default='No Device')

    def __str__(self):
        return self.username