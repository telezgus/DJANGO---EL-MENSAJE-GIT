# Generated by Django 3.2.9 on 2022-04-11 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portada', '0005_portada_titulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='portada',
            name='opcion',
            field=models.CharField(choices=[('M', 'Muestra'), ('S', 'Subasta')], default='M', max_length=30),
        ),
    ]