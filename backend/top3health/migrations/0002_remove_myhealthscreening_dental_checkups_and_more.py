# Generated by Django 5.1.7 on 2025-04-23 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('top3health', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myhealthscreening',
            name='Dental_checkups',
        ),
        migrations.RemoveField(
            model_name='myhealthscreening',
            name='Dental_cleanings',
        ),
        migrations.RemoveField(
            model_name='myhealthscreening',
            name='Vision_checkups',
        ),
        migrations.AddField(
            model_name='myhealthscreening',
            name='dental_date',
            field=models.DateField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='myhealthscreening',
            name='vision_date',
            field=models.DateField(blank=True, max_length=10, null=True),
        ),
    ]
