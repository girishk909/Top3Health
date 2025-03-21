# Generated by Django 5.1.5 on 2025-03-03 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('top3health', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mydailylog',
            name='balance',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mydailylog',
            name='moderate_intensity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mydailylog',
            name='muscle_build',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mydailylog',
            name='vigorous_intensity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
