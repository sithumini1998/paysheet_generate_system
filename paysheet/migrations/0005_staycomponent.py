# Generated by Django 5.0.2 on 2024-03-09 05:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paysheet', '0004_salary'),
    ]

    operations = [
        migrations.CreateModel(
            name='StayComponent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('component_id', models.CharField(default='', max_length=20, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('is_deduction', models.BooleanField(default=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('salary_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paysheet.salary')),
            ],
        ),
    ]
