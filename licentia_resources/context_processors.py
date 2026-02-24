from . import models as resources_models
import django.db.models.base as model_base

def recursos_menu(request):
    # Lista apenas as classes de modelo que herdaram de AuditoriaBase (ou que você queira listar)
    modelos = []
    for name, obj in vars(resources_models).items():
        if isinstance(obj, type) and issubclass(obj, resources_models.AuditoriaBase) and obj is not resources_models.AuditoriaBase:
            modelos.append({
                'nome_exibicao': obj._meta.verbose_name_plural.capitalize(),
                'url_name': f'resources:{obj._meta.model_name}_list'
            })
    
    # Ordena alfabeticamente pelo nome de exibição
    modelos.sort(key=lambda x: x['nome_exibicao'])
    
    return {'menu_recursos': modelos}