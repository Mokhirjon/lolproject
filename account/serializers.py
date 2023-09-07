from .models import Customuser
from rest_framework.serializers import ModelSerializer

from rest_framework import serializers

class CustomuserSerializers(ModelSerializer):
    password = serializers.CharField(write_only
                                     =True)

    class Meta:
        model = Customuser
        fields = ('username','password','phone','role','first_name')
    def create(self, validated_data):
        user = Customuser(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            phone=validated_data['phone'],
            role=validated_data['role',1]
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
