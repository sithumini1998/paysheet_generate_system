# Generated by Django 5.0.2 on 2024-03-11 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paysheet', '0006_employee_account_number_employee_bank_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staycomponent',
            name='component_id',
        ),
    ]
