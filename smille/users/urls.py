from .views import UsersViews,LoginViews
from django.urls import path

urlpatterns = [
    path("login/",LoginViews.as_view()),
    path("create/",UsersViews.as_view())
]