# Generated by Django 5.0.1 on 2024-01-21 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='price',
            field=models.IntegerField(default=0, max_length=3),
        ),
    ]
