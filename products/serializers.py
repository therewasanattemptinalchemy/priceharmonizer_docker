from rest_framework import serializers
from .models import UnifiedProduct

class UnifiedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnifiedProduct
        fields = '__all__'
