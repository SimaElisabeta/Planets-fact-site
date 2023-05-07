# Generated by Django 4.2 on 2023-05-06 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planets_app', '0007_atmosphericcomposition'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atmosphericcomposition',
            name='planet',
        ),
        migrations.RemoveField(
            model_name='atmosphericcomposition',
            name='substance',
        ),
        migrations.AddField(
            model_name='atmosphericcomposition',
            name='planet',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='planets_app.planet'),
        ),
        migrations.AddField(
            model_name='atmosphericcomposition',
            name='substance',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='planets_app.substance'),
        ),
    ]
