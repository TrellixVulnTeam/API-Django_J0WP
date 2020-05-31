# Generated by Django 3.0 on 2020-04-10 04:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0024_auto_20200410_0539'),
        ('order', '0015_auto_20200410_0539'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_details',
            name='features',
            field=models.ManyToManyField(to='products.features'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 10, 4, 47, 10, 18769, tzinfo=utc)),
        ),
    ]
