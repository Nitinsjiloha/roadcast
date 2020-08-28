from rest_framework import serializers
from .models import zone


class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = zone
        fields = ('id',
                  'user',
                  'description',
                  )