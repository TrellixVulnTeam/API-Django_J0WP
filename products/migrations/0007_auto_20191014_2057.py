# Generated by Django 2.2.6 on 2019-10-14 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_branch_products_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch_products',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.branch'),
        ),
    ]
