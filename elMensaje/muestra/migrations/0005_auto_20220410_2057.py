# Generated by Django 3.2.9 on 2022-04-10 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muestra', '0004_remove_muestra_numero'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='muestra',
            name='name',
        ),
        migrations.AddField(
            model_name='muestra',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
