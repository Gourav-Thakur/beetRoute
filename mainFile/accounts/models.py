from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (('asm','ASM'),('cro','CRO'))
    role = models.CharField(max_length=3, choices=ROLE_CHOICES)