# Generated by Django 2.2.4 on 2019-10-10 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_review_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='user',
        ),
    ]
