from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    columns_configuration = models.JSONField(default=list, blank=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('not_started', 'Not Started'),
        ('terminated', 'Terminated'),
    ]

    DEPARTMENT_CHOICES = [
        ('hr', 'Human Resources'),
        ('engineering', 'Engineering'),
        ('sales', 'Sales'),
        # Add other departments as needed
    ]

    POSITION_CHOICES = [
        ('manager', 'Manager'),
        ('engineer', 'Engineer'),
        ('sales_executive', 'Sales Executive'),
        # Add other positions as needed
    ]

    LOCATION_CHOICES = [
        ('new_york', 'New York'),
        ('san_francisco', 'San Francisco'),
        ('singapore', 'Singapore'),
        # Add other locations as needed
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)
    position = models.CharField(max_length=50, choices=POSITION_CHOICES)
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        indexes = [
            models.Index(fields=['status']),
            models.Index(fields=['company_id']),
            models.Index(fields=['department']),
            models.Index(fields=['position']),
            models.Index(fields=['location']),
        ]
