from django.contrib import admin
from .models import (Usuario, Lenguaje, Habilidad, Experiencia, Conocimiento,
                     Educacion, Certificado, Acerca, Portafolio)
admin.site.site_header="CURRICULUM ADMIN"
admin.site.site_title="Portal del Curriculum"
admin.site.index_title="Bienvenidos al portal de administracion"
# Register your models here.
class PortafolioAdmin(admin.ModelAdmin):
    list_display = ('portafolio','imagen','tipo','estado')
    list_filter = ('portafolio','imagen','tipo','estado')
    search_fields = ('portafolio','imagen','tipo','estado')
    ordering = ('portafolio','imagen','tipo','estado')
    list_editable =('estado',)
    list_per_page = 10

admin.site.register(Portafolio, PortafolioAdmin)

class AcercaAdmin(admin.ModelAdmin):
    list_display = ('acerca','estado')
    list_filter = ('acerca','estado')
    search_fields = ('acerca','estado')
    ordering = ('acerca','estado')
    list_editable =('estado',)
    list_per_page = 10

admin.site.register(Acerca, AcercaAdmin)

# class TrabajoAdmin(admin.ModelAdmin):
#     list_display = ('trabajo','descripcion','icono','estado')
#     list_filter = ('trabajo','descripcion','icono','estado')
#     search_fields = ('trabajo','descripcion','icono','estado')
#     ordering = ('trabajo','descripcion','icono','estado')
#     list_editable =('estado',)
#     list_per_page = 10

# admin.site.register(Trabajo, TrabajoAdmin)

class CertificadoAdmin(admin.ModelAdmin):
    list_display = ('certificado','epoca','imagen','descripcion','estado')
    list_filter = ('certificado','epoca','imagen','descripcion','estado')
    search_fields = ('certificado','epoca','imagen','descripcion','estado')
    ordering = ('certificado','epoca','imagen','descripcion','estado')
    list_editable =('estado',)
    list_per_page = 10

admin.site.register(Certificado, CertificadoAdmin)

class ConocimientoAdmin(admin.ModelAdmin):
    list_display = ('conocimiento','estado')
    list_filter = ('conocimiento','estado')
    search_fields = ('conocimiento','estado')
    ordering = ('conocimiento','estado')
    list_editable =('estado',)
    list_per_page = 10

admin.site.register(Conocimiento, ConocimientoAdmin)

class EducacionAdmin(admin.ModelAdmin):
    list_display = ('educacion','descripcion','estado')
    list_filter = ('educacion','descripcion','estado')
    search_fields = ('educacion','descripcion','estado')
    ordering = ('educacion','descripcion','estado')
    list_editable =('estado',)
    list_per_page = 10

admin.site.register(Educacion, EducacionAdmin)

class ExperienciaAdmin(admin.ModelAdmin):
    list_display = ('cargo','lugar','epoca','descripcion','estado')
    list_filter = ('cargo','lugar','epoca','descripcion','estado')
    search_fields = ('cargo','lugar','epoca','descripcion','estado')
    ordering = ('cargo','lugar','epoca','descripcion','estado')
    list_editable =('estado',)
    list_per_page = 10

admin.site.register(Experiencia, ExperienciaAdmin)

class HabilidadAdmin(admin.ModelAdmin):
    list_display = ('habilidad','nivel','estado')
    list_filter = ('habilidad','nivel','estado')
    search_fields = ('habilidad','nivel','estado')
    ordering = ('habilidad','nivel','estado')
    list_editable =('estado',)
    list_per_page = 10

admin.site.register(Habilidad, HabilidadAdmin)

class LenguajeAdmin(admin.ModelAdmin):
    list_display = ('lenguaje','nivel','estado')
    list_filter = ('lenguaje','nivel','estado')
    search_fields = ('lenguaje','nivel','estado')
    ordering = ('lenguaje','nivel','estado')
    list_editable =('estado',)
    list_per_page = 10

admin.site.register(Lenguaje, LenguajeAdmin)


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'telefono', 'estado')
    list_filter = ('nombre', 'correo', 'telefono', 'estado')
    search_fields = ('nombre', 'correo', 'telefono', 'estado')
    ordering = ('nombre', 'correo', 'telefono', 'estado')
    list_editable =('estado',)
    list_per_page = 10

admin.site.register(Usuario, UsuarioAdmin)

