# Generated by Django 3.0.2 on 2020-05-03 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_establishment_menu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='establishment',
            name='menu',
        ),
    ]