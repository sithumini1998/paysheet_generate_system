# Generated by Django 5.0.2 on 2024-03-06 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paysheet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='position',
            field=models.CharField(default='Unspecified', max_length=100),
        ),
    ]
