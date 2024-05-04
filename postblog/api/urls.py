from django.urls import path
from . import views

urlpatterns = [
    
    path('get', views.getData, name='data'),
    path('add/', views.addPost, name='add'),
    
]
