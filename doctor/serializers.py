from rest_framework import serializers

from . import models


class SpecializationSerializer(serializers.ModelSerializer):
  
    class Meta:
        model=models.Specialization
        fields='__all__'


class DesignationSerializer(serializers.ModelSerializer):
  
    class Meta:
        model=models.Designation
        fields='__all__'

class AvailableTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.AvailableTime
        fields='__all__'


class DoctorSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model=models.Doctor
        fields='__all__'

    def get_image(self, obj):
        if obj.image:
            return obj.image.url
        return None
        
class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model=models.Review
        fields='__all__'