from django.urls import path
from . import views

    


urlpatterns = [

    path('about/',views.about_view, name="blog-about"),
    path('', views.home_view, name="blog-home"),
    path('blog/<int:id>/', views.blog, name="blog"),
    path('<int:post_id>/', views.post_detail, name='post_detail'),         

]


    

