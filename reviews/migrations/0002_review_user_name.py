# Generated by Django 2.2.4 on 2019-10-19 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='user_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
