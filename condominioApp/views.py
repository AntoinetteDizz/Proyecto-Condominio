from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


# Vista del login
def index(request):
  return render(request, 'login.html')

# Vista de registro de usuario
def register(request):
  return render(request, 'register.html')