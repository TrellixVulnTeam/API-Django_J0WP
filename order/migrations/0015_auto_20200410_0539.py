# Generated by Django 3.0 on 2020-04-10 03:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0014_auto_20200410_0435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 10, 3, 39, 9, 970493, tzinfo=utc)),
        ),
    ]
