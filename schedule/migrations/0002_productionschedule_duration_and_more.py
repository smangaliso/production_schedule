# Generated by Django 4.1.7 on 2023-03-18 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productionschedule',
            name='duration',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='productionschedule',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
