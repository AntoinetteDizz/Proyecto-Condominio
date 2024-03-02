from django.urls import path
from . import views

urlpatterns = [
  path('', views.index),
  path('view_admin/', views.admin),
  path('create_condominium/', views.create_condominium)
]