from django.urls import path
from .views import index, htmx

urlpatterns = [
    path('', index, name='index'),
    path('htmx/',htmx,name='htmx') 
]
