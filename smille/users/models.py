from django.db import models
from django.contrib.auth.models import AbstractUser

class UsersModels(AbstractUser):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    is_blocked = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "users"