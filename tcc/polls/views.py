from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.base import RedirectView, TemplateView

from .models import Usuario, Curso, Medalha, Usuario_Curso, Usuario_Medalha, Curso_Medalha

"""
class ListaMedalhasView(ListView):
    template_name = 'polls/index.html'

    def get_queryset(self):
        return Medalha.objects.order_by('-nome')

    def get_context_data(self, **kwargs):
        context = super(ListaMedalhasView, self).get_context_data(**kwargs)

        context.update({'medalhas': self.get_queryset()[:5]})
        return context

class ListaCursosView(ListView):
    template_name = 'polls/index.html'

    def get_queryset(self):
        return Curso.objects.order_by('-nome')

    def     (self, **kwargs):
        context = super(ListaCursosView, self).get_context_data(**kwargs)

        context.update({'cursos': self.get_queryset()})
        return context
"""

class HomeView(TemplateView):
    template_name = 'polls/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        usuario = Usuario.objects.get(system_user=self.request.user)
        medalhas = Usuario_Medalha.objects.filter(usuario=usuario)
        cursos = Usuario_Curso.objects.filter(usuario=usuario)

        context.update({'usuario': usuario, 'medalhas': medalhas, 'cursos': cursos})
        return context

class HomeRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return '/home'