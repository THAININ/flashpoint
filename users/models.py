from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)#true so pra poupar tempo depois lembrar de mudar pra false

    def __str__(self):
        return self.username
    
