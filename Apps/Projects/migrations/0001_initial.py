# Generated by Django 5.1.4 on 2025-01-10 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('project_description', models.TextField()),
                ('project_budget', models.IntegerField()),
                ('project_start_date', models.DateField()),
            ],
        ),
    ]
