from django.shortcuts import render
from django.db.models import Case, When, Value, IntegerField
from .models import Tarefa

# Create your views here.
def index(request):
    # Definimos a ordem personalizada dos status
    tarefas = Tarefa.objects.annotate(
        prioridade_status=Case(
            When(statusTarefa='Atrasada', then=Value(1)),
            When(statusTarefa='No prazo', then=Value(2)),
            When(statusTarefa='Concluída', then=Value(3)),
            When(statusTarefa='Cancelada', then=Value(4)),
            default=Value(5),
            output_field=IntegerField(),
        )
    ).order_by('tarefa', 'prioridade_status', 'prazoRealizacaoTarefa')
    
    return render(request, 'gestaoTarefas/index.html', {'tarefas': tarefas})