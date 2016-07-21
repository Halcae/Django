from django.http import HttpResponse
from django.views.generic.list import ListView

from .models import Usuario, Curso, Medalha, Usuario_Curso, Usuario_Medalha, Curso_Medalha


class ListaMedalhasView(ListView):
    template_name = 'polls/index.html'

    def get_queryset(self):
        return Medalha.objects.order_by('-nome')

    def get_context_data(self, **kwargs):
        context = super(ListaMedalhasView, self).get_context_data(**kwargs)

        context.update({'medalhas': self.get_queryset()[:5]})
        return context


class AvatarUsuario(ListView):
    template_name = 'polls/index.html'

    def get_queryset(self):
        return Usuario.objects.order_by('-nome')

    def get_context_data(self, **kwargs):
        context = super(AvatarUsuario, self).get_context_data(**kwargs)

        context.update({'usuarios': self.get_queryset()[:5]})
        return context