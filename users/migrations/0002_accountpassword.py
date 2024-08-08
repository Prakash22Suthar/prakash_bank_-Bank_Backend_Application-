# Generated by Django 5.0.7 on 2024-08-08 08:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountPassword',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.basemodel')),
                ('password', models.CharField(max_length=255)),
                ('account_holder', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='passwords', to=settings.AUTH_USER_MODEL)),
            ],
            bases=('base.basemodel',),
        ),
    ]
