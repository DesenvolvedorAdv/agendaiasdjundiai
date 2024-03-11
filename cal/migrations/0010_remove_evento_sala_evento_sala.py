# Generated by Django 5.0 on 2024-03-01 14:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cal", "0009_alter_evento_usuario"),
        ("home", "0011_delete_horariobloqueado_remove_sala_cor"),
    ]

    operations = [
        migrations.RemoveField(model_name="evento", name="sala",),
        migrations.AddField(
            model_name="evento",
            name="sala",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="home.sala"
            ),
        ),
    ]