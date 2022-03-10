from django.shortcuts import render

from django.views.generic import ListView
from .models import Category, Tag, Entry

# Create your views here.

class EntryListView(ListView):
    template_name = "entrada/lista.html"
    context_object_name = "entradas"
    paginate_by = 10

    def get_queryset(self):
        kword= self.request.GET.get('kword', '')
        categoria = self.request.GET.get('categoria', '')
        #consulta de busqueda
        resultado = Entry.objects.buscar_entrada()
        print(resultado)
        return resultado
