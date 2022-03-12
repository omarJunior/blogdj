from django.db import models
from django.conf import settings
from model_utils.models import TimeStampedModel

from applications.entrada.models import Entry
from .managers import FavoriteManager

# Create your models here.
class Favorites(TimeStampedModel):
    "Modelo de favoritos"
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Usuarios", blank=True, null=True, on_delete=models.CASCADE)
    entry = models.ForeignKey(Entry, verbose_name="Entradas", blank=True, null=True, on_delete=models.CASCADE)

    objects = FavoriteManager()

    class Meta:
        unique_together = ('user', 'entry',)  #Campos para que no se repitan las entradas favoritas a cada usuario"
        verbose_name = "Entrada Favorita"
        verbose_name_plural = "Entradas favoritas"

    def __str__(self):
        return str(self.entry.title)

