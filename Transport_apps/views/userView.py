from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from Transport_apps.serializers import User_Serializer
class UserView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = User_Serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        tokenData = {"username":request.data["username"],
        "password":request.data["password"]}

        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)
























"""from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Transport_apps.models import NewUser
from Transport_apps.serializers import User_Serializer

class UserView(APIView):
    def get(self,request,*args, **kwargs):
        users = NewUser.objects.all()
        serializer = User_Serializer(users, many=True)
        return Response(serializer.data)

    def post(self,request, *args, **kwargs):
        serializer = User_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        reservas = self.get_object(pk)
        reservas.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk, format=None):
        users = self.get_object(pk)
        serializer = User_Serializer(users, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""