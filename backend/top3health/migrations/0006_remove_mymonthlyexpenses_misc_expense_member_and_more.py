# Generated by Django 5.1.7 on 2025-03-26 23:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('top3health', '0005_myexpenses_created_at_mymonthlyexpenses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mymonthlyexpenses',
            name='Misc_expense_member',
        ),
        migrations.RemoveField(
            model_name='mymonthlyexpenses',
            name='Misc_expenses',
        ),
        migrations.RemoveField(
            model_name='mymonthlyexpenses',
            name='family_eatout_count',
        ),
        migrations.RemoveField(
            model_name='mymonthlyexpenses',
            name='family_grocery_count',
        ),
        migrations.RemoveField(
            model_name='mymonthlyexpenses',
            name='weekly_eatout_cost',
        ),
        migrations.RemoveField(
            model_name='mymonthlyexpenses',
            name='weekly_grocery_cost',
        ),
    ]
