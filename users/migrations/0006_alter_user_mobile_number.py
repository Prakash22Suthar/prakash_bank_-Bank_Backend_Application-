# Generated by Django 4.1.13 on 2024-08-13 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_mobile_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile_number',
            field=models.PositiveIntegerField(blank=True, default=None, null=True),
        ),
    ]
