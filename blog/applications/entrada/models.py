from django.db import models
from django.conf import settings
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Category(TimeStampedModel):
    "Modelo de categoria"
    short_name = models.CharField(verbose_name="Nombre corto", max_length=15, blank=True, null=True)
    name = models.CharField(verbose_name="Nombre", max_length=30, blank=True, null=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name
    
class Tag(TimeStampedModel):
    "Modelo de etiquetas"
    name = models.CharField(verbose_name="Nombres", max_length=30, blank=True, null=True)

    class Meta:
        verbose_name = "Etiqueta"
        verbose_name_plural = "Tags"
    
    def __str__(self):
        return self.name

class Entry(TimeStampedModel):
    "Modelo de entradas"
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Usuario", blank=True, null=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name="Usuario", blank=True, null=True, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    title = models.CharField(verbose_name="Titulo", max_length=200, blank=True, null=True)
    resume = models.TextField()
    content = RichTextUploadingField(verbose_name="Contenido")
    public = models.BooleanField(default=False)
    image = models.ImageField(verbose_name="Imagen", upload_to = "Entry")
    portada = models.BooleanField(default=False)
    in_home = models.BooleanField(default=False)
    slug = models.SlugField(editable=False, max_length=300)

    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"

    def __str__(self):
        return self.title
    
