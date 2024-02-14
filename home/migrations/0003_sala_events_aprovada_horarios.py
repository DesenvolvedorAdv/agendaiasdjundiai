# Generated by Django 5.0 on 2024-02-06 16:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_events_delete_pendencia_delete_reservado_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=15, null=True)),
                ('thumb', models.ImageField(upload_to='thumb_salas')),
                ('tipo', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'db_table': 'tblsala',
            },
        ),
        migrations.AddField(
            model_name='events',
            name='aprovada',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Horarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario_inicio', models.TimeField()),
                ('horario_fim', models.TimeField()),
                ('sala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.sala')),
            ],
            options={
                'db_table': 'tblhorarios',
            },
        ),
    ]
