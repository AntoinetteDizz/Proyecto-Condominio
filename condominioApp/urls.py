from django.urls import path
from . import views

urlpatterns = [
  path('', views.index),
  path('view_admin/', views.admin),
  path('view_admin/create_condominium/', views.create_condominium, name='create_condominium'),
  path('view_admin/update_condominium/',views.update_condominium, name='update_condominium'),
  path('view_admin/create_owner/', views.create_owner, name = 'create_owner'),
  path('view_admin/update_owner/', views.update_owner, name = 'update_owner'),
  path('view_admin/create_employee/', views.create_employee, name = 'create_employee')
  
]