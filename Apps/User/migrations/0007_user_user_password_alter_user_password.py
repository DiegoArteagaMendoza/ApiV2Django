# Generated by Django 5.1.4 on 2025-01-14 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0006_remove_user_user_password_user_groups_user_is_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_password',
            field=models.CharField(default='password', max_length=128),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]