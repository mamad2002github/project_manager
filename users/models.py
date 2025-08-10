from django.contrib.auth.models import AbstractUser
from django.db import models

# مدل کاربر با فیلد نقش اضافه
class User(AbstractUser):
    ROLE_CHOICES = (
        ('manager', 'Project Manager'),
        ('user', 'User'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')
