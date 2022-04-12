# Generated by Django 3.2.9 on 2022-04-11 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subasta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lote', models.IntegerField(max_length=4, null=True)),
                ('apellido', models.CharField(max_length=30, null=True)),
                ('nombre', models.CharField(max_length=30, null=True)),
                ('titulo', models.CharField(max_length=40, null=True)),
                ('medidas', models.CharField(max_length=20, null=True)),
                ('tecnica', models.CharField(max_length=100, null=True)),
                ('firma', models.TextField(max_length=300, null=True)),
                ('base', models.CharField(max_length=20, null=True)),
                ('imagen', models.ImageField(null=True, upload_to='subasta')),
                ('creado', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Subasta',
                'verbose_name_plural': 'Subastas',
            },
        ),
    ]