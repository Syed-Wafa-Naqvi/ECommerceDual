from django.db import models
from user.models import *
from shop.models import TimeStampModel
# Create your models here.

class Shipping(TimeStampModel):
  user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
  address = models.CharField(max_length=255)
  city = models.CharField(max_length=30)
  phone_number = models.CharField(max_length=15)
  
  def __init__(self):
    return self.user.name