# Generated by Django 3.0.2 on 2020-01-16 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20200116_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='establishment',
            name='logo',
            field=models.ImageField(upload_to='logos', verbose_name='Логотип заведения'),
        ),
    ]
