from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Tarefa(models.Model):

    STATUS = (
        ('doing', 'Pendente'),
        ('done', 'Feito'),
    )

    SETOR = (
        ('manutencao', 'Manutenção'),
        ('ti', 'TI'),
        ('marketing', 'Marketing'),
        ('logistica', 'Logistica'),
        ('rh', 'RH'),

    )
    
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    setor = models.CharField(max_length=10, choices=SETOR)
    situacao = models.CharField(
        max_length=5,
        choices=STATUS,
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo