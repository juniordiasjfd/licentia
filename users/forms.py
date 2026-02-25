from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Departamento
from django.contrib.auth.models import Group

class RegistroUsuarioForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "first_name", "last_name", "email")
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = False
        if commit:
            user.save()
        return user

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do departamento'}),
        }

class AtivacaoUsuarioForm(forms.ModelForm):
    grupo = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        required=True,
        empty_label="Selecione um nível de acesso",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    departamentos = forms.ModelMultipleChoiceField(
        queryset=Departamento.objects.all(),
        required=False,
        widget=forms.SelectMultiple(attrs={
            'class': 'form-select tom-select', 
            'style': 'height: 150px;' # Altura para facilitar a visualização
        })
    )

    class Meta:
        model = User
        fields = ['empresa', 'departamentos']
        widgets = {
            'empresa': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Editora X'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.instance aqui refere-se ao objeto User sendo editado
        if self.instance and self.instance.pk:
            grupo_atual = self.instance.groups.first()
            if grupo_atual:
                self.initial['grupo'] = grupo_atual