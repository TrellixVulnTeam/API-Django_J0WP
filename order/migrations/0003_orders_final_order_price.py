# Generated by Django 3.0 on 2020-06-17 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20200613_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='final_order_price',
            field=models.FloatField(default=0.0),
        ),
    ]
