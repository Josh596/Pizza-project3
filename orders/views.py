from django.http import HttpResponse
from django.shortcuts import render


#Importing my models
from .models import *

# Create your views here.
def index(request):
    context = {
        'menus' : Menu.objects.all()
    }
    return render(request, "orders/layout.html", context)

def get_item(request, item_name):
    #Using ajax requests
    if request.method == 'GET':

        item_data = Items.objects.get(name = item_name)
        print(item_data)

        item_price = item_data.price.all()
        print(Item_price)

        add_on = item_data.add_on.all()
        print(add_on)

        context = {
            'item_price': item_price,
            'add_on': add_on
        }
        print(context)
        
        return HttpResponse(context)
    else:
        return HttpResponse('unsuccessful')
# Problem with models... item not recognixed orders.models.Items.DoesNotExist: Items matching query does not exist.



