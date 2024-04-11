from django.db import models

# Create your models here.

class UserManager(models.Manager):
  def login(self,email,password):
    if self.filter(email=email).first():
      if self.filter(password=password).first():
        return True
    return False

class User(models.Model):
  first_name= models.CharField(max_length=45)
  last_name= models.CharField(max_length=45)
  email = models.EmailField()
  password = models.CharField(max_length=100)

  objects = UserManager()

