# Generated by Django 5.1.4 on 2025-01-16 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0016_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$870000$JyLE8UqeoCli4bHJ3gKvaa$wDe/XKvUh3TFLkcsIAkvsdHDmaP083tCr8rAQ9K3iS8=', max_length=128),
        ),
    ]
