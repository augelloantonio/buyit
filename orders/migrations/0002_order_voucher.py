# Generated by Django 2.2.4 on 2019-10-16 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='voucher',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
