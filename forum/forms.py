from django import forms
from .models import Mensagem

class FormMensagem(forms.ModelForm):
	class Meta:
		model = Mensagem
		fields = ('nome', 'email','mensagem','data')
