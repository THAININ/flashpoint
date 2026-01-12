from django import forms
from .models import ConsoleModel

class ConsoleForm(forms.ModelForm):
    class Meta:
        model = ConsoleModel
        fields = ['nome', 'estado','preço', 'descrição']