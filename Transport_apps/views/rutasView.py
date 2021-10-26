from rest_framework.views import APIView
from rest_framework.response import Response

from Transport_apps.models import Ruta
from Transport_apps.serializers import Ruta_Serializer

class RutaView(APIView):
    def get(self,request,*args, **kwargs):
        rutas = Ruta.objects.all()
        serializer = Ruta_Serializer(rutas, many=True)
        return Response(serializer.data)