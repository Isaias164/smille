from django.db import models
from django.conf import settings

class ChatUsers(models.Model):
    send = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,related_name="enviados")
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,related_name="recividos")
    message = models.TextField(null=True)
    views = models.BooleanField(default=False)


