from .models import Console
from django.forms import ModelForm


class ConsoleForm(ModelForm):
    class Meta:
        model = Console
        fields = '__all__'
