from django.urls import path
from .views import index, ver_pdf

urlpatterns = [
    path('', index, name='index'),
    path('ver_pdf/<int:id>/', ver_pdf, name='verpdf') 
]
