from django.shortcuts import render
from rest_framework import viewsets
from .serializers import KeepFitSerializer
from .models import KeepFit

# Create your views here.

class KeepFitView(viewsets.ModelViewSet):
    serializer_class = KeepFitSerializer
    queryset = KeepFit.objects.all()