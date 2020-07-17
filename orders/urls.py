from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:item_details>", views.get_item, name = 'get_item')
]
