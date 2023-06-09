# Generated by Django 4.2 on 2023-04-19 18:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('overview', models.TextField()),
                ('overview_source', models.URLField()),
                ('structure', models.TextField()),
                ('structure_source', models.URLField()),
                ('geology', models.TextField()),
                ('geology_source', models.URLField()),
                ('rotation', models.CharField(max_length=50)),
                ('revolution', models.CharField(max_length=50)),
                ('radius', models.CharField(max_length=50)),
                ('temperature', models.CharField(max_length=50)),
                ('planet_image', models.FileField(upload_to='static/images/', validators=[django.core.validators.FileExtensionValidator(['pdf', 'doc', 'svg'])])),
                ('internal_image', models.FileField(upload_to='static/images/', validators=[django.core.validators.FileExtensionValidator(['pdf', 'doc', 'svg'])])),
                ('geology_image', models.ImageField(upload_to='static/images/')),
            ],
        ),
    ]
