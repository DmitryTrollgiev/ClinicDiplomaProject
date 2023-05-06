from clients.models import Clients
from django.forms import ModelForm, TextInput, Textarea, PasswordInput, DateInput, DateTimeInput, EmailInput, \
    ImageField, forms, FileInput


class ClientForm(ModelForm):
    class Meta:
        model = Clients
        fields = ['name', 'sex', 'mail', 'age', 'phone', 'passport_number', 'polis']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ФИО',
                'name': 'name',
            }),
            'sex': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пол',
                'name': 'sex'
            }),
            'mail': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Почта',
                'name': 'mail'
            }),
            'age': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Возраст',
                'name': 'age',
                'type': 'number',
            }),
            'phone': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Телефон',
                'name': 'phone',
                'type': 'number',
            }),
            'passport_number': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Серия и номер паспорта',
                'name': 'passport_number',
            }),
            'polis': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ПОЛИС ОМС',
                'name': 'polis',
                'type': 'number',
            })
        }
