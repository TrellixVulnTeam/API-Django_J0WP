# Generated by Django 2.2.6 on 2019-10-14 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20191014_2059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='branch',
            old_name='name',
            new_name='QR_code',
        ),
    ]
