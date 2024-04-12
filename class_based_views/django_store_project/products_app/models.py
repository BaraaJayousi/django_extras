from django.db import models

# Create your models here.

class ProductManager(models.Manager):
  def get_product(self,id):
    product = self.filter(id=id).first()
    if product:
      return product
    return None
  
  def delete_product(self, id):
    if self.get_product(id):
      self.get_product(id).delete()

class Manufacturer(models.Model):
  name= models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name


class Product(models.Model):
  name = models.CharField(max_length=100)
  price=models.DecimalField(max_digits=11, decimal_places=2)
  manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
  description=models.TextField(blank=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  objects = ProductManager()