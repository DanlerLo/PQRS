# Generated by Django 4.0.4 on 2022-04-20 00:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_pqrs_registro_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vinculo',
            old_name='Vinculo',
            new_name='nombre',
        ),
    ]
