from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from django.contrib.auth import authenticate,login
from .serializers import LoginSerializers,UsersSerializers

class LoginViews(APIView):
    permission_classes = [AllowAny,]
    
    def post(self,request,*args,**kwargs):
        fields = LoginSerializers(data=request.data)
        if not fields.is_valid():
            return Response(data={"error":True,"message":"Campos incorrectos"})
        
        user_autenticated = authenticate(**fields.validated_data)
        if not user_autenticated:
            return Response(data={"error":True,"message":"Usuario y o contraseñas no validos"})

        login(request,user_autenticated)
        data = {"error":False,"message":"Usuario logeado correctamente"} | fields.get_token(user_autenticated)
        return Response(data=data)

class UsersViews(APIView):
    permission_classes = [AllowAny]

    def post(self,request):
        data = UsersSerializers(data=request.data)
        if not data.is_valid():
            return Response(data={"error":True,"message":"Campos incorrectos"})
        try:
            data = data.create(data.validated_data)
            return Response(data=data)
        except Exception as e:
            return Response(data={"error":True,"message":f"No se pudieron crear los datos {e}"})


            


