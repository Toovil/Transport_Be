from rest_framework import status, views
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from Transport_apps.models.vehiculos import Vehiculo
from Transport_apps.serializers.vehiculos_Serializer import Vehiculo_Serializer

@api_view(['GET',])
def vehiculos_Detail_View(request, slug):
    try:
        vehiculos = Vehiculo.objects.get(slug=slug)
    except Vehiculo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = Vehiculo_Serializer(vehiculos)
        return Response(serializer.data) 

"""@api_view(['PUT',])
def vehiculos_Delete_View(request, slug):
    try:
        vehiculos = Vehiculo.objects.get(slug=slug)
    except Vehiculo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = Vehiculo_Serializer(vehiculos, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['Success'] = 'update successful'
            return Response(data = data)
        return Response(serializer.data) 

@api_view(['DELETE',])
def vehiculos_Update_View(request, slug):
    try:
        vehiculos = Vehiculo.objects.get(slug=slug)
    except Vehiculo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        operation = vehiculos.delete()
        data = {}
        if operation:
            data['Success'] = 'delete successful'
        else:
            data['Failure'] = 'delete failed'
        return Response(data =data) 

@api_view(['POST',])
def vehiculos_create_View(request, slug):
    account = Account.objects.get(pk=1)

    vehiculos = 
    
    if request.method == 'DELETE':
        operation = vehiculos.delete()
        data = {}
        if operation:
            data['Success'] = 'delete successful'
        else:
            data['Failure'] = 'delete failed'
        return Response(data =data) """
