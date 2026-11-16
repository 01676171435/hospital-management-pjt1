from rest_framework import serializers

from . import models


class PatientSerializer(serializers.ModelSerializer):
    user= serializers.StringRelatedField(many=False)
    class Meta:
        model=models.Patient
        fields='__all__'


    def validate_mobile_no(self,value):
        if 'x' in value:
            raise serializers.ValidationError("x should not be")
        return value
        
    def validate(self,data):
        nm = data.get('user')

        if nm is None and self.instance:
            nm = self.instance.user

        ct = data.get('mobile_no')

        if ct is None and self.instance:
            ct = self.instance.mobile_no

        if  "y" in ct:
            raise serializers.ValidationError('City must be Ranchi')
        
        cat= super().validate(data)
        print(cat)
        return data 

 