from site_mc.models import Cliente
from django.shortcuts import render
from django.template import Context, Template
import requests

class cliente():
    id = 1
    nome = "xuxu"
    codigo = "123"
    crm = "XXX"

def site_list(request):
    # context = Context ( {"clientes", [cliente(), cliente()]})
    # clintes =  
    response = requests.get('https://crhisllane.pythonanywhere.com/Clientes/')
    
    context = {'clientes': response.json()}
    
    # context["clientes"] = [cliente(), cliente()]    
    return render(request, 'site_mc/site_list.html', context)

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




