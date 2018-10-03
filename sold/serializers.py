from rest_framework import serializers
from .models import SoldData

class SoldSerializer(serializers.ModelSerializer):
  class Meta:
    model = SoldData
    fields = ('id', 'address', 'zipCode', 'sellPrice', 'date')