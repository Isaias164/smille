from rest_framework import serializers
from .models import UsersModels
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken


class LoginSerializers(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length = 4)

    def get_token(self,user):

        _user = refresh = RefreshToken.for_user(user)
        return {
        'refresh': str(_user),
        'access': str(_user.access_token),
        }

class UsersSerializers(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(min_length = 4)


    def create(self, validated_data):
        if UsersModels.objects.filter(username=validated_data.get("username")).exists():
            return {"error":True,"message":"El username ya se encuentra en uso. Elija otro username"}

        if UsersModels.objects.filter(email=validated_data.get("email")).exists():
            return {"error":True,"message":"El correo ya se encuentra en uso. Elija otro username"}
        
        p = validated_data.get("password")
        validated_data.update({"password":make_password(p)})
        user_created = UsersModels.objects.create(**validated_data)
        _user = refresh = RefreshToken.for_user(user_created)
        return {
        "error": False,
        "message":"usuario creado con exito",
        'refresh': str(_user),
        'access': str(_user.access_token),
        }

    