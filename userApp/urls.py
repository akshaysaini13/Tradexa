from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('',views.index, name="user page" ),
    path('register/', views.register, name="register"),
    path('registerform', views.register_form, name="register form"),
    path('login_user', views.login_user, name="login user"),
    path('createpost', views.create_post, name="create post"),
    path('logout_user', views.logout_user, name="logout user"),
    path('createpost', views.create_post, name="create post")


]
