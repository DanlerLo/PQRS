from django import forms
from .models import registro

class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'

class registroForm(forms.ModelForm):

    class Meta:
        model = registro
        fields = '__all__'

class productoForm(forms.ModelForm):

    class Meta:
        model = registro
        fields = '__all__'
        widgets={
            "fecha_fabricacion":forms.SelectDateWidget()
        }    