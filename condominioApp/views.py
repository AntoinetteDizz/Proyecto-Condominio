from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models  import *
# Create your views here.

# Vista del login
def index(request):
  if request.method == 'GET':
    return render(request, 'login.html')
  else:
    email = request.POST['email']
    password = request.POST['contrasena']
    
    admins = Directivo.objects.filter(email=email)
 
    #Acceso a la vista del usuario admin
    for admin in admins:
      if admin.email == email and admin.password == password and admin.acess_id == 1:
        return redirect('view_admin/')
    
    return render(request, 'login.html')
  
  
# vista del admin
def admin(request):
  return render(request, 'view_admin.html')


def create_condominium(request):
  if request.method == 'GET':
    return render(request, 'create_condominium.html')
  else:
    name = request.POST['name']
    address = request.POST['address']
    city =  request.POST['city']
    dwellings = request.POST['dwellings']
    year =  request.POST['year']
    
    Condominio.objects.create(name = name , address =address, city = city ,number_of_dwellings =dwellings, year_construction = year)
    return redirect('/view_admin/')