from django import forms
from django.contrib.auth import authenticate
#
from .models import User

class UserRegisterForm(forms.ModelForm):

    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña'
            }
        )
    )
    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Repetir Contraseña'
            }
        )
    )

    class Meta:
        """Meta definition for Userform."""

        model = User
        fields = (
            'email',
            'full_name',
            'ocupation',
            'genero',
            'date_birth',
        )
        #personalizacion a campos del modelo
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'placeholder': "Correo electronico..."
                }
            ),
            'full_name': forms.TextInput(
                attrs={
                    'placeholder': "Nombres completo..."
                }
            ),
            'ocupation': forms.TextInput(
                attrs={
                    'placeholder': "Ocupacion..."
                }
            ),
            'date_birth': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            ),
            
        }
    
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Las contraseñas no son iguales')


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'email',
            'full_name',
            'ocupation',
            'genero',
            'date_birth',
        )
        #personalizacion a campos del modelo
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'placeholder': "Correo electronico..."
                }
            ),
            'full_name': forms.TextInput(
                attrs={
                    'placeholder': "Nombres completo..."
                }
            ),
            'ocupation': forms.TextInput(
                attrs={
                    'placeholder': "Ocupacion..."
                }
            ),
            'date_birth': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            ),
            
        }

class LoginForm(forms.Form):
    email = forms.CharField(
        label='E-mail',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Ingrese su correo...',
            }
        )
    )
    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Ingrese su contraseña...'
            }
        )
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        if not authenticate(email=email, password=password):
            raise forms.ValidationError('Los datos de usuario no son correctos')
        
        return self.cleaned_data


class UpdatePasswordForm(forms.Form):

    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña Actual'
            }
        )
    )
    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña Nueva'
            }
        )
    )