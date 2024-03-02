from django.urls import path
from . import views

urlpatterns = [
  path('', views.index),
  path('view_admin/', views.admin),
  path('view_admin/create_condominium/', views.create_condominium, name='create_condominium')
]