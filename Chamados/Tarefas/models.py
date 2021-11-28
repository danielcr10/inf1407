from django.db import models

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
    )
    
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    setor = models.CharField(max_length=10, choices=SETOR)
    situacao = models.CharField(
        max_length=5,
        choices=STATUS,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo