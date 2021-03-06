# Generated by Django 4.0.2 on 2022-04-20 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_registrosnuevo_vinculo'),
    ]

    operations = [
        migrations.CreateModel(
            name='registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha', models.DateField()),
                ('Radicado', models.CharField(max_length=50)),
                ('Nombre', models.CharField(max_length=50)),
                ('Telefono', models.CharField(max_length=50)),
                ('Grado_o_area', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('vinculo', models.IntegerField(choices=[[0, 'directivos'], [1, 'docentes'], [2, 'administrativos'], [3, 'padre de familia'], [4, 'estudiante'], [5, 'otros']])),
                ('tipo', models.IntegerField(choices=[[2, 'peticion'], [3, 'queja'], [4, 'sugerencia'], [5, 'reconocimiento']])),
                ('Dependencia', models.CharField(max_length=50)),
                ('Cargo', models.CharField(max_length=50)),
                ('Deescripcion', models.TextField()),
                ('norma', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.vinculo')),
            ],
        ),
        migrations.DeleteModel(
            name='registrosnuevo',
        ),
    ]
