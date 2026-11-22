

from rest_framework import serializers
from . import models


class ServieceSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    
    class Meta:
        model=models.Service
        fields='__all__'

    def get_image(self, obj):
        if obj.image:
            return obj.image.url
        return None