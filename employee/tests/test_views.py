import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from employee.models import Company, Employee


@pytest.mark.django_db
class TestEmployeeSearchView:
    def setup_method(self):
        self.client = APIClient()
        self.url = reverse('employee-search')  # Update with the correct URL name
        self.company = Company.objects.create(
            name="ACME",
            columns_configuration=['first_name', 'last_name', 'status', 'location', 'department', 'position']
        )
        self.employee_1 = Employee.objects.create(
            first_name="John",
            last_name="Doe",
            contact_info="john@example.com",
            status="active",
            company_id=self.company,
            department="Engineering",
            position="Engineer",
            location="New York"
        )
        self.employee_2 = Employee.objects.create(
            first_name="Jane",
            last_name="Smith",
            contact_info="jane@example.com",
            status="not_started",
            company_id=self.company,
            department="HR",
            position="Manager",
            location="Singapore"
        )

    def test_search_employees_by_status(self):
        response = self.client.get(self.url, {'company_id': self.company.id, 'status': 'active'})
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data['results']) == 1
        assert response.data['results'][0]['first_name'] == 'John'

    def test_search_employees_by_location(self):
        response = self.client.get(self.url, {'company_id': self.company.id, 'location': 'Singapore'})
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data['results']) == 1
        assert response.data['results'][0]['location'] == 'Singapore'

    def test_search_employees_by_department(self):
        response = self.client.get(self.url, {'company_id': self.company.id, 'department': 'HR'})
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data['results']) == 1
        assert response.data['results'][0]['department'] == 'HR'

    def test_search_employees_by_position(self):
        response = self.client.get(self.url, {'company_id': self.company.id, 'position': 'Engineer'})
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data['results']) == 1
        assert response.data['results'][0]['position'] == 'Engineer'

    def test_company_not_found(self):
        response = self.client.get(self.url, {'company_id': 999})
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.data['error'] == 'Company not found'

    def test_search_employees_with_multiple_filters(self):
        response = self.client.get(self.url, {
            'company_id': self.company.id,
            'status': 'active',
            'location': 'New York',
            'department': 'Engineering',
            'position': 'Engineer'
        })
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data['results']) == 1
        assert response.data['results'][0]['first_name'] == 'John'

    def test_pagination(self):
        # Assuming EmployeePagination is set to paginate by 1 item per page
        response = self.client.get(self.url, {'company_id': self.company.id})
        assert response.status_code == status.HTTP_200_OK
        assert 'next' in response.data
        assert len(response.data['results']) == 2

