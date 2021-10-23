from rest_framework import serializers
from Transport_apps.models.newUsers import NewUser

class User_Serializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ['email','user_name','first_name','last_name']
