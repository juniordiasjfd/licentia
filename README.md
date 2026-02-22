# Licentia 🏛️

Sistema de gestão de ativos editoriais e controle de processos de licenciamento.

## 🚀 Tecnologias
- **Framework:** Django 5.x
- **UI:** Tabler (Bootstrap 5)
- **Ícones:** Font Awesome 6
- **Ambiente:** Python 3.11+

## 🛠️ Instalação
1. Clone o repositório: `git clone ...`
2. Crie o ambiente virtual: `python -m venv .venv`
3. Ative o venv:
   - Windows: `.venv\Scripts\activate`
   - Linux/Mac: `source .venv/bin/activate`
4. Instale as dependências: `pip install -r requirements.txt`
5. Execute as migrações: `python manage.py migrate`

## 🔐 Níveis de Acesso
O sistema utiliza Mixins customizados para garantir a hierarquia:
- **Coordenador:** Gestão total e ativação de usuários.
- **Comum Interno:** Acesso a processos e recursos editoriais.
- **Comum Externo:** Acesso restrito a prestadores de serviços.

## 🎨 Identidade Visual
O projeto utiliza a cor **Teal** (#0ca678) como base, aplicada via variáveis CSS do Tabler.