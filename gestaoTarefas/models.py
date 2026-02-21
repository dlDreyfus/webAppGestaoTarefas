from django.db import models
from datetime import datetime

def gerar_id_tarefa():
    """
    Gera um ID numérico baseado no timestamp atual.
    Formato: YYYYMMDDHHMMSSmmm (17 dígitos)
    """
    return int(datetime.now().strftime('%Y%m%d%H%M%S%f')[:-3])

class Tarefa(models.Model):
    STATUS_CHOICES = [
        ('No prazo', 'No prazo'),
        ('Atrasada', 'Atrasada'),
        ('Concluída', 'Concluída'),
        ('Cancelada', 'Cancelada'),
    ]

    # idTarefa: autoincremental (gerado automaticamente), formato data/hora/ms
    idTarefa = models.BigIntegerField(
        primary_key=True, 
        default=gerar_id_tarefa, 
        editable=False, 
        verbose_name="ID da Tarefa"
    )
    
    tarefa = models.CharField(max_length=255, verbose_name="Nome da Tarefa")
    itemTarefa = models.CharField(max_length=255, verbose_name="Item da Tarefa")
    responsavelTarefa = models.CharField(max_length=255, verbose_name="Responsável")
    dataDistribuicaoTarefa = models.DateField(verbose_name="Data de Distribuição")
    prazoRealizacaoTarefa = models.DateField(verbose_name="Prazo de Realização")
    observacoes = models.TextField(blank=True, null=True, verbose_name="Observações")
    statusTarefa = models.CharField(max_length=20, choices=STATUS_CHOICES, default='No prazo', verbose_name="Status")

    def __str__(self):
        return f"{self.tarefa} ({self.statusTarefa})"