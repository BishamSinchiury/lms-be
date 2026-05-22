from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import Organization
from .serializers import OrganizationSerializer


class OrganizationListView(APIView):

    permission_classes = [AllowAny]


    def get(self, request):

        organizations = Organization.objects.first()

        serializer = OrganizationSerializer(
            organizations,
            many=True
        )

        return Response(serializer.data)