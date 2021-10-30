from rest_framework import serializers
from Transport_apps.models.newUsers import NewUser

class User_Serializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ['id','email','first_name','last_name', 'password']
        
    def create(self, validated_data):
            user = NewUser(**validated_data)
            user.set_password(validated_data['password'])
            user.save()
            return user

    def update(self, instance, validated_data):
        updated_user = super().update(instance, validated_data)
        updated_user.set_password(validated_data['password'])
        updated_user.save()
        return updated_user