# Generated by Django 3.2.9 on 2022-04-11 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portada', '0007_alter_portada_opcion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portada',
            name='evento',
        ),
    ]
