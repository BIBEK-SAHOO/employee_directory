from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import Employee, Company
from .serializers import EmployeeSerializer


class EmployeePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class EmployeeSearchView(generics.ListAPIView):
    serializer_class = EmployeeSerializer
    pagination_class = EmployeePagination

    def get_queryset(self):
        company_id = self.request.query_params.get('company_id')
        # Get the company instance
        try:
            company = Company.objects.get(id=company_id)
        except Company.DoesNotExist:
            return Employee.objects.none()  # Return an empty queryset if company not found

        # Base queryset for employees in the given company
        queryset = Employee.objects.filter(company_id=company)

        # Apply filters
        _status = self.request.GET.getlist('status')
        location = self.request.GET.getlist('location')
        department = self.request.GET.getlist('department')
        position = self.request.GET.getlist('position')

        if _status:
            queryset = queryset.filter(status__in=_status)
        if location:
            queryset = queryset.filter(location__in=location)
        if department:
            queryset = queryset.filter(department__in=department)
        if position:
            queryset = queryset.filter(position__in=position)

        return queryset.select_related('company_id').only(
            'first_name', 'last_name', 'contact_info', 'status',
            'company_id__name', 'department', 'position', 'location'
        ).order_by('id')

    def list(self, request, *args, **kwargs):
        # Get the company instance again for columns configuration
        company_id = self.request.query_params.get('company_id')
        try:
            company = Company.objects.get(id=company_id)
        except Company.DoesNotExist:
            return Response({"error": "Company not found"}, status=status.HTTP_404_NOT_FOUND)

        # Get the filtered queryset
        queryset = self.get_queryset()

        # Fetch the company's column configuration
        columns = company.columns_configuration

        # Paginate the queryset
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = EmployeeSerializer(page, many=True, fields=columns)
            return self.get_paginated_response(serializer.data)

        # Use the dynamic serializer with the fields based on the configuration
        serializer = EmployeeSerializer(queryset, many=True, fields=columns)
        return Response(serializer.data)



