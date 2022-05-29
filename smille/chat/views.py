from rest_framework.views import APIView
from rest_framework.response import Response




class ChatViews(APIView):

    def post(self,request):
        print(request.user)
        return Response({"saludo":f"Hola, com estas "})