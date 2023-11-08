from django.shortcuts import render
from rest_framework import viewsets

from .models import Mitbrand
from .serializers import MitbrandSerializer


# Create your views here.

class MitbrandView(viewsets.ModelViewSet):
    queryset = Mitbrand.objects.all()
    serializer_class = MitbrandSerializer
