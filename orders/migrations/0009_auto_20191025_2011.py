# Generated by Django 2.2.6 on 2019-10-25 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20191025_2005'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='coupon',
            new_name='voucher',
        ),
    ]