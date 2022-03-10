import datetime
#
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from django.views.generic import (
    TemplateView,
    CreateView
)

from applications.entrada.models import Entry
from applications.home.models import Home
from .forms import SuscribersForm

class HomePageView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        #cargamos el home
        context['home'] = Home.objects.latest('created')
        #contexto de portada
        context["portada"] = Entry.objects.entrada_en_portada()
        #contexto para los articulos en home
        context['entradas_home'] = Entry.objects.entradas_en_home()
        #contexto para las entradas recientes
        context['entradas_recientes'] = Entry.objects.entradas_recientes()
        #enviamos formulario de subscripcion
        context['form'] = SuscribersForm
        return context


class SuscriberCreateView(CreateView):
    form_class = SuscribersForm
    success_url = reverse_lazy("home_app:index")