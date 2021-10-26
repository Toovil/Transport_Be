from rest_framework.views import APIView
from rest_framework.response import Response

from Transport_apps.models import Vehiculo
from Transport_apps.serializers import Vehiculo_Serializer
class VehiculoView(APIView):
    def get(self,request,*args, **kwargs):
        vehiculos = Vehiculo.objects.all()
        serializer = Vehiculo_Serializer(vehiculos, many=True)
        return Response(serializer.data)

"""    def post(self,request, *args, **kwargs):
        serializer = Vehiculo_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)"""