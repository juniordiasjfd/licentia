# licentia_resources/forms.py
from django import forms

class BaseResourceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            # Adiciona a classe do Tabler em todos os inputs
            field.widget.attrs['class'] = 'form-control'