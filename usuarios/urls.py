from django.urls import path
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from . import views

urlpatterns = [
    path('', views.cadastro, name='cadastro'),  # Cadastro como página inicial
    path('login/', views.login, name='login'),
    path('task_list/', views.task_list, name='task_list'),
    path('task_create/', views.task_create, name='task_create'),
    path('task_update/<int:pk>/', views.task_update, name='task_update'), 
    path('task_delete/<int:pk>/', views.task_delete, name='task_delete'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout, name='logout'),
]
