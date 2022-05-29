from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import ChatReceiver,ChatSend
from .serializers import SearchUsernameSerializers,SendSerializers



class ChatSendViews(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        data = SendSerializers(data=request.data,context={'request': request})
        if not data.is_valid():
            return Response({"error":True,"message":"Error al recibir la data"})
        response = data.create(data.validated_data)
        return Response(data=response)

class ChatReceivedViews(APIView):
    
    def post(self,request):
        pass