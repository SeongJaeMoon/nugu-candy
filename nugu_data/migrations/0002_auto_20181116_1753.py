# Generated by Django 2.1.3 on 2018-11-16 08:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('nugu_data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calorie',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
