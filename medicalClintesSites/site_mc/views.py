from site_mc.models import Cliente
from django.shortcuts import render
from django.template import Context, Template
from site_mc.forms import ClienteForm
import requests

class cliente():
    nome = ""
    dataNascimento = ""
    dataColeta = ""
    dataEntrega = ""
    codigoIdentificador = ""
    CRM = ""

def site_list(request):
    # context = Context ( {"clientes", [cliente(), cliente()]})
    # clintes =  
    response = requests.get('https://crhisllane.pythonanywhere.com/Clientes/')
    
    context = {'clientes': response.json()}
    
    # context["clientes"] = [cliente(), cliente()]    
    return render(request, 'site_mc/site_list.html', context)

def delete(request, id):

    delete = requests.delete('https://crhisllane.pythonanywhere.com/Clientes/' + str(id)) 
    print(delete.ok)

    consulta = requests.get('https://crhisllane.pythonanywhere.com/Clientes/')
    context = {'clientes': consulta.json()}

    return render(request, 'site_mc/site_list.html', context)
    print( "chegou aqui")

def alterar(request, id):
    consulta = requests.get('https://crhisllane.pythonanywhere.com/Clientes/'+ str(id))

    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            dataNascimento = form.cleaned_data['dataNascimento'].strftime("%d-%m-%Y")
            dataColeta = form.cleaned_data['dataColeta'].strftime("%d-%m-%Y")
            dataEntrega = form.cleaned_data['dataEntrega'].strftime("%d-%m-%Y")
            codigoIdentificador = form.cleaned_data['codigoIdentificador']
            CRM = form.cleaned_data['CRM']
            
            resposta = requests.put(f'https://crhisllane.pythonanywhere.com/Clientes/{id}/', data= {
                "nome": nome,
                "dataNascimento": dataNascimento,
                "dataColeta": dataColeta,
                "dataEntrega": dataEntrega,
                "codigoIdentificador": codigoIdentificador,
                "CRM": CRM,
            })
            
    return render(request, 'site_mc/site_alterar.html', {context})

def alterar_put(request, cliente):
    print("#########################")
    print(cliente.nomes)

'''
class ClienteViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = ClienteSerializer
    filter_fields = ('id', 'nome', 'dataNascimento','dataColeta', 'dataEntrega', 'statusEntrega', 'codigoIdentificador')
    lookup_field = 'codigoIdentificador'

    def get_queryset(self):
        return Cliente.objects.all()
'''




