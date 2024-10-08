# Generated by Django 5.1 on 2024-08-31 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_alter_employee_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.CharField(choices=[('hr', 'Human Resources'), ('engineering', 'Engineering'), ('sales', 'Sales')], max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.CharField(choices=[('manager', 'Manager'), ('engineer', 'Engineer'), ('sales_executive', 'Sales Executive')], max_length=50),
        ),
    ]
