from django.urls import path, include
from . import views 


app_name = 'user_auth'
urlpatterns = [
    path('', views.user_login, name='login'),
    path('auth_user/', views.auth_user, name='auth_user'),
    path('auth_user/show_user/', views.show_user, name='show_user'),
    path('register/', views.user_registration, name='register')

]