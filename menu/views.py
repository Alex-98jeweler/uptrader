from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    menus = Menu.objects.all()
    return render(request, "index.html", {'items': menus})

def menu_view(request, pk):
    pass
