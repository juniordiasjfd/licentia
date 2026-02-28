from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, Sum
from licentia_process.models import Process
from licentia_process.views import ProcessContextMixin
from licentia_resources.models import Projeto, Componente
from django.db.models.functions import Coalesce
from django.db.models import DecimalField, IntegerField


class HomeView(LoginRequiredMixin, ProcessContextMixin, TemplateView):
    login_url = 'users:login'
    model = Process
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # 1. Captura de Filtros
        proj_id = self.request.GET.get('projeto')
        comp_id = self.request.GET.get('componente')
        volume = self.request.GET.get('volume')

        # Queryset Base
        qs = Process.objects.all()

        # Aplicação dos Filtros
        if proj_id:
            qs = qs.filter(projeto_id=proj_id)
        if comp_id:
            qs = qs.filter(componente_id=comp_id)
        if volume:
            qs = qs.filter(volume=volume)

        # 2. Agregações para os 3 Gráficos (Status + Valor)
        context['valor_status_do_processo'] = [
            {
                'status': item['status_do_processo__nome'] or 'Não definido',
                'total_valor': float(item['total_valor']) 
            } 
            for item in qs.values('status_do_processo__nome')
            .annotate(total_valor=Coalesce(Sum('valor_do_processo'), 0, output_field=DecimalField()))
            .order_by('-total_valor')
        ]
        context['valor_status_do_orcamento'] = [
            {
                'status': item['status_do_orcamento__nome'] or 'Não definido',
                'total_valor': float(item['total_valor'])
            }
            for item in qs.values('status_do_orcamento__nome')
            .annotate(total_valor=Coalesce(Sum('valor_do_processo'), 0, output_field=DecimalField()))
            .order_by('-total_valor')
        ]
        context['valor_status_do_orcamento_aprovacao'] = [
            {
                'status': item['status_do_orcamento_aprovacao__nome'] or 'Não definido',
                'total_valor': float(item['total_valor'])
            }
            for item in qs.values('status_do_orcamento_aprovacao__nome')
            .annotate(total_valor=Coalesce(Sum('valor_do_processo'), 0, output_field=DecimalField()))
            .order_by('-total_valor')
        ]



        context['contagem_status_do_processo'] = [
            {
                'status': item['status_do_processo__nome'] or 'Não definido',
                'total_valor': int(item['total_valor']) 
            } 
            for item in qs.values('status_do_processo__nome')
            .annotate(total_valor=Coalesce(Sum(1), 0, output_field=IntegerField()))
            .order_by('-total_valor')
        ]
        context['contagem_status_do_orcamento'] = [
            {
                'status': item['status_do_orcamento_aprovacao__nome'] or 'Não definido',
                'total_valor': float(item['total_valor'])
            }
            for item in qs.values('status_do_orcamento_aprovacao__nome')
            .annotate(total_valor=Coalesce(Sum(1), 0, output_field=IntegerField()))
            .order_by('-total_valor')
        ]
        context['contagem_status_do_orcamento_aprovacao'] = [
            {
                'status': item['status_do_orcamento_aprovacao__nome'] or 'Não definido',
                'total_valor': float(item['total_valor'])
            }
            for item in qs.values('status_do_orcamento_aprovacao__nome')
            .annotate(total_valor=Coalesce(Sum(1), 0, output_field=DecimalField()))
            .order_by('-total_valor')
        ]

        # Listas para os Selects do Filtro
        context['projetos'] = Projeto.objects.all()
        context['componentes'] = Componente.objects.all()
        
        return context