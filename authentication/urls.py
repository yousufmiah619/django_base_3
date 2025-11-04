from django.urls import path
from .views import *

urlpatterns = [
    path("register",register,name="registration"),
    path("login/",signin,name="signin"),
    path("logout/",user_logout,name="logout")

]
