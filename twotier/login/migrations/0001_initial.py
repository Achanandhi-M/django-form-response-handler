# Generated by Django 5.0.6 on 2024-08-06 17:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^[a-z0-9]([-a-z0-9]*[a-z0-9])?$', 'Only alphanumeric characters and - are allowed.')])),
                ('password', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('^[a-z0-9]([-a-z0-9]*[a-z0-9])?$', 'Only alphanumeric characters and - are allowed.')])),
            ],
        ),
    ]
