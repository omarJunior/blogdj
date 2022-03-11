from django.contrib import admin

from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'full_name',
        'ocupation',
        'genero',
        'date_birth',
    )

admin.site.register(User, UserAdmin)
