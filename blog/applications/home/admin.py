from django.contrib import admin
from .models import Home, Suscribers, Contact

# Register your models here.

class HomeAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'about_title',
        'about_text',
        'email',
        'phone',
    )
    search_fields = ('title',)

class SuscribersAdmin(admin.ModelAdmin):
    list_display = ('email',)
    search_fields = ('email',)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'message',)
    search_fields = ('email',)

admin.site.register(Home, HomeAdmin)
admin.site.register(Suscribers, SuscribersAdmin)
admin.site.register(Contact, ContactAdmin)
