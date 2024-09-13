from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Task(models.Model):
    STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Em andamento', 'Em andamento'),
        ('Concluída', 'Concluída'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='Pendente')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=settings.AUTH_USER_MODEL) # Relaciona cada tarefa a um usuário
    
    def __str__(self): # Método que retorna o título da tarefa
        return self.title