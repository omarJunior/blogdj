from django import forms

from .models import Suscribers

class SuscribersForm(forms.ModelForm):
    class Meta:
        #referencia al modelo donde se guardaran los datos del formulario
        model = Suscribers
        fields = ('email',)
        widgets = {
            'email': forms.EmailInput(
                attrs = {
                    'placeholder' : 'Correo electronico...',
                },
            )
        }
