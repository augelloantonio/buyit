# Generated by Django 2.2.6 on 2019-10-24 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voucher', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voucher',
            name='amount',
        ),
    ]
