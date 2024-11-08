from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_goat, name='register_goat'),
    path('', views.goat_list, name='goat_list'),
    path('<int:goat_id>/', views.goat_detail, name='goat_detail'),
]
