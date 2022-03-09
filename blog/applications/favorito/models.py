from django.db import models
from django.conf import settings
from model_utils.models import TimeStampedModel

from applications.entrada.models import Entry

# Create your models here.
class Favorites(TimeStampedModel):
    "Modelo de favoritos"
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Usuario", blank=True, null=True, on_delete=models.CASCADE)
    entry = models.ForeignKey(Entry, verbose_name="Entrada", blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'entry',)  #Campos para que no se repitan"
        verbose_name = "Entrada Favorita"
        verbose_name_plural = "Entradas favoritas"

    def __str__(self):
        return str(self.entry.title)

