from django.contrib import admin
from .models import Category, Tag, Entry

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('short_name', 'name',)
    search_fields = ('short_name',)

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class EntryAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'category',
        'nombres_tag',
        'title',
        'resume',
        'content',
        'public',
        'image',
        'portada',
        'in_home',
    )
    search_fields = ('user', 'category',)
    
    #metodo en el admin
    def nombres_tag(self, obj):
        name = ""
        if obj.tag:
            for i in obj.tag.all():
                name = name + " " + i.name
            return name
        return ""

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Entry, EntryAdmin)

