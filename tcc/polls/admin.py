from django.contrib import admin

from .models import Usuario, Curso, Medalha, Usuario_Curso, Usuario_Medalha, Curso_Medalha

admin.site.register(Usuario)
admin.site.register(Curso)
admin.site.register(Medalha)
admin.site.register(Usuario_Curso)
admin.site.register(Usuario_Medalha)
admin.site.register(Curso_Medalha)