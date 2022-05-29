from django.db import models
from django.conf import settings
    
class ChatSend(models.Model):
    send = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,related_name="enviados")
    message = models.TextField(null=True)
    remitente = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,related_name="remitente")

class ChatReceiver(models.Model):
    receiver = models.ForeignKey(ChatSend,on_delete=models.CASCADE,null=True,related_name="recividos")
    views = models.BooleanField(default=False)

