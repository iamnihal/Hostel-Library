# Generated by Django 3.1.2 on 2020-10-29 09:45

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.TextField(max_length=40, unique=True)),
                ('semester', models.IntegerField(max_length=1)),
                ('student_name', models.CharField(max_length=15)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('contact_number', models.CharField(default='0', max_length=10, validators=[django.core.validators.RegexValidator(message='Check your format of phone number. Up to 10 digits allowed.', regex='^\\d{10}$')])),
            ],
        ),
    ]