from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Transport_apps.models import Reserva
from Transport_apps.serializers import Reserva_Serializer

class ReservaView(APIView):
    def get(self,request,*args, **kwargs):
        reservas = Reserva.objects.all()
        serializer = Reserva_Serializer(reservas, many=True)
        return Response(serializer.data)

    def post(self,request, *args, **kwargs):
        serializer = Reserva_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        reservas = self.get_object(pk)
        reservas.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)