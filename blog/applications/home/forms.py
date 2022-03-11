from django import forms

from .models import Suscribers, Contact

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


class ConctactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('__all__')