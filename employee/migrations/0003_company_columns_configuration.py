# Generated by Django 5.1 on 2024-08-29 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_employee_employee_em_status_33d5fd_idx_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='columns_configuration',
            field=models.JSONField(blank=True, default=list),
        ),
    ]
