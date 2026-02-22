import random
import time
from datetime import date, timedelta
from django.core.management.base import BaseCommand
from gestaoTarefas.models import Tarefa
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Cria 100 registros fictícios na base de dados dbGestaoTarefas'

    def handle(self, *args, **kwargs):
        self.stdout.write('Iniciando a criação de dados fictícios...')

        # Listas de dados para sorteio
        projetos = [
            'Implantação ERP', 'Website Institucional', 'App Mobile Vendas', 
            'Auditoria Interna', 'Treinamento Equipe', 'Migração de Servidor',
            'Campanha Marketing Verão', 'Relatório Anual'
        ]
        
        itens_acao = [
            'Levantamento de Requisitos', 'Desenvolvimento Backend', 'Desenvolvimento Frontend',
            'Testes Unitários', 'Reunião de Alinhamento', 'Documentação Técnica',
            'Configuração de Ambiente', 'Homologação', 'Treinamento de Usuários',
            'Deploy em Produção', 'Análise de Riscos', 'Design de Interface'
        ]
        
        nomes_responsaveis = [
            ('ana', 'Ana Silva'), ('bruno', 'Bruno Souza'), 
            ('carlos', 'Carlos Pereira'), ('daniela', 'Daniela Oliveira'), 
            ('eduardo', 'Eduardo Santos'), ('fernanda', 'Fernanda Lima'), 
            ('gabriel', 'Gabriel Costa')
        ]
        
        # Cria ou recupera os objetos User reais
        usuarios_objs = []
        for username, full_name in nomes_responsaveis:
            user, created = User.objects.get_or_create(username=username)
            if created:
                user.first_name = full_name.split()[0]
                user.last_name = " ".join(full_name.split()[1:])
                user.email = f"{username}@exemplo.com"
                user.save()
            usuarios_objs.append(user)
        
        status_opcoes = ['No prazo', 'Atrasada', 'Concluída', 'Cancelada']

        contador = 0

        # Loop para criar 100 registros
        for _ in range(100):
            # Escolhe um projeto aleatório
            projeto_selecionado = random.choice(projetos)
            
            # Gera datas coerentes
            dias_atras = random.randint(0, 60)
            data_distribuicao = date.today() - timedelta(days=dias_atras)
            prazo = data_distribuicao + timedelta(days=random.randint(5, 30))

            tarefa = Tarefa(
                tarefa=projeto_selecionado,
                itemTarefa=random.choice(itens_acao),
                responsavel=random.choice(usuarios_objs),
                dataDistribuicaoTarefa=data_distribuicao,
                prazoRealizacaoTarefa=prazo,
                observacoes=f"Observação automática gerada para o projeto {projeto_selecionado}.",
                statusTarefa=random.choice(status_opcoes)
            )
            
            tarefa.save()
            contador += 1
            
            # Pequena pausa para garantir que o ID (baseado em milissegundos) seja único
            time.sleep(0.01)

            if contador % 10 == 0:
                self.stdout.write(f'{contador} tarefas criadas...')

        self.stdout.write(self.style.SUCCESS(f'Sucesso! {contador} registros foram criados.'))