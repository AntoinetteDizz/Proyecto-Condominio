from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
  path('', views.index),
  path('view_admin/', views.admin),

  #URL PARA EL CRUD DE CONDOMIOS ===========================================================
  path('view_admin/read_condominium/', views.read_condominium, name='read_condominium'),
  path('view_admin/create_condominium/', views.create_condominium, name='create_condominium'),
  path('view_admin/update_condominium/',views.update_condominium, name='update_condominium'),
  path('view_admin/delete_condominium/',views.delete_condominium, name='delete_condominium'),
  
  
  #==========================================================================================
  path('view_admin/read_condominium/view_edificio/', views.view_edificio, name='view_edificio'),



  #URL PARA EL CRUD DE Propetarios===========================================
  path('view_admin/read_owner/', views.read_owner, name='read_owner'),
  path('view_admin/create_owner/', views.create_owner, name = 'create_owner'),
  path('view_admin/update_owner/', views.update_owner, name = 'update_owner'),
  path('view_admin/delete_owner/', views.delete_owner, name='delete_owner'),
  #============================================================================

  
  #URL PARA EL CRUD DE Empleados====================================================
  path('view_admin/read_employee/', views.read_employee, name = 'read_employee'),
  path('view_admin/create_employee/', views.create_employee, name = 'create_employee'),
  path('view_admin/update_employee/', views.update_employee, name = 'update_employee'),
  path('view_admin/delete_employee/', views.delete_employee, name = 'delete_employee'),
  #====================================================================================


  path('view_user/',views.user)

]

#update_employee