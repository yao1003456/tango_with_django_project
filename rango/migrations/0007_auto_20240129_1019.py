# Generated by Django 2.2.28 on 2024-01-29 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0006_auto_20240129_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]