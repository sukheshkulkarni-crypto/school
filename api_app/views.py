
from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet
from staff.models import Staff
from .serializers import StaffSerializer
class StaffViewSet(ModelViewSet):
    queryset=Staff.objects.all()
    serializer_class=StaffSerializer
