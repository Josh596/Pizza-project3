# Generated by Django 3.0.7 on 2020-07-12 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20200708_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_ons',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='add_on', to='orders.Items'),
        ),
        migrations.AlterField(
            model_name='toppings',
            name='menu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='topping', to='orders.Menu'),
        ),
    ]
