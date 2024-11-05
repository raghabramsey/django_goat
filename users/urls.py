from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    
    path('users/', views.user_list, name='user_list'),
    path('home/', views.home, name='home'),
]
