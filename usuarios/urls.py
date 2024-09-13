from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastro, name='cadastro'),  # Cadastro como página inicial
    path('login/', views.login, name='login'),
    path('task_list/', views.task_list, name='task_list'),
    path('task_create/', views.task_create, name='task_create'),
    path('task_update/<int:pk>/', views.task_update, name='task_update'), 
    path('task_delete/<int:pk>/', views.task_delete, name='task_delete'), 
]
