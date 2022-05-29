from django.urls import path
from .views import ChatViews

urlpatterns = [
    path("saludo/",ChatViews.as_view()),
]