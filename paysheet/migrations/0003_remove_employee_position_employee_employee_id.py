# Generated by Django 5.0.2 on 2024-03-06 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paysheet', '0002_employee_position'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='position',
        ),
        migrations.AddField(
            model_name='employee',
            name='employee_id',
            field=models.CharField(default='', max_length=20, unique=True),
        ),
    ]