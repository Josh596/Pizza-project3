from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
import json


#Importing my models
from .models import *

# Create your views here.
def index(request):
    context = {
        'menus' : Menu.objects.all()
    }
    return render(request, "orders/layout.html", context)

def get_item(request, item_details):
    #Using ajax requests
    if request.method == 'GET' and request.is_ajax:
        #Getting the menu the item belongs too
        #converting item_details to string from json
        item_details_str = json.loads(item_details)
        menu_name = Menu.objects.get(name = item_details_str['menu_name'])

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
        context_json = serializers.serialize("json", [item_data, *item_price, *add_on])
        

        
        return HttpResponse(context_json, content_type ="application/json")
    else:
        return HttpResponse('unsuccessful')
# Problem with models... item not recognixed orders.models.Items.DoesNotExist: Items matching query does not exist.



