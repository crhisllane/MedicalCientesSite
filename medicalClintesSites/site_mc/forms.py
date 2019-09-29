from django import forms
from datetime import datetime

class ClienteForm(forms.Form):
    nome = forms.CharField()
    dataNascimento = forms.DateField(input_formats=['%d-%m-%Y'])
    dataColeta = forms.DateField(input_formats=['%d-%m-%Y'])
    dataEntrega = forms.DateField(input_formats=['%d-%m-%Y'])
    CRM = forms.CharField()