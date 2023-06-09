# Generated by Django 4.2 on 2023-05-06 17:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planets_app', '0003_planet_category_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='planet',
            name='day_length',
            field=models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AddField(
            model_name='planet',
            name='distance_sun',
            field=models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AddField(
            model_name='planet',
            name='gravity',
            field=models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AddField(
            model_name='planet',
            name='mass',
            field=models.CharField(default='add a value', max_length=50),
        ),
        migrations.AddField(
            model_name='planet',
            name='moons_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='planet',
            name='rings',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='Y', max_length=1),
        ),
        migrations.AddField(
            model_name='planet',
            name='year_length',
            field=models.IntegerField(default=0),
        ),
    ]
