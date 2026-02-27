from django import forms

class BaseResourceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            # 1. Define a classe base do Tabler
            css_classes = 'form-control'

            if field_name == 'cor':
                css_classes += ' color-selector'
            
            # 2. Verifica se este campo específico tem erros no formulário
            # Usamos self.errors (do formulário) e não field.errors
            if self.errors and field_name in self.errors:
                css_classes += ' is-invalid'
                
            # 3. Atualiza os atributos do widget
            field.widget.attrs.update({'class': css_classes})
        