# Generated by Django 3.2.9 on 2022-04-11 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subasta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subasta',
            name='lote',
            field=models.IntegerField(null=True),
        ),
    ]
