from django.http import HttpResponse
from django.shortcuts import render
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
      if user.email == email and user.pasword == password and user.acess_id == 1:
        return render(request, 'view_admin.html')
    
    return render(request, 'login.html')
  
  
  
  