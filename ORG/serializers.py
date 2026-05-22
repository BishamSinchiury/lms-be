from rest_framework import serializers
from .models import Organization

# Organization Serializer

class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:

        model = Organization

        fields = [
            "id",
            "name",
            "email",
            "phone",
            "address",
            "website",
            "description",
            "logo",
            "established_date",
            "created_at"
        ]

