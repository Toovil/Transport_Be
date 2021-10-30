from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from Transport_apps.models import NewUser
from Transport_apps.serializers import User_Serializer


class UserListView(generics.ListAPIView):
    queryset = NewUser.objects.all()
    serializer_class = User_Serializer
    permission_classes = (IsAuthenticated,)