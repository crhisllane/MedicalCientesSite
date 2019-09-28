from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.site_list, name='site_list'),
    path('<int:id>/delete/',views.delete, name='delete')
]