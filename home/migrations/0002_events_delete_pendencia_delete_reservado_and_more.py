# Generated by Django 5.0 on 2024-02-02 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('start', models.DateTimeField(blank=True, null=True)),
                ('end', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tblevents',
            },
        ),
        migrations.DeleteModel(
            name='Pendencia',
        ),
        migrations.DeleteModel(
            name='Reservado',
        ),
        migrations.DeleteModel(
            name='Salas',
        ),
    ]
