from records.models import Records
from django.forms import ModelForm, TextInput, Textarea, PasswordInput, DateInput, DateTimeInput, EmailInput, \
    ImageField, forms, FileInput


class RecordForm(ModelForm):
    class Meta:
        model = Records
        fields = ['procedure_name', 'cabinet', 'price', 'is_payed', 'is_cancelled', 'datetime']

        widgets = {
            'procedure_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Процедура',
                'name': 'name',
            }),
            'cabinet': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Кабинет',
                'name': 'cabinet'
            }),
            'price': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена',
                'name': 'price',
                'type': 'number',
            }),
            'datetime': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Время',
                'name': 'datetime',
                'type': "datetime-local",
                'step': "60",
            }, format= "%d/%m/%y %H:%M")
        }
