# Generated by Django 3.1.2 on 2020-10-24 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default-book.jpg', upload_to='profile_pics'),
        ),
    ]
