from django.urls import path
from blogapp import views

urlpatterns = [
    path("",views.index,name="index"),
    path("post/<int:pk>",views.PostDetailViews.as_view(),name="post"),
    path("post/create",views.PostCreate.as_view(),name="post_create"),
]