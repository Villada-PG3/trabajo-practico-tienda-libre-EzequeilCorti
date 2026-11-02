from django import forms


class ContactoForm(forms.Form):
    nombre = forms.CharField(
        max_length=100,
        label="Nombre completo",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingresá tu nombre'
        })
    )
    email = forms.EmailField(
        label="Correo electrónico",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'ejemplo@correo.com'
        })
    )
    asunto = forms.CharField(
        max_length=150,
        label="Asunto",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Motivo de tu mensaje'
        })
    )
    mensaje = forms.CharField(
        label="Mensaje",
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Escribí tu mensaje aquí...'
        })
    )
    telefono = forms.CharField(
        required=False,
        max_length=20,
        label="Teléfono (Opcional)",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '11-1234-5678'
        })
    )