from django.db import models


class RoleType(models.Model):
  access= models.CharField(max_length=60)
  
  class Meta:
        db_table = 'RoleType'

# Create your models here.
class Users(models.Model):
  name= models.CharField(max_length=50)
  email= models.CharField(max_length=100)
  pasword= models.CharField(max_length=40)
  acess= models.ForeignKey(RoleType, on_delete=models.CASCADE)
  
  class Meta:
        db_table = 'Users'