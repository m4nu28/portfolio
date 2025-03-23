from django.urls import path 
from .import views 

urlpatterns=[
    path('', views.home, name='index'),
    path('toggle_theme/', views.toggle_theme, name='toggle_theme'),
]