from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models


# Create your models here.
class Menu(models.Model):
	name = models.CharField(max_length = 64)

	def __str__(self):
		return f"{self.name}"


class Items(models.Model):
	menu = models.ForeignKey(Menu, on_delete = models.CASCADE, related_name='item')
	name = models.CharField(max_length = 64)

	def __str__(self):
		return f"{self.menu} - {self.name}"

class Add_ons(models.Model):
	item = models.ForeignKey(Items, on_delete = models.CASCADE, null = True, related_name = 'add_on')
	name = models.CharField(max_length = 64)
	price = models.DecimalField(max_digits=3, decimal_places=2)

	def __str__(self):
		return f"{self.name} is ${self.price} ({self.item})"

class Toppings(models.Model):
	menu = models.ForeignKey(Menu, on_delete = models.CASCADE, null = True, related_name = 'topping')
	name = models.CharField(max_length = 64)
	

	def __str__(self):
		return f"{self.name}"

class Size(models.Model):
	size = models.CharField(max_length = 10)

	def __str__(self):
		return  f"{self.size}"


class Item_price(models.Model):
	item = models.ForeignKey(Items, on_delete = models.CASCADE, related_name='price')
	price = models.DecimalField(max_digits=4, decimal_places=2)
	size = models.ForeignKey(Size, on_delete = models.CASCADE, null = True, blank = True, related_name='item_size')

	def __str__(self):
		return f"{self.item}({self.size}) is ${self.price}"


class Order(models.Model):
	item = models.ManyToManyField(Item_price, related_name = 'items')
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name='user_orders')
	price = models.DecimalField(max_digits = 4, decimal_places =2)

	def __str__(self):
		return f"{self.user}- ${self.price}"



