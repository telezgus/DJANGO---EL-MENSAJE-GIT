# Generated by Django 3.2.9 on 2022-04-10 23:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obras', '0002_auto_20220410_1952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='obras',
            name='codigo',
        ),
    ]