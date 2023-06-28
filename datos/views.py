from django.shortcuts import render
from .models import (Usuario, Educacion, Habilidad,Lenguaje, 
                     Experiencia, Conocimiento, Certificado,
                     Trabajo, Acerca, Portafolio)
from django.conf import settings
from django.contrib import messages
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
# Create your views here.

def enviar_email(nombre, asunto, mensaje,correo):
    context={'nombre':nombre,
             'asunto':asunto,
             'mensaje':mensaje,
             'correo':correo}
    template= get_template('correo.html')
    content = template.render(context)
    correo = EmailMultiAlternatives(
        'Un correo de prueba',     
        settings.EMAIL_HOST_USER,
        [nombre,asunto,mensaje,correo]
    )
    correo.attach_alternative(content,'text/html')
    correo.send()
    

def index(request):
    usuario = Usuario.objects.all()
    educacion=  Educacion.objects.all() 
    habilidad= Habilidad.objects.all() 
    lenguaje = Lenguaje.objects.all()
    experiencia = Experiencia.objects.order_by('epoca')
    conocimiento = Conocimiento.objects.all()
    certificado = Certificado.objects.all()
    servicios = Trabajo.objects.all()
    trabajo0= servicios[0]
    trabajo1= servicios[1]  
    trabajo2= servicios[2]
    trabajo3= servicios[3]  
   
    acerca = Acerca.objects.all()
    portafolio = Portafolio.objects.all()
    if request.method == "POST":
        correo= settings.EMAIL_HOST_USER
        nombre = request.POST.get('nombre')  
        asunto = request.POST.get('asunto')  
        mensaje = request.POST.get('mensaje')
     
        enviar_email(nombre,asunto,mensaje,correo)
        messages.success(request, 'Mensaje enviado')

    
    return render(request, 'index.html', {'usuarios': usuario,
                                          'educaciones':educacion,
                                          'habilidades':habilidad,
                                          'lenguajes':lenguaje,
                                          'experiencias':experiencia,
                                          'conocimientos':conocimiento,
                                          'certificados':certificado,
                                          'trabajo0':trabajo0,                                    
                                          'trabajo1':trabajo1,                                                                     
                                          'trabajo2':trabajo2,                                    
                                          'trabajo3':trabajo3,                                                                     
                                          'acercas':acerca,
                                          'portafolios':portafolio})

 
    
    




