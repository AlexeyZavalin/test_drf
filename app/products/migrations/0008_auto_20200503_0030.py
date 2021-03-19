# Generated by Django 3.0.2 on 2020-05-02 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20200118_1859'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='establishmentpayments',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='establishmentpayments',
            name='establishment',
        ),
        migrations.RemoveField(
            model_name='establishmentpayments',
            name='payment_type',
        ),
        migrations.AddField(
            model_name='establishment',
            name='kitchens',
            field=models.ManyToManyField(to='products.Kitchen'),
        ),
        migrations.AddField(
            model_name='establishment',
            name='payment',
            field=models.ManyToManyField(to='products.PaymentType'),
        ),
        migrations.RemoveField(
            model_name='establishment',
            name='category',
        ),
        migrations.AddField(
            model_name='establishment',
            name='category',
            field=models.ManyToManyField(to='products.Category'),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.SmallIntegerField(),
        ),
        migrations.DeleteModel(
            name='EstablishmentKitchens',
        ),
        migrations.DeleteModel(
            name='EstablishmentPayments',
        ),
    ]