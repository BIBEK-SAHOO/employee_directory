from rest_framework import serializers
from .models import Employee, Company


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    # company = serializers.StringRelatedField(source='company_id')

    class Meta:
        model = Employee
        fields = "__all__"  # We'll dynamically set this

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        super(EmployeeSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)
