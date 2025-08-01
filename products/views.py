from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import UnifiedProduct
from .serializers import UnifiedProductSerializer

class UnifiedProductViewSet(viewsets.ModelViewSet):
    queryset = UnifiedProduct.objects.all()
    serializer_class = UnifiedProductSerializer