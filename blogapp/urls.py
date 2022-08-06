from django.urls import path
from blogapp import views

urlpatterns = [
    path("",views.index,name="index"),
    path("single/",views.single,name="single"),
]