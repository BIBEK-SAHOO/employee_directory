from rest_framework import generics
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from .models import Employee, Company
from .serializers import EmployeeSerializer, CompanySerializer
from rest_framework.views import APIView


class EmployeePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


# class EmployeeSearchView(generics.ListAPIView):
#     queryset = Employee.objects.all().select_related('company_id').only(
#         'first_name', 'last_name', 'contact_info', 'status',
#         'company_id__name', 'department', 'position', 'location'
#     )
#     serializer_class = EmployeeSerializer
#     pagination_class = EmployeePagination
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['status', 'company_id', 'department', 'position', 'location']
#
#     def get_serializer_class(self):
#         company_id = self.request.query_params.get('company_id', None)
#         company_conf = []
#
#         if company_id:
#             try:
#                 company = Company.objects.get(id=company_id)
#                 company_obj = CompanySerializer(company).data
#                 company_conf = company_obj.get("columns_configuration")
#             except Company.DoesNotExist:
#                 pass  # Handle the case where the company does not exist
#
#         if company_conf:
#             return lambda *args, **kwargs: EmployeeSerializer(*args, **kwargs, fields=company_conf)
#
#         return EmployeeSerializer
#
#     def get_queryset(self):
#         # Adding filters dynamically and using Django's query optimization features
#         queryset = super().get_queryset()
#         return queryset


class EmployeeSearchView(generics.ListAPIView):
    queryset = Employee.objects.all().select_related('company_id').only(
                'first_name', 'last_name', 'contact_info', 'status',
                'company_id__name', 'department', 'position', 'location'
            )
    pagination_class = EmployeePagination

    def list(self, request, *args, **kwargs):
        company_id = self.request.query_params.get('company_id')
        # Get the company instance
        try:
            company = Company.objects.get(id=company_id)
        except Company.DoesNotExist:
            return Response({"error": "Company not found"}, status=404)

        # Get the query parameters for filtering
        status = request.GET.getlist('status')
        location = request.GET.getlist('location')
        department = request.GET.getlist('department')
        position = request.GET.getlist('position')

        # Base queryset for employees in the given company
        employees = Employee.objects.filter(company_id=company)

        # Apply filters
        if status:
            employees = employees.filter(status__in=status)
        if location:
            employees = employees.filter(location__in=location)
        if department:
            employees = employees.filter(department__in=department)
        if position:
            employees = employees.filter(position__in=position)

        # Fetch the company's column configuration
        columns = company.columns_configuration

        # Use the dynamic serializer with the fields based on the configuration
        serializer = EmployeeSerializer(employees, many=True, fields=columns)

        # Paginate the queryset
        page = self.paginate_queryset(employees)
        if page is not None:
            serializer = EmployeeSerializer(page, many=True, fields=columns)
            return self.get_paginated_response(serializer.data)

        return Response(serializer.data)


