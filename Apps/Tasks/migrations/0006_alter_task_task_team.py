# Generated by Django 5.1.4 on 2025-01-14 15:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0005_alter_task_task_team'),
        ('WorkTeams', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_tasks', to='WorkTeams.workteam'),
        ),
    ]
