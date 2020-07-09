from django.http import HttpResponse
from django.shortcuts import render
from .models import *

#Importing my models
from .models import *

# Create your views here.
def index(request):
    context = {
        'menus' : Menu.objects.all()
    }
    return render(request, "orders/layout.html", context)


