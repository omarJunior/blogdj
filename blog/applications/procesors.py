from applications.home.models import Home

#Context Procesors para recuperar telefono y email del registro home
def home_contact(request):
    home = Home.objects.latest('created')
    return {
        'telefono': home.phone,
        'correo': home.email
    }
