from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.site_list, name='site_list'),
]