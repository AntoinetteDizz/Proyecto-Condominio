from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from .models  import *
# Create your views here.


# Vista del login
def index(request):

  if request.method == 'GET':
    return render(request, 'login.html')
  else:
    email = request.POST['email']
    password = request.POST['contrasena']
    
    admins = Directivo.objects.filter(email=email, password=password)
    users = Users.objects.filter(email=email, password = password)
 

    #Acceso a la vista del usuario admin
    for admin in admins:
      if admin.email == email and admin.password == password and admin.acess_id == 1:
        return redirect('view_admin/')
    
    # Acceso a la vista del usuario comun 
    for user in users:
      if user.email == email and user.password == password and user.acess_id == 2:
        return redirect('view_user/')
    
    return render(request, 'login.html')



  
# vista del admin
def admin(request):
  return render(request, 'view_admin.html')

def read_condominium(request):
  if request.method == 'GET':
      # Consulta a la tabla Codominio para obtener todos los registros
      condominios = Condominio.objects.all()

      # Pasar los datos al contexto de renderizado
      context = {'condominios': condominios}

      return render(request,'read_condominium.html',context)


def create_condominium(request):
  if request.method == 'GET':
    return render(request, 'create_condominium.html')
  else:
    name = request.POST['name']
    address = request.POST['address']
    city =  request.POST['city']

    year =  request.POST['year']
    
    Condominio.objects.create(name = name , address =address, city = city, year_construction = year)
    return redirect('/view_admin/')
  
  
def update_condominium(request):
    if request.method == 'GET':
        # Consulta a la tabla Codominio para obtener todos los registros
        condominios = Condominio.objects.all()

        # Pasar los datos al contexto de renderizado
        context = {'condominios': condominios}
        return render(request, 'update_condominium.html', context)
    else:
        name = request.POST['name']
        address = request.POST['address']
        city =  request.POST['city']
        year =  request.POST['year']
        
        #obtener el ID del condominio seleccionado del formulario
        condominio_id = request.POST['condominio']
        
        # Actualizar el condominio seleccionado usando su ID
        condominio = Condominio.objects.get(pk=condominio_id)
        condominio.name = name
        condominio.address = address
        condominio.city = city
        condominio.year_construction = year
        condominio.save()

        return redirect('/view_admin/')

def delete_condominium(request):
  if request.method == 'GET':
      condominios = Condominio.objects.all()

      # Pasar los datos al contexto de renderizado
      context = {'condominios': condominios}

      return render(request, 'delete_condominium.html', context)
  else:
     
     condominio_id = request.POST['condominio']

     condominio = get_object_or_404(Condominio, pk=condominio_id)

      # Eliminar el condominio
     condominio.delete()
     
     return redirect('/view_admin/')



def read_owner(request):
  if request.method == 'GET':
    # Obtener todos los propietarios
    owners = Users.objects.all()
    
    # Preparar el contexto con los propietarios
    context = {'usuarios': owners}
    
    # Renderizar la plantilla HTML pasándole el contexto
    return render(request, 'read_owner.html', context)


def create_owner(request):
    
    if request.method == 'GET':
        condominios = Condominio.objects.all()
        context = {'condominios': condominios}
        return render(request, 'create_owner.html', context)
    else:
        name = request.POST['name']
        email = request.POST['email']
        password= request.POST['password']
        condominio_id = request.POST['condominio']
        acess_id = request.POST['acceso']

        Users.objects.create(name=name, email=email,password = password  ,acess_id=acess_id, condominio_id=condominio_id)
        
        return redirect('/view_admin/')

def update_owner(request):
    if request.method == 'GET':
        # Consulta a la tabla Users para obtener todos los registros
        owner = Users.objects.all()
        # Consulta a la tabla Condomios para obtener todos los registros
        condominios = Condominio.objects.all()
        # Pasar los datos al contexto de renderizado
        context = {'usuarios': owner, 'condominios': condominios}
        return render(request, 'update_owner.html', context)
    else:
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        id_user = request.POST['usuario']
        condominio_id = request.POST['condominio']

        # Obtener la instancia de Condominio correspondiente al ID proporcionado
        condominio = get_object_or_404(Condominio, pk=condominio_id)

        # Actualizar el usuario seleccionado usando su ID
        user = Users.objects.get(pk=id_user)
        user.name = name
        user.email = email
        user.password = password
        user.condominio = condominio
        user.save()

        return redirect('/view_admin/')
      

def delete_owner(request):
  if request.method == 'GET':
    owner=Users.objects.all()
    context = {'usuarios': owner}
    
    return render(request, 'delete_owner.html', context)
  else:
    user_id = request.POST['user']
    
    user = get_object_or_404(Users, pk=user_id)
    user.delete()
    
    
    return redirect('/view_admin/')


def read_employee(request):
  if request.method == 'GET':
    # Recupera todos los empleados de la base de datos
    employees = Empleado.objects.all()
    
    # Prepara el contexto con los empleados
    context = {'empleados': employees}
    
    # Renderiza la plantilla con el contexto
    return render(request, 'read_employee.html', context)


def create_employee(request):
  if request.method == 'GET':
    
    condominios = Condominio.objects.all()
    context = {'condominios': condominios}
    return render(request, 'create_employee.html', context)
  else:
    name = request.POST['name']
    lastname = request.POST['lastname']
    age = request.POST['age']
    gender = request.POST['gender']
    email = request.POST['email']
    charge = request.POST['charge']
    salary = request.POST['salary']
    phone = request.POST['phone']
    condominio = request.POST['condominio']
    
    # Obtener la instancia de Condominio correspondiente al ID proporcionado
    # condominio = get_object_or_404(Condominio, pk=condominio_id)
        
    Empleado.objects.create(name = name, lastname =lastname , age = age, gender = gender, email = email, charge =  charge, salary =  salary, phone_number =  phone, condominio_id = condominio)

    return redirect('/view_admin/')

def update_employee(request):
  if request.method == 'GET':
    empeleado = Empleado.objects.all()
    condominios = Condominio.objects.all()
    context ={'empleados': empeleado, 'condominios':condominios}
    return render(request,'update_employee.html',context)
  else:

        # Obtener los datos actualizados del formulario
        empleado_id = request.POST['empleado']
        name = request.POST['name']
        lastname = request.POST['lastname']
        age = request.POST['age']
        gender = request.POST['gender']
        email = request.POST['email']
        charge = request.POST['charge']
        salary = request.POST['salary']
        phone = request.POST['phone']
        condominio_id = request.POST['condominio']

        condominio = get_object_or_404(Condominio, pk=condominio_id)

        empleado = get_object_or_404(Empleado, pk=empleado_id)
        # Actualizar los campos del empleado
        empleado.name = name
        empleado.lastname = lastname
        empleado.age = age
        empleado.gender = gender
        empleado.email = email
        empleado.charge = charge
        empleado.salary = salary
        empleado.phone_number = phone
        empleado.condominio = condominio
        
        # Guardar los cambios en la base de datos
        empleado.save()
        return redirect('/view_admin/')

def delete_employee(request):
  if request.method == 'GET':
      empleado = Empleado.objects.all()

      # Pasar los datos al contexto de renderizado
      context = {'empleados': empleado}

      return render(request, 'delete_employee.html', context)
  else:
     
     empleado_id = request.POST['empleado']

     empleado = get_object_or_404(Empleado, pk=empleado_id)

      # Eliminar el condominio
     empleado.delete()
     
     return redirect('/view_admin/')


def view_edificio(request):
   if request.method == 'GET':
      
      return redirect('/view_edificio/')




# vista del usuario común
def user(request):
  return render(request,'view_user.html')

