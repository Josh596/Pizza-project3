from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sign_up", views.sign_up, name = 'sign_up'),
    path("login", views.login_view, name = 'login'),
   	path("<str:item_details>", views.get_item, name = 'get_item')
]
	