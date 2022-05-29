from django.urls import path
from .views import ChatViews

urlpatterns = [
    path("send/",ChatViews.as_view()),
]