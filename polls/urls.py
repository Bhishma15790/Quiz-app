from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user_login/', views.user_login, name='user_login'),
    path('signup/', views.signup, name='signup'),
    path('quiz/', views.quiz, name='quiz'),
    path('logout/', views.logout_func, name='logout_func'),
    path('userprofile/', views.userprofile, name='userprofile'),
    
]