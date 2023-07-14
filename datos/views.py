from django.shortcuts import render
from .models import (Usuario, Educacion, Habilidad,Lenguaje, 
                     Experiencia, Conocimiento, Certificado,
                     Acerca, Portafolio, Trabajo)
from django.conf import settings
from django.contrib import messages
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives

from django.http import FileResponse
# Create your views here.
def ver_pdf(request, id):
    certificado = Certificado.objects.get(id=id)
    return FileResponse(certificado.archivo, content_type='application/pdf')



def enviar_email(nombre, asunto, mensaje, correo):
    context={'nombre':nombre,
             'asunto':asunto,
             'mensaje':mensaje,
             'correo':correo
             }
    template= get_template('correo.html')
    content = template.render(context)
    correo = EmailMultiAlternatives(
        'Un correo de mi pagina curriculum', 
        'Curriculum',    
        settings.EMAIL_HOST_USER,
        [nombre, asunto, mensaje, correo]
    )
    correo.attach_alternative(content,'text/html')
    correo.send()
    

def index(request):
    usuario = Usuario.objects.all()
    educacion=  Educacion.objects.order_by('epoca') 
    habilidad= Habilidad.objects.all() 
    lenguaje = Lenguaje.objects.all()
    experiencia = Experiencia.objects.order_by('epoca')
    conocimiento = Conocimiento.objects.all()
    certificado = Certificado.objects.all()   
    acerca = Acerca.objects.all()
    portafolio = Portafolio.objects.all()
    trabajo = Trabajo.objects.all()

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
                                          'acercas':acerca,
                                          'portafolios':portafolio,
                                          'certificados':certificado,
                                          'trabajos':trabajo})


 
    
    




