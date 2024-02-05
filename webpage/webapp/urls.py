from django.urls import path, include
from . import views

urlpatterns=[
    path('', views.index),
    path('skills/', views.skills, name='skills'),#path webapp/skills
]