from django.db import models


class RoleType(models.Model):
  access= models.CharField(max_length=60)
  
  
  def __str__(self):
    return f"{self.pk}-{self.access}"
  
  class Meta:
        db_table = 'RoleType'
        
  

class Condominio(models.Model):
    name = models.CharField(max_length=80)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    year_construction = models.CharField(max_length=30)
    number_of_dwellings=models.PositiveIntegerField() #Cantidad de casas o departamentos que hay en el condominio

    def __str__(self):
      return f"[id]: {self.pk} --- [name]:{self.name} --- [address]:{self.address} --- [city]:{self.city} --- [year_construction]:{self.year_construction } --- [Number of dwellings]:{self.number_of_dwellings}"
  
    class Meta:
        db_table = 'Condominios'


class Directivo(models.Model):
    name= models.CharField(max_length=50)
    email = models.CharField(max_length=100,unique=True)
    password= models.CharField(max_length=40)
    acess= models.ForeignKey(RoleType, on_delete=models.CASCADE)
    
    
    def __str__(self):
      return f"[id]: {self.pk} --- [name]:{self.name} --- [email]:{self.email} --- [password]:{self.password} --- [acess]:{self.acess.access}"
    
    
    class Meta:
        db_table='Directivos'


class Empleado(models.Model):
  name= models.CharField(max_length=50)
  lastname= models.CharField(max_length=50)
  age=models.PositiveBigIntegerField()
  gender = models.CharField(max_length=10)
  email = models.CharField(max_length=100,unique=True)
  charge = models.CharField(max_length=100)
  salary = models.DecimalField(max_digits=10, decimal_places=2)
  phone_number = models.CharField(max_length=20)
  condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE)
  
  def __str__(self):
    return f"[id]: {self.pk} --- [name]:{self.name} --- [lastname]:{self.lastname} --- [age]:{self.age} --- [gender]:{self.gender} --- [email]:{self.email} --- [charge]:{self.charge} --- [salary]:{self.salary} --- [phone]:{self.phone_numer} --- [condominio_name]: {self.condominio.name}  --- [condominio_adress]:{self.condominio.address} --- [condominio_city]:{self.condominio.city}"

  class Meta:
        db_table='Empleados'

# Create your models here.
class Users(models.Model):
  name= models.CharField(max_length=50)
  email = models.CharField(max_length=100,unique=True)
  password= models.CharField(max_length=40)
  acess= models.ForeignKey(RoleType, on_delete=models.CASCADE)
  condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE)
  
  def __str__(self):
    return f"[id]: {self.pk} --- [name]:{self.name} --- [email]:{self.email} --- [password]:{self.password} --- [acess]:{self.acess.access} --- [condominio_name]:{self.condominio.name} --- [condominio_adress]:{self.condominio.address} --- [condominio_city]:{self.condominio.city}"

  class Meta:
        db_table = 'Users'
