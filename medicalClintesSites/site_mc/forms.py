from django import forms
from datetime import datetime

class ClienteForm(forms.Form):
    nome = forms.CharField(widget=forms.TextInput(attrs={'class' : 'uk-input'}))
    dataNascimento = forms.DateField(label="Data Nascimento",input_formats=['%d-%m-%Y'], widget=forms.DateInput(attrs={'class' : 'uk-input'}))
    dataColeta = forms.DateField(label="Data Coleta",input_formats=['%d-%m-%Y'], widget=forms.DateInput(attrs={'class' : 'uk-input'}))
    dataEntrega = forms.DateField(label="Data Entrega",input_formats=['%d-%m-%Y'], widget=forms.DateInput(attrs={'class' : 'uk-input'}))
    CRM = forms.CharField(label="CRM do médico solicitante",widget=forms.TextInput(attrs={'class' : 'uk-input'}))


