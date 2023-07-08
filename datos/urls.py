from django.urls import path
from .views import index, portafolio

urlpatterns = [
    path('', index, name='index'),
    path('portafolio/',portafolio,name='portafolio') 
]
