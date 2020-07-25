from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from django.core import serializers
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import json
#Importing my models
from .models import *

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        context = {
            'menus' : Menu.objects.all()
        }
        return render(request, "orders/layout.html", context)
    return render(request, "orders/login.html")

def sign_up(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.create_user(username = username, password = password)
        user.save()
        
        return HttpResponseRedirect(reverse(login_view))
    else:
        return render(request, "orders/register.html")

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            request.session['username'] = username
            return HttpResponseRedirect(reverse(index))
        else:
            return render(request, "orders/register.html")
    else:
        return render(request, "orders/login.html")
#Making menu_name and item_data a global variable

def get_item(request, item_details):
    #Using ajax requests
    if request.method == 'GET' and request.is_ajax:

        #Getting the menu the item belongs too
        #converting item_details to string from json
        item_details_str = json.loads(item_details)
        menu_name = Menu.objects.get(name = item_details_str['menu_name'])

        topping = menu_name.topping.all()


        item_data = menu_name.item.get(name = item_details_str['item_name'])
        print(item_data)


        item_price = item_data.price.all()
        print(Item_price)

        add_on = item_data.add_on.all()
        print(add_on)

        size = item_data.price.all()

        context = {
            'item_price': item_price,
            'add_on': add_on
        }
        print(context)
        context_json = serializers.serialize("json", [item_data, *item_price, *add_on, *topping])
          
        return HttpResponse(context_json, content_type ="application/json")
  
    return Http404("Page not found")
    

def order(request):
    if request.method == 'POST':
        size = request.POST['size']
        toppings = request.POST.getlist('toppings', None)
        item_id = request.POST['item_id']
        menu_id = request.POST['menu_id']

        menu = Menu.objects.get(pk = menu_id)
        item_size = Size.objects.get(size = size)
        size_id = item_size.pk
        item = menu.item.get(pk = item_id)
       

        item_price = item.price.get(size = size_id)
        main_price = item_price.price
        price = 0
        for topping in toppings:
          price += 0.5
        
       
        
        
        return HttpResponse(main_price)
      
    


    else:
        return Http404("Page does not exist")





