# Generated by Django 5.1.4 on 2025-01-13 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0002_alter_task_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_status',
            field=models.CharField(choices=[('NEW', 'Nuevo'), ('IN_PROGRES', 'En Progreso'), ('COMPLETED', 'Completado')], default='NEW', max_length=20),
        ),
    ]
