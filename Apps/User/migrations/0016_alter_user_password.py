# Generated by Django 5.1.4 on 2025-01-16 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0015_alter_user_password_alter_user_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$870000$QOyA1ZNo9PtR2qgfCvqKNN$KmVfquOUvxpeXHPmRXa4a10cEndw5JRIqSxjde2Ndek=', max_length=128),
        ),
    ]
