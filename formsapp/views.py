from django.shortcuts import render
from django.forms import modelformset_factory
from .forms import ConsoleForm
from .models import Console

# Create your views here.
def index(request):

    console_form = ConsoleForm()
    ConsoleFormSet = modelformset_factory(Console,fields=('__all__'), extra=3)
    context = {
        'console_form': console_form,
        'console_formset': ConsoleFormSet
    }

    return render(request, "formsapp/index.html", context)