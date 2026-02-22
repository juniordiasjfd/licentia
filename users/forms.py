from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
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

class AtivacaoUsuarioForm(forms.ModelForm):
    grupo = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        required=True,
        empty_label="Selecione um nível de acesso",
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = User
        fields = ['empresa', 'departamento']
        widgets = {
            'empresa': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Editora X'}),
            'departamento': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Editorial'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.instance aqui refere-se ao objeto User sendo editado
        if self.instance and self.instance.pk:
            grupo_atual = self.instance.groups.first()
            if grupo_atual:
                self.initial['grupo'] = grupo_atual