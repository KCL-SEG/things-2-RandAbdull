from .forms import ThingForm
from django.shortcuts import render


def home(request):
    form = ThingForm()
    return render(request, 'home.html', {'form': form})
