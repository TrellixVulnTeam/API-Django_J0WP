# Generated by Django 3.0 on 2020-04-10 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_auto_20200406_0416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='QR_code',
            field=models.CharField(default=None, max_length=233),
        ),
    ]
