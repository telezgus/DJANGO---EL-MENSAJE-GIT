# Generated by Django 3.2.9 on 2022-04-10 21:28

from django.db import migrations, models
import django.db.models.deletion
import sqlalchemy.sql.expression


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('muestra', '0002_alter_muestra_numero'),
    ]

    operations = [
        migrations.CreateModel(
            name='Obras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellido', models.CharField(max_length=30)),
                ('nombre', models.CharField(max_length=30)),
                ('titulo', models.CharField(max_length=40, null=sqlalchemy.sql.expression.false)),
                ('fecha', models.CharField(max_length=20)),
                ('medidas', models.CharField(max_length=20)),
                ('firma', models.TextField(max_length=300)),
                ('imagen', models.ImageField(null=sqlalchemy.sql.expression.false, upload_to='obras')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('numero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='muestra.muestra')),
            ],
            options={
                'verbose_name': 'Obra',
                'verbose_name_plural': 'Obras',
            },
        ),
    ]
