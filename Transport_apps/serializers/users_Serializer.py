from rest_framework import serializers
from Transport_apps.models.newUsers import NewUser

class User_Serializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ['email','first_name','last_name', 'password']
        
        def create(self,validated_data):
            userInstance = NewUser.objects.create(**validated_data)
            return userInstance


        def to_representation(self, obj):
            user = NewUser.objects.get(id=obj.email)
            return {
                'email' : user.email, 
                'first_name' : user.first_name,
                'last_name' : user.last_name, 
                'password' : user.password 
            }