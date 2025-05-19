from django.db import models

# Create your models here.
class TimeStampModel(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  class Meta:
    abstract = True

class Product(TimeStampModel):
  name = models.CharField(max_length=35)
  price = models.FloatField()
  description = models.TextField(blank=True,null=True)
  Categories = models.ForeignKey('Category',on_delete=models.CASCADE,related_name='categories')
  stock = models.PositiveIntegerField(default=1)
  images = models.ImageField()

  def __init__(self):
    return self.name

class Category(TimeStampModel):
  name = models.CharField(max_length=30,unique=True)
  image = models.ImageField()

  def __init__(self):
    return self.name
