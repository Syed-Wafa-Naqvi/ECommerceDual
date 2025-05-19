from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
  id = models.BigAutoField(primary_key=True)
  name = models.CharField(max_length=55)
  address = models.CharField(max_length=255)
  email = models.EmailField()
  
  def __str__(self):
    return self.name