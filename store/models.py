from django.db import models
# Create your models here.

class ConsoleModel(models.Model):
    nome = models.CharField(max_length=100)
    ano = models.DateField(auto_now_add=True)
    ESTADOS = {
        'N':'Novo',
        'U':'Usado'
    }
    estado = models.CharField(max_length=1, choices=ESTADOS)
    preço = models.CharField(max_length=10)
    descrição = models.TextField(null = True, blank = True)
    
    def __str__(self):
        return self.nome