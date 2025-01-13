# Generated by Django 5.1.4 on 2025-01-13 18:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0003_task_task_status'),
        ('WorkTeams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_team',
            field=models.ForeignKey(default=101, on_delete=django.db.models.deletion.CASCADE, related_name='team_tasks', to='WorkTeams.workteam'),
            preserve_default=False,
        ),
    ]