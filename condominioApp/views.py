from django.utils import timezone
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
        users = Users.objects.filter(email=email, password=password)

        # Acceso a la vista del usuario admin
        for admin in admins:
            if admin.acess.access == "Administrador":
                request.session['user_type'] = 'admin'  # Guardar el tipo de usuario en la sesión
                return redirect('view_admin/')
        
        # Acceso a la vista del usuario común
        for user in users:
          if user.acess.access == "Propietario":
              request.session['user'] = {
                  'id': user.id,
                  'name': user.name,
                  'email': user.email,
                  # Agrega cualquier otro atributo que desees incluir en la sesión
              }
          request.session['user_type'] = 'user'  # Guardar el tipo de usuario en la sesión
          return redirect('view_user/')
        return render(request, 'login.html', {'error_message': 'Credenciales inválidas'})  # Pasar un mensaje de error a la vista

  
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
        acess_id = request.POST['acceso']

        Users.objects.create(name=name, email=email,password = password  ,acess_id=acess_id)
        
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

        # Actualizar el usuario seleccionado usando su ID
        user = Users.objects.get(pk=id_user)
        user.name = name
        user.email = email
        user.password = password
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
    # Recupera todos los edificios de la base de datos
    edificios = Edificios.objects.all()
    
    # Prepara el contexto con los edificios
    context = {'edificios': edificios}
    
    # Renderiza la plantilla con el contexto
    return render(request, 'view_edificio.html', context)


def create_edificio(request):
  if request.method == 'GET':
    
    condominios = Condominio.objects.all()
    context = {'condominios': condominios}
    return render(request, 'create_edificio.html', context)
  else:
    condominio = request.POST['condominio']
    bloque = request.POST['bloque']
    year_construction = request.POST['year_construction']
    # Obtener la instancia de Condominio correspondiente al ID proporcionado
    # condominio = get_object_or_404(Condominio, pk=condominio_id)
        
    Edificios.objects.create(condominio_id = condominio , bloque = bloque, year_construction= year_construction)

    return redirect('/view_admin/read_condominium/')


def update_edificio(request):
  if request.method == 'GET':
    edificio = Edificios.objects.all()
    condominios = Condominio.objects.all()
    context ={'edificios': edificio, 'condominios':condominios}
    return render(request,'update_edificio.html',context)
  else:

        # Obtener los datos actualizados del formulario
        edificio_id = request.POST['edificio']
        bloque = request.POST['bloque']
        year_construction = request.POST['year_construction']
        

        edificio = get_object_or_404(Edificios, pk=edificio_id)
        # Actualizar los campos del empleado
        edificio.bloque = bloque
        edificio.year_construction = year_construction     
        # Guardar los cambios en la base de datos
        edificio.save()
        return redirect('/view_admin/read_condominium/')


def delete_edificio(request):
  if request.method == 'GET':
      edificio = Edificios.objects.all()
      # Pasar los datos al contexto de renderizado
      context = {'edificios': edificio}
      return render(request, 'delete_edificio.html', context)
  else:
     edificio_id = request.POST['edificio']
     edificio = get_object_or_404(Edificios, pk=edificio_id)
      # Eliminar el condominio
     edificio.delete()
     return redirect('/view_admin/read_condominium/')

def read_departamento(request):
    # Obtener todos los departamentos
    departamentos = Departamentos.objects.all()
    departamento_user = Departamento_user.objects.all()

    # Pasar los datos al template
    context = {'departamentos': departamentos, 'departamentos_user': departamento_user}
    return render(request, 'read_departamento.html', context)

def create_departamento(request):
    if request.method == 'GET':
        edificios = Edificios.objects.all() 
        context = {'edificios': edificios}
        return render(request, 'create_departamento.html', context)
    else:
        edificios = request.POST['edificio']
        nro_dpto = request.POST['nro_dpto']
        telefono_casa = request.POST['telefono_casa']
        status = request.POST['status']

        Departamentos.objects.create(edificios_id=edificios, nro_dpto=nro_dpto, telefono_casa=telefono_casa, status=status)
        return redirect('read_departamento')


def update_departamento(request):
    if request.method == 'GET':
      departamentos = Departamentos.objects.all()
      users = Users.objects.all()
      context = {'departamentos': departamentos, 'users': users}
      return render(request, 'update_departamento.html', context)
    
    if request.method == 'POST':
        departamento_id = request.POST['departamento']
        departamento = Departamentos.objects.get(pk=departamento_id)
        departamento.nro_dpto = request.POST['nro_dpto']
        departamento.telefono_casa = request.POST['telefono_casa']

        status = request.POST['status']
        if status == 'false':
            departamento.status = False
            departamento_user = Departamento_user.objects.filter(departamento=departamento).first()
            if departamento_user:
                departamento_user.delete()
        else:
            departamento.status = True
            user_id = int(status)
            user = Users.objects.get(pk=user_id)
            fecha_compra = timezone.now()
            departamento_user = Departamento_user(departamento=departamento, users=user, fecha_compra=fecha_compra)
            departamento_user.save()

        departamento.save()
        return redirect('read_departamento')  

def delete_departamento(request):
    if request.method == 'GET':
        departamentos = Departamentos.objects.all()
        # Pasar los datos al contexto de renderizado
        context = {'departamentos': departamentos}
        return render(request, 'delete_departamento.html', context)
    else:
        departamento_id = request.POST['departamento']
        departamento = get_object_or_404(Departamentos, pk=departamento_id)
        # Eliminar el departamento
        departamento.delete()
        return redirect('read_departamento')


def user(request):
    try:
        user = request.session['user']  # Obtener el usuario de la sesión
        departamentos_usuario = Departamento_user.objects.filter(users=user['id'])  # Filtrar los departamentos del usuario por su ID

        # Crear una lista para almacenar los pagos asociados a cada condominio
        pagos_condominio = []

        # Iterar sobre los departamentos del usuario
        for departamento in departamentos_usuario:
            condominio_id = departamento.departamento.edificios.condominio.id

            # Filtrar los pagos asociados al condominio actual
            pagos = Mantenimiento.objects.filter(condominio_id=condominio_id)

            # Agregar los pagos asociados al condominio a la lista de pagos_condominio
            pagos_condominio.append({'condominio': departamento.departamento.edificios.condominio, 'pagos': pagos})

        context = {'user_info': user, 'departamentos_usuario': departamentos_usuario, 'pagos_condominio': pagos_condominio, 'session_present': True}
        return render(request, 'view_user.html', context)
    except KeyError:
        # Si no se encuentra la sesión del usuario, pasar la variable de contexto como False
        context = {'session_present': False}
        return render(request, 'view_user.html', context)

def procesar_pagos(request):
    if 'user' in request.session:
      user_id = request.session['user']['id']  # Obtener el ID de usuario de la sesión
      usuario = Users.objects.get(pk=user_id)
      user = request.session['user']
      if request.method == 'POST':
          condominio_id = request.POST.get('condominio')
          monto = request.POST.get('monto')
          descripcion = request.POST.get('descripcion')

          mantenimiento = Mantenimiento(condominio_id=condominio_id, usuario=usuario, monto_pago=monto, descripcion=descripcion)
          mantenimiento.save()

          # Redireccionar a alguna página de éxito o a la misma página
          return redirect('inicio_usuario') 
      else:
        departamentos_usuario = Departamento_user.objects.filter(users=user['id'])
        context = {'user_info': user, 'session_present': True, 'departamentos_usuario': departamentos_usuario }
        return render(request, 'mantenimiento.html', context)
    else:
        context = {'session_present': False}
        return render(request, 'mantenimiento.html', context)
