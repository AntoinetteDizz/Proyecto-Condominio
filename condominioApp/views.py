from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models  import Users, RoleType
# Create your views here.

# Vista del login
def index(request):
  if request.method == 'GET':
    return render(request, 'login.html')
  else:
    email = request.POST['email']
    password = request.POST['contrasena']
    
    users = Users.objects.filter(email=email)
    
    #Acceso a la vista del usuario admin
    for user in users:
      if user.email == email and user.password == password and user.acess_id == 1:
        return redirect('view_admin/')
    
    return render(request, 'login.html')
  
  
# vista del admin
def admin(request):
  return render(request, 'view_admin.html')


def create_condominium(request):
  return render(request, 'create_condominium.html')
  
  