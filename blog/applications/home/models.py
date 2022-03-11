from django.db import models
from model_utils.models import TimeStampedModel

# Create your models here.
class Home(TimeStampedModel):
    "Modelo de pagina principal"
    title = models.CharField(verbose_name="Titulo", max_length=50, null=True, blank=True)
    description = models.TextField()
    about_title = models.CharField(verbose_name="Titulo nosotros", max_length=50, null=True, blank=True)
    about_text = models.TextField()
    email = models.EmailField(verbose_name="Email de contacto", unique=True, blank=True, null=True)
    phone = models.CharField(verbose_name="Telefono de contacto", max_length=20, null=True, blank=True)

    class Meta:
        verbose_name = "Pagina principal"
        verbose_name_plural = "Pagina principal"

    def __str__(self):
        return self.title

class Suscribers(TimeStampedModel):
    "Modelo para suscriptores"
    email = models.EmailField(verbose_name="Email de contacto", unique=True, blank=True, null=True)

    class Meta:
        verbose_name = "Suscriptor"
        verbose_name_plural = "Suscriptores"

    def __str__(self):
        return self.email

class Contact(TimeStampedModel):
    "Modelo para contacto"
    full_name = models.CharField(verbose_name="Nombres", max_length=60)
    email = models.EmailField(verbose_name="Email de contacto")
    message = models.TextField(verbose_name="Mensaje")

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"

    def __str__(self):
        return self.full_name