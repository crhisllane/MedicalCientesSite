from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.site_list, name='site_list'),
    path('<int:id>/delete/',views.delete, name='delete'),
    path('<int:id>/alterar/',views.alterar, name='alterar'),
    path('cadastrar/',views.cadastrar, name='cadastrar'),


    # path('alterar_put<cliente:cliente>/',views.alterar_put, name='alterar_put')

]