# Generated by Django 4.1.7 on 2023-12-11 00:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_klient_managers'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kategoria',
            options={'ordering': ['nazwa']},
        ),
    ]
