# Generated by Django 2.2.4 on 2019-10-10 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='user',
        ),
    ]