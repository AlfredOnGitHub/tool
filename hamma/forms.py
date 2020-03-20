from django import forms
from .models import Usuario

class Registro(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ('username', 'password', 'email',)