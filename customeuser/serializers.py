from rest_framework import serializers
from customeuser.models import CustomeUser

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomeUser
        fields = ['username','user_type','address','email','phone_number']
