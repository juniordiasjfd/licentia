from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Futuramente, buscaremos dados reais aqui
        context['stats'] = {
            'usuarios': 12, # Exemplo estático para teste visual
            'recursos_pendentes': 45,
        }
        return context