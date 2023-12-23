from django import forms
from .models import Inscrito
from .models import Institucion

class InscritoForm(forms.ModelForm):
    class Meta:
        model = Inscrito
        fields = '__all__'
        widgets = {
            'institucion': forms.Select,
        }

class InstitucionForm(forms.ModelForm):
    class Meta:
        model = Institucion
        fields = ['nombre']
