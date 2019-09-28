from site_mc.models import Cliente
from django.shortcuts import render
from django.template import Context, Template

class cliente():
    id = 1
    nome = "xuxu"
    codigo = "123"
    crm = "XXX"

def site_list(request):
    # context = Context ( {"clientes", [cliente(), cliente()]})
    context = {'clientes': [cliente(), cliente()]}
    # clintes =  
    
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




