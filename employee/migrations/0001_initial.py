# Generated by Django 5.1 on 2024-08-29 17:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('contact_info', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('active', 'Active'), ('not_started', 'Not Started'), ('terminated', 'Terminated')], max_length=20)),
                ('department', models.CharField(choices=[('HR', 'Human Resources'), ('Engineering', 'Engineering'), ('Sales', 'Sales')], max_length=50)),
                ('position', models.CharField(choices=[('Manager', 'Manager'), ('Engineer', 'Engineer'), ('Sales Executive', 'Sales Executive')], max_length=50)),
                ('location', models.CharField(choices=[('New York', 'New York'), ('San Francisco', 'San Francisco'), ('London', 'London')], max_length=50)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.company')),
            ],
        ),
    ]
