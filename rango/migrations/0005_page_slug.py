# Generated by Django 2.2.28 on 2024-01-28 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0004_auto_20240128_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='slug',
            field=models.SlugField(default='', unique=True),
            preserve_default=False,
        ),
    ]
