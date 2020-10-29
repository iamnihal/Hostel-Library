# Generated by Django 3.1.2 on 2020-10-29 09:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookrequest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookrequest',
            name='semester',
            field=models.CharField(max_length=1, validators=[django.core.validators.RegexValidator(message='Invalid Semester.', regex='^[1-8]$')]),
        ),
    ]