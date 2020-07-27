from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sign_up", views.sign_up, name = 'sign_up'),
    path("login", views.login_view, name = 'login'),
    path('<str:item_details>/', views.get_item, name = 'get_item'),
   	path("order", views.order, name = 'order'),
    path("your_orders", views.user_order, name = 'user_order')
]
