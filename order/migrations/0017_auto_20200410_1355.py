# Generated by Django 3.0 on 2020-04-10 11:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0016_auto_20200410_0647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 10, 11, 55, 7, 37318, tzinfo=utc)),
        ),
    ]
