from django.http import HttpResponse

from .models import Usuario, Curso, Medalha, Usuario_Curso, Usuario_Medalha, Curso_Medalha


def index(request):
    latest_user_list = Medalha.objects.order_by('-nome')[:5]
    output = ', '.join([q.nome for q in latest_user_list])
    return HttpResponse(output)

#Trocando q.nome para q.icone da erro