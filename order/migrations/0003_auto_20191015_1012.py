# Generated by Django 2.2.6 on 2019-10-15 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20191015_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='total_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
