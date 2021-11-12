from django.urls import path
from. import  views

urlpatterns = [
    path('login/',views.LoginPage, name='login'),
    path('logout/',views.LogoutUser, name='logout'),
    path('register/',views.registeruser, name='register'),


    path('',views.index,name='products'),
    path('new',views.new),
    
]