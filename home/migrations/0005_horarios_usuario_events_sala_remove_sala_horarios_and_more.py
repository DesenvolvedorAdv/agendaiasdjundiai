# Generated by Django 5.0 on 2024-02-08 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_sala_horarios_delete_horarios'),
    ]

    operations = [
        migrations.CreateModel(
            name='Horarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, choices=[('1', '09:30 - 12:00'), ('2', '12:00 - 15:30'), ('3', '15:30 - 19:30'), ('5', '19:30 - 21:30'), ('6', '15:30 - 21:30')], max_length=55, null=True)),
                ('horario_inicio', models.TimeField()),
                ('horario_fim', models.TimeField()),
            ],
            options={
                'db_table': 'tblhorarios',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('departamento', models.CharField(choices=[('ANCIONATO', 'Ancionato'), ('SECRETARIA', 'Secretaria')], max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='events',
            name='sala',
            field=models.ManyToManyField(to='home.sala'),
        ),
        migrations.RemoveField(
            model_name='sala',
            name='horarios',
        ),
        migrations.AddField(
            model_name='sala',
            name='horarios',
            field=models.ManyToManyField(to='home.horarios'),
        ),
    ]
