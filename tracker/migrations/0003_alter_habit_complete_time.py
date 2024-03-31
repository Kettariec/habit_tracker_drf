# Generated by Django 5.0.3 on 2024-03-31 14:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_alter_habit_complete_time_alter_habit_periodicity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='complete_time',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(120)], verbose_name='время выполнения(в секундах)'),
        ),
    ]
