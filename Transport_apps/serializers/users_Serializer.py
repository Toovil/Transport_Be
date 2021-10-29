from rest_framework import serializers
from Transport_apps.models.newUsers import NewUser

class User_Serializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ['email','first_name','last_name']
        
        def create(self,validated_data):
            userInstance = NewUser.objects.create(**validated_data)
            return userInstance


        def to_representation(self, obj):
            user = NewUser.objects.get(id=obj.email)
            return {
                'email' : NewUser.email, 
                'first_name' : NewUser.first_name,
                'last_name' : NewUser.last_name,  
            }