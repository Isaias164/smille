from rest_framework import serializers
from .models import ChatReceiver,ChatSend
from users.models import UsersModels

class SendSerializers(serializers.Serializer):
    message = serializers.CharField()
    username_receptor = serializers.CharField(required=False)
    username_send = serializers.CharField(required=False)

    def create(self,validate_data):
        data = dict()
        user_received = validate_data.pop("username_receptor",None)
        if not UsersModels.objects.filter(username=user_received).exists():
            return {"error":True,"message":"El usuario al que quieres enviar el mensaje no existe"}

        user_current = self.context.get("request",None)
        user_received = UsersModels.objects.filter(username=user_received).first()
        data.update({"send":user_current.user,"remitente":user_received,"message":validate_data.get("message",None)})
        chat_sended = ChatSend.objects.create(**data)
        chat_received = ChatReceiver.objects.create(receiver=chat_sended)
        return {"error":False,"message":"Mensaje enviado con exito"}

class SearchUsernameSerializers(serializers.Serializer):
    search = serializers.CharField(required=False)

