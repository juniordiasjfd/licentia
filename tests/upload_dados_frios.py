# ====================================================================
# 1. CONFIGURAÇÃO MANDATÓRIA DO AMBIENTE DJANGO
# ====================================================================
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'licentia_project.settings')
django.setup()

# ====================================================================
# 2. IMPORTAÇÕES DE MODELOS
# ====================================================================
from licentia_process.models import Process
import pandas as pd

NAO_LISTAR = ['logs', 'id', 'criado_em', 'atualizado_em', 'criado_por', 'atualizado_por']
field_names = [f.name for f in Process._meta.get_fields() if f.name not in NAO_LISTAR]
